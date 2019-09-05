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

关于DNS请求的方式如图，
具体可描述如下： 
1. 主机先向本地域名服务器进行递归查询 
2. 本地域名服务器采用迭代查询，向一个根域名服务器进行查询 
3. 根域名服务器告诉本地域名服务器，下一次应该查询的顶级域名服务器的IP地址 
4. 本地域名服务器向顶级域名服务器进行查询 
5. 顶级域名服务器告诉本地域名服务器，下一步查询权限服务器的IP地址 
6. 本地域名服务器向权威服务器进行查询 
7. 权限服务器告诉本地域名服务器所查询的主机的IP地址 
8. 本地域名服务器最后把查询结果告诉主机 

![dns](../images/dnstun.jpeg)

如果在企业内网，那么黑客的攻击机器，就是所谓的权威服务器