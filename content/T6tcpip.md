Title: NIDS开发之IP分片重组和TCP段重组
Date: 2024-10-29 20:20
Modified: 2024-10-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T6
Authors: nJcx
Summary: NIDS开发之IP分片重组和TCP段重组 ~

#### 介绍

NIDS（Network Intrusion Detection System，网络入侵检测系统）开发过程中，主要拆解成两个部分开发， 第一的DPI深度包解析，第二就是规则引擎。DPI深度包解析是指NIDS通过监听网络流量来捕捉数据包、协议识别、拆解成字段过程。这些数据包包含了从网络的一个点传输到另一个点的信息。DPI是NIDS分析网络活动以检测潜在入侵行为的基础步骤， 捕捉数据包的工具有 libpcap 、PF_RING、DPDK等等。DPI深度包解析工具有PacketBeat、NDPI、Zeek、Suricata等等。


在TCP/IP协议栈中，数据包的重组主要涉及两个方面：IP分片重组和TCP段重组。

IP分片重组：当一个IP数据报由于过大而无法在一个物理网络上进行传输时，它可能会被分成多个较小的片段（分片），每个分片作为一个独立的IP数据报进行传输。这些分片最终需要在目的地处重新组装成原始的数据报。这个过程称为IP分片重组。IP头部包含了一个标识字段、一个标志字段和一个分片偏移字段，它们共同作用以帮助目的主机正确地重组这些分片。

TCP段重组：TCP（传输控制协议）是面向连接的，并提供可靠的数据传输服务。在数据传输过程中，发送方可能会将数据分割成多个TCP段进行发送。因为网络中的路由和延迟不同，这些TCP段可能不会按照它们被发送的顺序到达接收方。TCP使用序列号和确认机制来确保所有发送的数据都能够按照正确的顺序被重组。接收方根据序列号对收到的TCP段进行排序，并在必要时等待丢失段的重传，从而实现数据的正确重组。


为什么NIDS 涉及到IP分片重组和TCP段重组 ？ 这些不是TCP/IP协议栈的事情吗？
因为NIDS使用 libpcap 或者 DPDK， 抓取的都是一帧， 一个IP分片通常被封装成一帧进行传输。 当数据比较大的时候，比如 http post 一个稍大的json， 经过TCP段重组（没有IP分片），才能看到完整的 json。在TCP/IP协议栈中， 每一层对上都是透明的， 而在NIDS 中，每一层都需要自己重组。



IP分片和TCP分段是一回事吗 ？

IP分片和TCP分段不是一回事，它们是发生在网络协议栈不同层次的数据切分机制, 一般不同时发生。具体区别如下：

	IP分片：发生在网络层，由IP协议处理，由于网络链路层的MTU（最大传输单元）限制，当IP数据报大小超过MTU时，需要进行分片。
	TCP分片：发生在传输层，由TCP协议处理，为了适应MSS（最大分段大小），避免IP层分片，TCP会根据MSS对数据进行分段。

TCP分段是非常常见的，因为几乎所有的HTTP、FTP等基于TCP的应用层协议都依赖于这种机制来传输数据。TCP协议的设计本身就支持这种分段和重组操作，以适应各种网络状况并保证数据传输的可靠性。而IP分片则更多是一种在网络层面上处理特殊情况的机制，理想情况下应该尽量避免，因为它带来的问题比它解决的问题还要多。



IP 分片示例


假设主机 A 要通过以太网向主机 B 发送一个总大小为 **4000 字节**的 IP 数据报。  

- 网络路径的 MTU（最大传输单元）为 **1500 字节**。
- IP 首部长度为 **20 字节**。

由于数据报的总长度（4000 字节）超过了 MTU（1500 字节），因此需要进行 **IP 分片**。



IP 分片过程

 1. 计算 IP 分片数量
 
- 每个分片的最大有效载荷 1500 - 20(IP首部) = 1480  字节。
- 总数据量为 **4000 字节**，因此需要分成：4000 ÷ 1480  = 3   

 2. IP 分片详细信息

| 分片编号 | 数据范围      | 数据长度 | 偏移量（字节） | 偏移量（单位） | MF 标志位 | 总长度 |
|----------|---------------|----------|----------------|----------------|-----------|--------|
| 第 1 片  | 0 ~ 1479      | 1480     | 0              | 0              | 1         | 1500   |
| 第 2 片  | 1480 ~ 2959   | 1480     | 1480           | 185            | 1         | 1500   |
| 第 3 片  | 2960 ~ 3999   | 1040     | 2960           | 370            | 0         | 1060   |


> **偏移量单位说明**: 偏移量是以 **8 字节** 为单位计算的，因此实际偏移量需要除以 8。



分片的具体内容

 第 1 片
 
