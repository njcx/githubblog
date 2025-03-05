Title: 用ebpf的xdp 快速丢包，避免too late
Date: 2022-08-29 20:20
Modified: 2022-08-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T3
Authors: nJcx
Summary: 用ebpf的xdp 快速丢包，避免too late ~


#### 介绍

eBPF（extended Berkeley Packet Filter）是一种革命性的技术，它允许程序在操作系统内核的安全沙箱环境中运行，而无需更改内核源代码或加载内核模块。XDP（Express Data Path）是eBPF的一个子系统，专注于网络数据包的快速处理。

XDP通过在网络设备驱动层面上提供一个早期处理点来加速数据包的处理过程。这意味着数据包在到达更高级别的网络堆栈之前就能被处理，从而能够实现极低延迟的数据包过滤和转发。XDP程序使用eBPF编写，并直接附加到网络接口上。由于XDP工作在网络驱动层，因此能够在不影响系统其余部分的情况下以最高速度处理数据包。尽管性能极高，但XDP依旧保留了eBPF的灵活性，使得开发者可以根据需要定制数据包处理逻辑。

