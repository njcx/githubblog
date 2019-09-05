Title: NIDS 中的 DNS隐蔽隧道检测
Date: 2018-07-08 20:20
Modified: 2018-07-08 20:20
Category: 安全
Tags: nids
Slug: M5
Authors: nJcx
Summary: NIDS 中的 DNS隐蔽隧道检测~


#### 介绍

![icmp](../images/tcpip.gif)

我们先简单介绍一下 DNS协议，DNS协议是一个应用层协议，用来将域名转换为IP地址（也可以将IP地址转换为相应的域名地址），类似一个分布式数据库，数据通过udp传输,IP报头中的协议字段值为17.

DNS协议报文格式

![dns](../images/dns-protocol-format.png)

通过wireshark 抓到的包：

![dns](../images/dnswireshark.png)

由于关于dns报文介绍太长，参考下面url 

[DNS协议详解及报文格式分析](https://www.cnblogs.com/davidwang456/articles/10660051.html)


#### 安装

![dns](../images/dnsq.jpeg)

![dns](../images/dnstun.jpeg)