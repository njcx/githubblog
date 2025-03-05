Title: 用ebpf的xdp 快速丢包，避免too late
Date: 2022-08-29 20:20
Modified: 2022-08-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T3
Authors: nJcx
Summary: 用ebpf的xdp 快速丢包，避免too late ~


#### 介绍

eBPF（Extended Berkeley Packet Filter）最初设计用于高效网络包过滤，现在已扩展到操作系统和用户空间应用程序之间的多种交互场景。它允许在操作系统内核中安全地执行沙盒程序，而无需更改内核源代码或加载自定义内核模块。XDP（Express Data Path）是eBPF的一个子系统，专注于网络数据包的快速处理。

XDP通过在网络设备驱动层面上提供一个早期处理点来加速数据包的处理过程。这意味着数据包在到达更高级别的网络堆栈之前就能被处理，从而能够实现极低延迟的数据包过滤和转发。XDP程序使用eBPF编写，并直接附加到网络接口上。由于XDP工作在网络驱动层，因此能够在不影响系统其余部分的情况下以最高速度处理数据包。尽管性能极高，但XDP依旧保留了eBPF的灵活性，使得开发者可以根据需要定制数据包处理逻辑。

当网络接口接收到一个数据包时，XDP程序会首先处理这个数据包。XDP程序可以决定对这个数据包执行什么操作，如丢弃、通过或修改数据包。



#### XDP 和 Netfilter对比

XDP（eXpress Data Path）和Netfilter都是Linux内核中用于网络数据包处理的框架，但它们在设计理念、性能、使用场景等方面存在显著差异。以下是对两者的对比：

-  处理阶段
XDP：XDP是在网络数据包到达网卡驱动层之后、进入更高级别的TCP/IP协议栈之前进行处理的。这意味着它能够以最小的延迟处理数据包。
Netfilter：Netfilter则是在网络堆栈的不同层次上设置了多个钩子点（如PREROUTING、INPUT、FORWARD、OUTPUT、POSTROUTING），允许在这些点上对数据包进行过滤、修改等操作。
-  性能
XDP：由于其处理发生在网络数据包进入系统后尽可能早的阶段，并且可以绕过不必要的协议栈处理，因此具有更高的性能和更低的延迟。特别是在需要快速决策（例如丢弃恶意流量）的情况下，XDP表现尤为出色。
Netfilter：虽然Netfilter也支持高效的数据包处理，但由于它位于协议栈内部，因此相比XDP可能会引入更多的延迟。
-  可编程性与灵活性
XDP：通过使用eBPF（Extended Berkeley Packet Filter），XDP提供了高度可编程的能力，允许开发者编写复杂的逻辑来处理数据包。同时，由于是运行于沙盒环境中的字节码，保证了安全性。
Netfilter：主要通过iptables命令行工具或nftables来进行配置，对于简单的规则集非常直观，但对于复杂逻辑可能不如XDP灵活。

总结来说，如果应用需要极高的性能和低延迟，则XDP可能是更好的选择， 选用Netfilter则可能 Too late。
