Title: HIDS-Agent开发之抓取DNS请求和异常分析 
Date: 2018-08-13 20:20
Modified: 2018-08-13 20:20
Category: 安全
Tags: HIDS
Slug: R12
Authors: nJcx
Summary: HIDS-Agent开发之抓取DNS请求和异常分析 ~


#### 介绍


使用 cgroups + etcd + kafka 开发而成的hids的架构，agent 部分使用go 开发而成， 会把采集的数据写入到kafka里面，由后端的规则引擎（go开发而成）消费，配置部分以及agent存活使用etcd。关于agent 使用cgroups限制资源以及使用etcd做配置管理agent存活已经在前文介绍了一下。下面介绍一下agent抓取DNS请求和异常分析的部分



![agent](../images/dnsgenformat.png)


![agent](../images/dnsheaderformat.png)


![agent](../images/02-DNS-Message-Header-Flags-Codes.png)

![agent](../images/dnsquestionformat.png)

![agent](../images/dnsrrformat.png)


DNS 报文格式
DNS 请求的格式和响应格式差不多，就不单独讲了。从 UDP 数据包的正文部分算起，DNS 报文的结构按顺序如下：

数据类型	Ethereal 里的名字	说明
uint16_t	Transaction ID	标识符。下文说明
uint16_t	Flags	参数。下文说明
uint16_t	Questions	询问列表的数目
uint16_t	Answer RRs	(直接) 的回答数
uint16_t	Authority RRs	认证机构数目（仅响应包里有）
uint16_t	Additional RRs	附加信息数目（仅响应包里有）
variable	Queries	请求数据的正文。请求包中只有这个。响应包也会附上原本的请求数据
variable	Answers	响应数据的正文
variable	Authortative name servers	域名管理机构数据
variable	Additional records	附加信息数据
Transaction ID：这是由 client 端指定的标识数据，DNS server 会将这个字段原样返回，client 端可以用来区分不同的 DNS 请求
RR：Resource Record 的缩写
Flags
16 bits 的值，各部分按顺序如下（按顺序：位号、Ethereal 名称、说明）：

Bit 15，Response：0 表示查询，1 表示响应（query / response）
Bit 14~11, Opcode：查询类型——请求和响应包都适用：

0：普通查询（最常用的）
1：反向查询
2：服务器状态请求
3：通知
4：更新（貌似是用在 DDNS 的？）
Bit 10, Authoritative：用于响应包，判断服务器是否一个认证的域服务器
Bit 9, Truncated：报文是否被截断了。收发包都用
Bit 8, Recursion desired：收发包都用，表示是否需要用递归。作为 client 端，最好置 1，要不然 DNS 不执行递归查询，将有很多数据没能查到
Bit 7, Recursion available：响应包用，表示服务器是否有能力使用递归查询
Bit 6：这个数据段，Ethereal 说是保留位，而书中表示数据是否是鉴别的——求确认
Bit 5, Answer authenticated：数据是否被服务器鉴定过（貌似抓到的包里都是 0）
Bit 4, Reserved
Bit 3~0, Reply code：响应状态码，如下（参见 Micrisoft 资料 的 “DNS update message flags field” 小节）：

0：OK
1：查询格式错误
2：服务器内部错误
3：名字不存在
4：这个错误码不支持
5：请求被拒绝
6：name 在不应当出现时出现（什么鬼）
7：RR 设置不存在
8：RR 设置应当存在但是却不存在（什么鬼）
9：服务器不具备改管理区的权限
10：name 不在管理区中
资源记录（RR）的格式
每一条 RR 的格式如下：

数据类型	Ethereal 里的名字	说明
variable	Name	资源的域名——其实前文已经出现了
uint16_t	Type	类型。下文说明
uint16_t	Class	大多数是 0x0001，代表 IN
uint32_t	Time to Live	TTL 秒数
uint16_t	Data length	当前 RR 剩余部分的长度
variable		RR 主数据
如果是请求数据的话，那么 TTL、Data Length 和 RR 主数据都不需要

Type 的大部分值在 RFC-1035 中定义，此外的一些在其他文档定义（比如 IPv6）。我会用到的有：

1：“A”，表示 IPv4 地址
2：“NS”，域名服务器的名字
28：“AAAA”，表示 IPv6 地址
5：“CNAME”，规范名，经常会有一个 CNAME 跟着一票 A 和 AAAA

#### 


#### 


#### 


#### 


####  



实例代码


```go


import (
	"fmt"
	"log"
	"errors"
	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
	"github.com/google/gopacket/pcap"

)

var (
	SrcIP      string
	DstIP      string
)


func getDnsPcapHandle(ip string) (*pcap.Handle, error) {
	devs, err := pcap.FindAllDevs()
	if err != nil {
		return nil, err
	}
	var device string
	for _, dev := range devs {
		for _, v := range dev.Addresses {
			if v.IP.String() == ip {
				device = dev.Name
				break
			}
		}
	}

	if device == "" {
		return nil, errors.New("find device error")
	}
	h, err := pcap.OpenLive(device, 65535, true, pcap.BlockForever)
	if err != nil {
		return nil, err
	}
	log.Println("StartDnSMonitor")
	err = h.SetBPFFilter("udp and port 53")
	if err != nil {
		return nil, err
	}
	return h, nil
}


func StartDNSNetSniff(resultChan chan map[string]string) {

	var eth layers.Ethernet
	var ip4 layers.IPv4
	var udp layers.UDP
	var dns layers.DNS
	var payload gopacket.Payload

	var resultdata =make(map[string]string)
	h, err := getDnsPcapHandle("10.10.16.1")
	if err != nil {
		fmt.Println("get pcaphandle failed, err:", err)
		return
	}

	parser := gopacket.NewDecodingLayerParser(layers.LayerTypeEthernet, &eth, &ip4,&udp, &dns, &payload)
	decodedLayers := make([]gopacket.LayerType, 0, 10)
	for {
		data, _, err := h.ReadPacketData()
		if err != nil {
			fmt.Println("Error reading packet data: ", err)
			continue
		}
		err = parser.DecodeLayers(data, &decodedLayers)
		for _, typ := range decodedLayers {
			switch typ {
			case layers.LayerTypeIPv4:
				SrcIP = ip4.SrcIP.String()
				DstIP = ip4.DstIP.String()
			case layers.LayerTypeDNS:
				if !dns.QR {
					for _, dnsQuestion := range dns.Questions {
						resultdata["source"] = "dns"
						resultdata["src"] = SrcIP
						resultdata["dst"] = DstIP
						resultdata["domain"] = string(dnsQuestion.Name)
						resultdata["type"] = dnsQuestion.Type.String()
						resultdata["class"] = dnsQuestion.Class.String()
						resultChan <- resultdata

					}
				}
			}
		}
	}
}


```




