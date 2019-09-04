Title: NIDS 中的 ICMP隐蔽隧道检测
Date: 2018-07-07 20:20
Modified: 2018-07-07 20:20
Category: 安全
Tags: nids
Slug: M4
Authors: nJcx
Summary:  NIDS 中的 ICMP隐蔽隧道检测 ~


#### 介绍

![icmp](../images/tcpip.gif)

我们先介绍一下 ICMP协议，ICMP的内容是放在ip数据包的数据部分里传输的，ICMP是基于IP协议工作的，我们要区别于传输层，它仍然属于网络层协议。ICMP报文包含在IP数据报中，IP报头在ICMP报文的最前面。一个ICMP报文包括IP报头（至少20字节）、ICMP报头（至少八字节）和ICMP报文（属于ICMP报文的数据部分）。当IP报头中的协议字段值为1时，就说明这是一个ICMP报文。ICMP报头如下图所示。 
如下图：

![icmp](../images/icmp.png)

![icmp](../images/icmpfield.png)


从上图看，也就是说，我们重点关注 Checksum 字段和Data字段，因为我们改变Data字段的时候，Checksum也要改变,我们把我们的payload或者数据放到Data字段里面即可.

如图，我们用wireshark抓的包

![icmp](../images/wiresharkicmp.jpeg)


#### 安装

我们测试一下，Linux 的icmp 的隐藏后门[ish](https://sourceforge.net/projects/icmpshell/files/ish/)，如果是Windows，推荐 [icmpsh](https://github.com/inquisb/icmpsh)， 

受控机CentOS7 ：172.19.25.53

控制机Parrot Linux ：172.19.25.73

我们在受控机上编译（make linux），启动 ishd，在控制机上启动 ./ish 172.19.25.53

![icmp](../images/ish.jpeg)

我们可以在 Data 里面可以看到一个ls

![icmp](../images/ishwireshark.jpeg)

我们可以在响应里面发现 相关目录的数据

![icmp](../images/wireshark1.jpeg)


可以看出，payload 是放在Data字段的

我们总结一下ICMP隐蔽隧道的特征：

1、ICMP隧道短时间会产生大量 ICMP 数据包，用来数据发送，可能存在大于 64 比特的数据包。

2、ICMP隧道发送的 ICMP 数据包前后Data字段不一样，而且响应数据包中 payload 跟请求数据包不一致。

3、ICMP 数据包的协议标签可能存在特殊字段。例如，icmptunnel 会在所有的 ICMP Data 前面增加 ‘TUNL’ 标记以用于识别隧道

4，Data 里面可能存在一些系统命令


防御和检测手段：

1，禁止 ping（不太可能），会影响到很多运维和安全检测设备的运行。

2，
