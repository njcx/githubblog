Title: 安装 Bro-2.5.5和PF_RING
Date: 2018-06-05 10:20
Modified: 2018-06-05 10:20
Category: bro
Tags: bro
Slug: H11
Authors: nJcx
Summary: bro 的安装和配置

#### 安装

网卡类型：
查看机器的网卡类型：
ethtool -i eth0
删除以前的网卡驱动：
rmmod e1000e 

```bash
> > wget https://www.bro.org/downloads/bro-2.5.5.tar.gz
> > tar -zxvf bro-2.5.5.tar.gz
> > yum install cmake make gcc gcc-c++ flex bison libpcap-devel openssl-devel python-devel swig zlib-devel -y
> > 
> > yum install "kernel-devel-uname-r == $(uname -r)" -y
> > git clone https://github.com/ntop/PF_RING.git
> > cd PF_RING/kernel
> > make
> > sudo make install
> > insmod pf_ring.ko transparent_mode=1
> > 
> > cd ../../ drivers/intel/e1000e/e1000e-xxx/src
> > make
> > make install 
> > insmod e1000e.ko #将驱动文件copy到内核

安装网卡驱动：
1.进入到目录lib/modules/<centos-kernel-version>/kernel/drivers/net下
2.加载驱动modprobe e1000e
安装完毕，使用dmesg命令查看驱动是否安装成功
ip addr 查看网卡

> > 
> > cd ../userland/lib
> > ./configure --prefix=/opt/pfring
> > sudo make install
> > 
> > cd ../libpcap
> > ./configure --prefix=/opt/pfring
> > sudo make install
> > 
> > cd ../tcpdump
> > ./configure --prefix=/opt/pfring
> > sudo make install
> > 
> > cd bro-2.5.5
> > ./configure --prefix=/opt/bro --with-pcap=/opt/pfring
> > make
> > sudo make install
> > 
> > cd aux/plugins/pf_ring/
> > ./configure --bro-dist=../../.. --with-pfring=/opt/pfring --install-root=/opt/bro/lib/bro/plugins
> > make && make install
> > 
> > echo "/opt/pfring/lib" >> /etc/ld.so.conf
> > ldconfig
```


#### 验证


```bash

./bro -N Bro::PF_RING

```

打印如下，代表安装正常

```bash

Bro::PF_RING - Packet acquisition via PF_RING (dynamic, version 1.0)

```

#### 使用

```bash

[bro]
type=standalone
host=localhost
interface=pf_ring::ens33

```

在网卡前面加个 pf_ring::, 即可使用

```bash

#./broctl

Welcome to BroControl 1.7

Type "help" for help.

[BroControl] > install

[BroControl] > start

```