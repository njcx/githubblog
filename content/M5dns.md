Title: nids 中的 dns 隐蔽隧道检测
Date: 2018-07-08 20:20
Modified: 2018-07-08 20:20
Category: 安全
Tags: nids
Slug: M5
Authors: nJcx
Summary: nids 中的 dns 隐蔽隧道检测~


#### 介绍

![icmp](../images/tcpip.gif)
我们先简单介绍一下 DNS协议，DNS协议是一个应用层协议，用来将域名转换为IP地址（也可以将IP地址转换为相应的域名地址），类似一个分布式数据库，数据通过udp传输,IP报头中的协议字段值为17.

DNS协议报文格式
#### 安装

