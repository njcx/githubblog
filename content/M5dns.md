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

第一步: 受控机向内部dns服务器发送一个查询NKNFjklKLuJNVIUM.ml.org的请求

第二步：内部dns服务器通过防火墙向根dns服务器发出查询请求

第三步：经过大量迭代后，DNS请求到达NKNFjklKLuJNVIUM.ml.org的权威DNS服务器（黑客所控制）

第四步：受控机请求查询的响应通过防火墙返回到内部DNS服务器

第五步：内部DNS服务器将响应结果返回给受控机


上面的流程展示了一个受控机在连接外部网络时dns解析的一个过程。由于防火墙并没有对dns协议做任何处理，所以我们可以通过这种方式来穿透防火墙。

这里很多人会有一个疑问，关于dns 请求查询NKNFjklKLuJNVIUMvKL.ml.org 是怎么到达黑客所控制的权威DNS服务器的？

请求一个域名，比如NKNFjklKLuJNVIUMvKL.ml.org ,本地DNS服务器上没有 NKNFjklKLuJNVIUMvKL.ml.org，那么它将向root，也就是根域名服务器请求，看看根知道不。root一看是.org的域名，就交 给.org域名服务器进行解析，.org的域名服务器一看是.ml.org那么就会去找.ml.org的域名服务器 (ns1.myhostadmin.net),看看它有没有这条记录，.ml.org的域名服务器上一看是.ml.org，如果它有这 条A记录，那么就会返回NKNFjklKLuJNVIUMvKL.ml.org 的记录。

但是，如果没有，你可以再在ml.org的域名服务器上设定一个NS 类型的记录，如：ml.org NS 111.222.333.444(通常这里不让设置为地址，你可以先在DNS服务器上添加一条A记录，如ns.ml.org A 111.222.333.444，再添加NS记录：ml.org NS ns.xxx.org)，这里指定一个公网服务器，就是黑客所控制的权威DNS服务器的