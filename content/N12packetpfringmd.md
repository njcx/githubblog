Title: 高版本Packetbeat借Pcap兼容PF_RING
Date: 2018-07-16 01:20
Modified: 2018-07-16 01:20
Category: 安全
Tags: PF_RING
Slug: N12
Authors: nJcx
Summary: 高版本Packetbeat借Pcap兼容PF_RING~

#### 安装


```bash
 git clone https://github.com/ntop/PF_RING.git 
 cd PF_RING-7.4.0-stable/
 yum install numactl-devel libnuma-dev
 UNAME=$(uname -r)
 yum install gcc kernel-devel-${UNAME%.*}
 make
 make install
 cd /lib/modules/`uname -r`/kernel/net/pf_ring
 insmod pf_ring.ko min_num_slots=8192 quick_mode=1
 cd  /lib/modules/`uname -r`/kernel/drivers/net/ethernet/intel/igb
 xz -d igb.ko.xz 
 rmmod igb ; insmod igb.ko 
 ethtool -i eno5
 dmesg | grep Ethernet
 cat /proc/net/pf_ring/infocat /proc/net/pf_ring/info
```


到这里PF_RING模块，以及网卡驱动已经安装好了


然后 

```bash
# yum remove libpcap  libpcap-devel 
# cd PF_RING-7.4.0-stable/userland/libpcap
# make install

```


安装高版本Packetbeat，

```bash

packetbeat.interfaces.type: pcap

```
即可