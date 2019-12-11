Title: CentOS7下DPDK18 安装
Date: 2018-07-23 20:20
Modified: 2018-07-23 20:20
Category: 安全
Tags: DPDK
Slug: N9
Authors: nJcx
Summary:  CentOS7下 DPDK18 安装~

#### 安装


```bash

#  yum install numactl-devel  numactl  net-tools pciutils kernel-devel 
#  wget http://fast.dpdk.org/rel/dpdk-18.11.tar.xz
#  tar xvJf  dpdk-18.11.tar.xz 

```

下面这一步，很重要，可以避免很多错误

```bash
# export  RTE_SDK=/opt/dpdk-18.11/
# export  RTE_TARGET=x86_64-native-linuxapp-gcc

```

```bash

#  cd /opt/dpdk-18.11/usertools
# ./dpdk-setup.sh

这里我们选择 
[15] x86_64-native-linuxapp-gcc

这里可能会报错，make: *** /lib/modules/3.10.0-1062.4.1.el7.x86_64/build: 没有那个文件或目录。 停止。

# ln -s /usr/src/kernels/3.10.0-1062.9.1.el7.x86_64/  /lib/modules/3.10.0-1062.4.1.el7.x86_64/build 

即可


[18] Insert IGB UIO module

Loading DPDK UIO module

[22] Setup hugepage mappings for NUMA

我这里设置的 1024

[24] Bind Ethernet/Crypto device to IGB UIO module

# ifconfig ens38 down   这里要把网卡停用，不然会安装失败

Network devices using DPDK-compatible driver
============================================
0000:02:06.0 '82545EM Gigabit Ethernet Controller (Copper) 100f' drv=igb_uio unused=e1000

Network devices using kernel driver
===================================
0000:02:01.0 '82545EM Gigabit Ethernet Controller (Copper) 100f' if=ens33 drv=e1000 unused=igb_uio *Active*
0000:02:05.0 '82545EM Gigabit Ethernet Controller (Copper) 100f' if=ens37 drv=e1000 unused=igb_uio *Active*

No 'Crypto' devices detected
============================

No 'Eventdev' devices detected
==============================

No 'Mempool' devices detected
=============================

No 'Compress' devices detected
==============================


```


手动绑定（备选）

```bash
# cd /opt/dpdk-18.11/x86_64-native-linuxapp-gcc/kmod
# modprobe uio
# insmod igb_uio.ko
# lsmod | grep uio

# ifconfig ens38 down
# cd /opt/dpdk-18.11/usertools/
# ./dpdk-devbind.py --bind=igb_uio ens38

[22] Setup hugepage mappings for NUMA

填写 1024

```



#### 测试


```bash
 #cd dpdk-18.11/examples/helloworld
 # make
 #./build/helloworld
 
 
 
EAL: Detected 1 lcore(s)
EAL: Detected 1 NUMA nodes
EAL: Multi-process socket /var/run/dpdk/rte/mp_socket
EAL: No free hugepages reported in hugepages-1048576kB
EAL: Probing VFIO support...
EAL: PCI device 0000:02:01.0 on NUMA socket -1
EAL:   Invalid NUMA socket, default to 0
EAL:   probe driver: 8086:100f net_e1000_em
EAL: PCI device 0000:02:05.0 on NUMA socket -1
EAL:   Invalid NUMA socket, default to 0
EAL:   probe driver: 8086:100f net_e1000_em
EAL: PCI device 0000:02:06.0 on NUMA socket -1
EAL:   Invalid NUMA socket, default to 0
EAL:   probe driver: 8086:100f net_e1000_em
hello from core 0
 
```


安装到这里，就结束了