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



gopacket 是一个用于Go语言的库，它提供了对网络数据包的低层次访问。基于著名的C库 libpcap ，gopacket 利用了Go语言的特性，如并发性、垃圾回收和类型安全性，使得处理网络数据包更加高效和易于使用。gopacket 常被用于网络安全分析、网络监控、性能分析等领域。例如，开发人员可以使用它来创建网络入侵检测系统（NIDS）、实时网络流量分析工具等。

主要功能

- 数据包捕获：可以用来监听并捕获流经指定网络接口的数据包。
- 数据包解码：支持多种协议（如以太网、IPv4、IPv6、TCP、UDP等）的数据包自动解码。



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
#  ifconfig ens38 down   ## 填写实际网卡
#  dpdk-devbind.py -b igb_uio 0000:03:00.0(pci-addr)  ## 根据实际填写

```



#### 开绑

gopacket 绑定 DPDK， 必然会遇到一个问题，就是Go调用C的问题，Go语言中调用C代码主要通过cgo工具实现。cgo允许Go代码与C代码进行互操作，这包括直接调用C函数、使用C的数据类型以及嵌入C代码片段等。

```bash
// hello.go
package main

//#include <stdio.h>
import "C"

func main() {
    C.puts(C.CString("Hello, this is a CGO demo.\n"))
}

```


Go的int类型对应于C的int类型。但需要注意的是，Go中的int大小是平台相关的（32位或64位），而C的int通常是32位。如果需要明确指定大小，可以使用固定宽度的类型如int32或int64来匹配C的int32_t或int64_t。Go的float64可以直接转换为C的double，float32转换为C的float。

```bash
var y float64 = 3.14
C.some_function(C.double(y))

```

Go的字符串需要通过C.CString()函数转换为C风格的字符串(char*)，并且记得用C.free()释放由C.CString()分配的内存。

```bash

str := "Hello, C!"
cstr := C.CString(str)
defer C.free(unsafe.Pointer(cstr))
C.some_function(cstr)

```

使用unsafe.Pointer可以在Go指针和C指针之间进行转换。例如，将一个Go切片传递给C函数时，可以通过(*C.type)(unsafe.Pointer(&slice[0]))这样的方式转换。

```bash
slice := []int{1, 2, 3}
C.some_function((*C.int)(unsafe.Pointer(&slice[0])), C.int(len(slice)))

```


#### DPDK 的初始化




#### Demo


```bash

package main

import (
	"fmt"
	"github.com/njcx/gopacket_dpdk"
	"github.com/njcx/gopacket_dpdk/dpdk"
	"github.com/njcx/gopacket_dpdk/layers"
	"log"
	"os"
)

func processPacket(data []byte) {
	packet := gopacket_dpdk.NewPacket(data, layers.LayerTypeEthernet, gopacket_dpdk.Default)
	ethernetLayer := packet.Layer(layers.LayerTypeEthernet)
	if ethernetLayer != nil {
		eth, _ := ethernetLayer.(*layers.Ethernet)
		fmt.Printf("Source MAC: %s, Destination MAC: %s\n", eth.SrcMAC, eth.DstMAC)
	}
	// Parse IP layer
	ipLayer := packet.Layer(layers.LayerTypeIPv4)
	if ipLayer != nil {
		ip, ok := ipLayer.(*layers.IPv4)
		if !ok {
			fmt.Println("Failed to parse IPv4 layer")
			return
		}
		fmt.Printf("Source IP: %s, Destination IP: %s\n", ip.SrcIP, ip.DstIP)
	}

	var resultDataList []map[string]string
	// 解析DNS层
	dnsLayer := packet.Layer(layers.LayerTypeDNS)
	if dnsLayer != nil {
		dns, ok := dnsLayer.(*layers.DNS)
		if !ok {
			fmt.Println("Failed to parse DNS layer")
			return
		}
		if !dns.QR {
			for _, dnsQuestion := range dns.Questions {
				if len(dns.Questions) == 0 {
					continue
				}
				resultdata := make(map[string]string)
				resultdata["source"] = "dns"
				resultdata["domain"] = string(dnsQuestion.Name)
				resultdata["type"] = string(dnsQuestion.Type)
				resultdata["class"] = string(dnsQuestion.Class)
				resultDataList = append(resultDataList, resultdata)
			}
			for _, data := range resultDataList {
				fmt.Printf("%+v\n", data)
			}
		}
	}
}

func main() {
	// Initialize DPDK
	if os.Geteuid() != 0 {
		log.Fatal("Root permission is required to execute")
	}

	args := []string{
		"dpdk_app_dns",
		"-l", "0-3",
		"-n", "4",
		"--proc-type=auto",
		"--file-prefix=dpdk_dns_",
		"--huge-dir", "/dev/hugepages",
	}

	if err := dpdk.InitDPDK(args); err != nil {
		log.Fatalf("Failed to initialize DPDK: %v", err)
	}
	handle, err := dpdk.NewDPDKHandle(0)

	handle.SetBPFFilter("udp and port 53")
	if err != nil {
		log.Fatalf("Failed to create DPDK handler: %v", err)
	}
	defer handle.Close()
	// Start receiving and processing packets
	handle.ReceivePacketsCallBack(processPacket)
}

```

代码在这里  https://github.com/njcx/gopacket_dpdk 。