- **标识符**: 12345
- **MF 标志位**: 1 （表示还有后续分片）
- **偏移量**: 0
- **数据负载**: 前 1480 字节的数据
- **总长度**: 1500 字节（1480 + 20）

第 2 片

- **标识符**: 12345
- **MF 标志位**: 1 （表示还有后续分片）
- **偏移量**: 185 （1480 ÷ 8 = 185）
- **数据负载**: 接下来的 1480 字节的数据
- **总长度**: 1500 字节（1480 + 20）

第 3 片

- **标识符**: 12345
- **MF 标志位**: 0 （表示这是最后一个分片）
- **偏移量**: 370 （2960 ÷ 8 = 370）
- **数据负载**: 最后的 1040 字节的数据
- **总长度**: 1060 字节（1040 + 20）



重组过程

当主机 B 收到这些分片时：

1. 主机 B 根据 **标识符** 来确定这些分片属于同一个原始数据报。
2. 根据 **偏移量** 和 **MF 标志位**，将所有分片按顺序拼接起来。
3. 重组后的数据报与原始数据报完全相同，包含 **4000 字节** 的数据。




通过这个例子可以清楚地看到：

- **IP 分片** 是基于网络路径的 MTU 进行的，确保每个分片的总长度不超过 MTU。
- 主机 B 通过 **标识符**、**偏移量** 和 **MF 标志位**，能够准确地将分片重组为原始数据报。




TCP 分段示例

假设主机 A 要通过以太网向主机 B 发送一个总大小为 **4000 字节**的应用层数据。  

- 网络路径的 MTU（最大传输单元）为 **1500 字节**。
- TCP 的 MSS（最大分段大小）协商后为 **1460 字节**（即 1500 - 20(IP首部) - 20(TCP首部)）。
- IP 首部长度为 **20 字节**。

由于应用层数据的大小超过了 MSS 的限制，因此需要进行 **TCP 分段**。



TCP 分段过程

 1. 计算 TCP 分段数量
 
	- 每个 TCP 数据段的最大有效载荷为 **1460 字节**。
	- 总数据量为 **4000 字节**，因此需要分成：
	   4000 ÷ 1460  = 3  


 2. TCP 分段详细信息

| 分段编号 | 序列号范围   | 数据长度 | TCP 首部长度 | IP 首部长度 | 总长度 |
|----------|--------------|----------|--------------|-------------|--------|
| 第 1 段  | 1 ~ 1460     | 1460     | 20           | 20          | 1500   |
| 第 2 段  | 1461 ~ 2920  | 1460     | 20           | 20          | 1500   |
| 第 3 段  | 2921 ~ 4000  | 1080     | 20           | 20          | 1120   |



重组过程

当主机 B 收到这些分段时：

1. 主机 B 根据 **TCP 序列号** 将所有分段按顺序拼接起来。
2. 最终得到完整的 **4000 字节** 数据，并交给应用层。



通过这个例子可以清楚地看到：

- **TCP 分段** 是基于 MSS 进行的，确保每个分段的总长度不超过 MTU。
- 主机 B 通过 **TCP 序列号**，能够准确地将分段重组为原始数据。
- 在本例中，由于网络路径的 MTU 为 1500 字节，且 MSS 为 1460 字节，因此无需进行 IP 分片。



####  IP分片重组

我们看一下, Suricata 是怎么处理IP分片重组的:


1,核心数据结构:


```bash

// defrag.h - 分片重组的主要数据结构
typedef struct DefragTracker_ {
    SCMutex lock;        // 互斥锁保护
    uint32_t id;         // IP 包 ID
    uint8_t proto;       // IP 协议
    uint8_t policy;      // 重组策略
    uint8_t af;          // 地址族(IPv4/IPv6)
    uint8_t seen_last;   // 是否看到最后一个分片
    Address src_addr;    // 源地址
    Address dst_addr;    // 目的地址
    struct IP_FRAGMENTS fragment_tree; // 分片树
} DefragTracker;

// 单个分片的结构
typedef struct Frag_ {
    uint16_t offset;     // 分片偏移 
    uint32_t len;        // 分片长度
    uint8_t more_frags;  // 是否还有更多分片
    uint8_t *pkt;        // 实际分片数据
    RB_ENTRY(Frag_) rb;  // 红黑树节点
} Frag;



```

2, 重组流程:

```bash

// decode-ipv4.c 中的处理流程
int DecodeIPV4(ThreadVars *tv, DecodeThreadVars *dtv, Packet *p, const uint8_t *pkt, uint16_t len)
{
    // 1. 检测到分片标记
    if (IPV4_GET_RAW_FRAGOFFSET(ip4h) > 0 || IPV4_GET_RAW_FLAG_MF(ip4h)) {
        // 2. 调用 Defrag 进行重组
        Packet *rp = Defrag(tv, dtv, p);
        if (rp != NULL) {
            // 3. 重组成功,将重组后的包加入队列
            PacketEnqueueNoLock(&tv->decode_pq, rp);
        }
        p->flags |= PKT_IS_FRAGMENT;
        return TM_ECODE_OK;
    }
}

```



