Title: 把gopacket 和 dpdk 绑定一起
Date: 2023-07-29 20:20
Modified: 2023-07-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T4
Authors: nJcx
Summary: 把gopacket 和 dpdk 绑定一起 ~


#### 介绍



DPDK（Data Plane Development Kit）是一个开源的软件项目，旨在提供快速的数据包处理能力，特别适用于高性能网络应用。它最初由英特尔公司开发，并于2010年首次发布。DPDK通过优化Linux环境下数据包的接收和发送过程，显著提高了网络性能，降低了延迟。虽然x86架构在通用计算方面表现出色，但在面对高性能网络应用中的高吞吐量和低延迟要求时，传统的基于内核的数据包处理方法暴露出了一些不足。

传统x86架构在网络高吞吐场景下的痛点

- 上下文切换开销：在传统的网络数据包处理中，每当有数据包到达时，操作系统会通过中断机制通知应用程序，这会导致频繁的上下文切换。这种机制虽然适用于一般的网络流量，但在高吞吐量情况下，大量的中断请求会导致显著的性能开销。
- 内存访问效率低：传统方式下，数据包通常需要经过多次内存拷贝，从网卡到内核空间再到用户空间。这些额外的拷贝操作不仅增加了延迟，也降低了整体的吞吐量。
- 缓存未充分利用：由于数据包处理过程中涉及大量小块数据的读写操作，导致CPU缓存命中率低，影响了处理效率。
- NUMA架构限制：现代多处理器系统通常采用非统一内存访问（NUMA）架构。如果数据包处理逻辑没有针对NUMA进行优化，可能会导致跨节点内存访问，进一步降低性能。


DPDK的设计初衷正是为了解决x86架构在处理网络高吞吐量任务时遇到的瓶颈问题，通过一系列技术创新，显著提升了x86平台在网络数据包处理方面的性能，使其更适合于对吞吐量和延迟有严格要求的应用场景。

核心特性

- 用户空间驱动：传统的网络数据包处理通常发生在内核空间，而DPDK将这一过程搬移到了用户空间，减少了上下文切换的开销。
- 轮询模式驱动：不同于中断驱动的方式，DPDK采用轮询机制直接从网卡读取数据包，这种方式能够更高效地利用CPU资源。
- 零拷贝：在数据传输过程中避免不必要的内存复制操作，进一步提升效率。
- NUMA感知：充分考虑现代多处理器系统的非统一内存访问架构（NUMA），以提高多处理器环境下的性能表现。



DPDK被广泛应用于需要高吞吐量、低延迟的网络环境中，通过使用DPDK，开发者可以构建出比传统方法更快、更高效的网络应用程序，这对于满足日益增长的数据流量需求至关重要。


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