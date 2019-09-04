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

![icmp](../images/wiresharkicmp.jpeg)


从上图看，也就是说，我们重点关注 Checksum 字段和Data字段，因为我们改变Data字段的时候，Checksum也要改变,我们把我们的payload或者数据放到Data字段里面即可.

![icmp](../images/icmpfield.png)

#### 安装

![icmp](../images/ish.jpeg)

![icmp](../images/ishwireshark.jpeg)

![icmp](../images/wireshark1.jpeg)


[icmpsh](https://github.com/inquisb/icmpsh)

[ish](https://sourceforge.net/projects/icmpshell/files/ish/)