IPv4 通过检查分片偏移(Fragment Offset)和 More Fragments 标志位识别分片, IPv6 通过分片扩展头(Fragment Extension Header)识别分片. 使用红黑树存储各个分片, 按照偏移量排序, 通过 DefragTracker 跟踪同一数据包的所有分片, 设置超时机制避免资源耗尽.

重要函数:

```bash

// 分片重组的主函数
Packet *Defrag(ThreadVars *tv, DecodeThreadVars *dtv, Packet *p) 
{
    // 1. 创建/查找分片追踪器
    // 2. 将分片加入分片树
    // 3. 检查是否可以重组
    // 4. 重组分片生成新包
    // 5. 返回重组后的包
}

// 处理 IPv6 分片头
void DecodeIPV6FragHeader(Packet *p, const uint8_t *pkt, uint16_t hdrextlen, 
                         uint16_t plen, uint16_t prev_hdrextlen)
{
    // 解析分片头
    // 设置分片标记
    // 进行合法性检查
}


```

所以总的来说,Suricata 的 IP 分片重组实现主要基于:

	使用分片跟踪器(DefragTracker)和分片树管理分片
	支持 IPv4 和 IPv6 协议
	有完善的错误检测机制
	通过队列管理重组后的包
	采用互斥锁保证线程安全
	这个实现比较完整地覆盖了 IP 分片重组的各个方面,包括分片识别、存储、重组、验证等环节。


####  TCP段重组 


Zeek 中 TCP 分段重组的实现:

1.核心数据结构

```bash

// src/analyzer/protocol/tcp/TCP_Reassembler.h
// TCP_Reassembler 类
class TCP_Reassembler final : public Reassembler {
    enum Type {
        Direct,  // 直接传递到目标分析器 
        Forward  // 转发到目标分析器的子节点
    }; 
    
    TCP_Endpoint* endp;        // TCP 端点
    bool had_gap;             // 是否有数据空洞
    bool deliver_tcp_contents; // 是否传递TCP内容
    uint64_t seq_to_skip;     // 要跳过的序列号
    FilePtr record_contents_file; // 记录内容的文件
};

// src/packet_analysis/protocol/tcp/TCPSessionAdapter.h
// TCPSessionAdapter 类
class TCPSessionAdapter {
    TCP_Endpoint* orig;         // 发起方端点
    TCP_Endpoint* resp;         // 响应方端点
    bool reassembling;          // 是否正在重组
    bool is_partial;            // 是否部分连接
    uint64_t rel_data_seq;      // 相对数据序列号
};



```

2, 重组流程

```bash

// 启用重组:
void TCPSessionAdapter::EnableReassembly() {
    SetReassembler(
        new TCP_Reassembler(this, TCP_Reassembler::Forward, orig),
        new TCP_Reassembler(this, TCP_Reassembler::Forward, resp)
    );
}

// 数据到达处理:
// src/analyzer/protocol/tcp/TCP_Reassembler.cc - TCP 重组器实现

void TCP_Reassembler::DataSent(double t, uint64_t seq, int len, 
                              const u_char* data) {
    
    // 检查是否需要跳过
    if (IsSkippedContents(seq, len)) 
        return;
    
    // 处理数据空洞
    if (seq > last_reassem_seq) {
        Gap(last_reassem_seq, seq - last_reassem_seq);
        had_gap = true;
    }
    
    // 交付数据
    DeliverBlock(seq, len, data);
}

// src/packet_analysis/protocol/tcp/TCPSessionAdapter.cc
void TCPSessionAdapter::Process(bool is_orig, const struct tcphdr* tp,
                              int len, const IP_Hdr* ip) {
    // 获取序列号    
    uint32_t base_seq = ntohl(tp->th_seq);
    
    // 处理标志位
    TCP_Flags flags(tp);
    
    // 分析状态
    UpdateStateMachine(t, endpoint, peer, base_seq, flags); 
    
    // 数据重组
    if (len > 0 && !flags.RST())
        endpoint->DataSent(t, base_seq, len, data);
}



//  空洞处理:
void TCP_Reassembler::Gap(uint64_t seq, uint64_t len) {
    // 报告空洞
    if (report_gap(endp, endp->peer))
        dst_analyzer->EnqueueConnEvent(content_gap, ...);
    
    // 更新状态
    had_gap = true;
}


// 跟踪 TCP 状态:
void TCPSessionAdapter::UpdateStateMachine(TCP_Endpoint* endpoint,
    TCP_Endpoint* peer, uint32_t seq, TCP_Flags flags)
{
    // SYN 处理
    if (flags.SYN()) {
        if (is_orig) {
            endpoint->SetState(TCP_ENDPOINT_SYN_SENT);
        } else {
            endpoint->SetState(TCP_ENDPOINT_ESTABLISHED); 
        }
    }

    // FIN 处理  
    if (flags.FIN()) {
        endpoint->SetState(TCP_ENDPOINT_CLOSED);
    }

    // RST 处理
    if (flags.RST()) {
        endpoint->SetState(TCP_ENDPOINT_RESET);
    }
}


```


