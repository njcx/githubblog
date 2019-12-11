Title: CentOS7 DPDK18 安装
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
#  cd /opt/dpdk-18.11/usertools
# ./dpdk-setup.sh

这里我们选择 
[15] x86_64-native-linuxapp-gcc

这里可能会报错，make: *** /lib/modules/3.10.0-1062.4.1.el7.x86_64/build: 没有那个文件或目录。 停止。

# ln -s /usr/src/kernels/3.10.0-1062.9.1.el7.x86_64/  /lib/modules/3.10.0-1062.4.1.el7.x86_64/build 

即可


[18] Insert IGB UIO module

[22] Setup hugepage mappings for NUMA

[24] Bind Ethernet/Crypto device to IGB UIO module

```


```bash

# modprobe uio
# insmod igb_uio.ko
# lsmod | grep uio

# ifconfig ens38 down
# cd usertools/
# ./dpdk-devbind.py --bind=igb_uio ens38


```

```bash

[22] Setup hugepage mappings for NUMA

我这里设置的 1024

```

```bash

# export  RTE_SDK=/opt/dpdk-18.11/
# export  RTE_TARGET=x86_64-native-linuxapp-gcc

```


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