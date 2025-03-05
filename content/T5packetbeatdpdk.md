Title: 让packetbeat 插上dpdk的翅膀
Date: 2023-09-29 20:20
Modified: 2023-09-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T5
Authors: nJcx
Summary: 让packetbeat 插上dpdk的翅膀 ~


#### 介绍

Packetbeat 是一款开源的网络数据包分析工具，由Elastic公司开发并维护。它能够实时捕获和分析网络中的传输数据，主要用于监控和分析应用层协议的数据传输情况，如HTTP、MySQL、PostgreSQL等。通过这种方式，Packetbeat可以帮助用户了解网络性能、追踪应用程序错误以及监控安全事件。

Packetbeat的工作原理

- 数据抓取：Packetbeat使用libpcap库（在Linux和macOS上）或WinPcap/Npcap（在Windows上）来抓取网络接口上的数据包。
- 协议解码：一旦抓取到数据包，Packetbeat会根据配置解析不同的协议，提取出相关的请求和响应信息。
- 数据发送：处理完的数据会被发送到指定的输出位置，通常是Elasticsearch，也可以是Logstash或者其他兼容的系统。


Packetbeat非常适合用于需要对网络流量进行深度分析的环境，例如企业内部网、云服务提供商、以及任何希望提升其应用性能和安全性的地方。结合Elastic Stack的其他组件（如Kibana），用户可以创建强大的可视化面板，以便更好地理解和管理他们的网络数据。早期的Packetbeat 支持Pf-ring，后来就不再支持了。为Packetbeat添加DPDK（Data Plane Development Kit）支持，可以显著提高其网络数据包处理能力，特别是对于高吞吐量和低延迟要求的场景。DPDK是一个优化了的数据包处理框架，它绕过了操作系统内核协议栈，直接在用户空间处理网络数据包，从而实现了高效的数据传输。



#### DPDK的安装 

 
 ```bash
 
 
 CentOS
#  yum install -y libpcap-devel gcc gcc-c++ make meson ninja  numactl-devel  numactl  net-tools pciutils
#  yum install -y kernel-devel-$(uname -r) kernel-headers-$(uname -r)

Debian + Ubuntu
# apt install -y libpcap-dev gcc g++ make meson ninja-build libnuma-dev numactl net-tools pciutils
# apt install -y linux-headers-$(uname -r)


#  wget http://fast.dpdk.org/rel/dpdk-20.11.10.tar.xz
#  tar -Jxvf dpdk-20.11.10.tar.xz
#  cd dpdk-stable-20.11.10 && meson build && cd build && ninja && ninja install
#  export LD_LIBRARY_PATH=/usr/local/lib64:$LD_LIBRARY_PATH
#  git clone git://dpdk.org/dpdk-kmods && cd  dpdk-kmods/linux/igb_uio
#  make
#  modprobe uio  &&  insmod igb_uio.ko
#  dpdk-devbind.py --status
#  # ifconfig ens38 down   ## 填写实际网卡
#  dpdk-devbind.py -b igb_uio 0000:03:00.0(pci-addr)  ## 根据实际填写

```