Zeek 使用两个主要组件来处理 TCP 分段重组:

```
	TCP_Reassembler: 专门负责重组的核心组件
	TCPSessionAdapter: 管理整个 TCP 会话的组件
```

就像是一个拼图游戏,TCP_Reassembler 负责把所有碎片(TCP分段)拼在一起,而 TCPSessionAdapter 则像是一个总管理员,负责监督整个拼图过程。

当一个 TCP 包到达时,处理流程是:

	数据排序
	检查序列号是否连续
	如果是期望的下一个序列号,直接处理
	如果不是,放入缓存等待处理
	空洞处理
	当发现序列号不连续时,记录为"空洞"
	继续接收后续数据,等待空洞被填补


Zeek 使用几个关键机制来管理数据:

	序列号跟踪
	记录已处理的最后序列号
	检查新数据的序列号是否符合预期
	缓存管理
	对乱序到达的数据进行缓存
	定期清理过期的缓存数据
	状态跟踪
	跟踪连接状态(SYN, FIN, RST等)
	根据状态决定如何处理数据



想象你在收集一系列明信片(TCP分段):

	每张明信片都有序号(序列号)
	你需要按顺序排列它们才能看到完整图片
	有时候明信片到达的顺序是乱的(乱序数据)
	有时候有明信片丢失了(数据空洞)
	你需要等待缺失的明信片(填补空洞)
	最后将所有明信片按顺序排好(重组完成)
	
Zeek 就是在做类似的工作,但是它同时在处理两个方向的"明信片集",而且速度要快得多。
这种实现方式既保证了数据的完整性和正确性,又提供了足够的灵活性和性能,使得 Zeek 能够有效地分析网络流量。





#### Demo


```bash

// TCP 流结构
typedef struct {
    uint32_t src_ip;
    uint32_t dst_ip;
    uint16_t src_port;
    uint16_t dst_port;
    uint32_t next_seq;    // 关键字段：下一个期望的序列号
    uint32_t init_seq;    // 初始序列号
    time_t last_seen;
    unsigned char *stream;  // 存储重组数据的缓冲区
    int stream_size;       // 当前已重组的数据大小
    flow_state state;
    char src_ip_str[INET_ADDRSTRLEN];
    char dst_ip_str[INET_ADDRSTRLEN];
} tcp_flow_t;

// 全局变量
tcp_flow_t flows[MAX_FLOWS];
int flow_count = 0;

```

```bash

void handle_tcp_packet(const struct ip *ip_header, const struct tcphdr *tcp_header,
                       const unsigned char *payload, int payload_len) {
    tcp_flow_t *flow = find_or_create_flow(ip_header, tcp_header);
    if (!flow) return;

    if (tcp_header->th_flags & TH_SYN) {
        if (flow->state == FLOW_NEW) {
            flow->state = FLOW_ESTABLISHED;
            flow->next_seq = ntohl(tcp_header->th_seq) + 1;  // SYN包，序列号+1
            print_flow_info(flow, "SYN");
        }
    }
    else if (tcp_header->th_flags & TH_FIN || tcp_header->th_flags & TH_RST) {
        flow->state = FLOW_CLOSED;
        print_flow_info(flow, tcp_header->th_flags & TH_FIN ? "FIN" : "RST");
        process_stream_data(flow);
    }
    else if (payload_len > 0) {
        uint32_t seq = ntohl(tcp_header->th_seq);
        if (seq == flow->next_seq) {  // 关键重组逻辑：检查序列号是否符合预期
            // 确保不会超出缓冲区
            int copy_len = payload_len;
            if (flow->stream_size + copy_len > MAX_STREAM_SIZE) {
                copy_len = MAX_STREAM_SIZE - flow->stream_size;
            }

            if (copy_len > 0) {
                // 按序复制数据到重组缓冲区
                memcpy(flow->stream + flow->stream_size, payload, copy_len);
                flow->stream_size += copy_len;
                flow->next_seq = seq + copy_len;  // 更新下一个期望的序列号
                flow->state = FLOW_DATA;
                print_flow_info(flow, "DATA");
            }
        }
    }
}


```

实现了基本的流跟踪功能, 序列号检查, 按序重组数据, 状态跟踪（SYN, FIN, RST等）

代码在这里:

https://github.com/njcx/pcap_tcp_reassemble



