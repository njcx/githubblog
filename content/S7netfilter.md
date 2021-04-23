Title: Linux环境微隔离之Netfilter
Date: 2018-08-22 20:20
Modified: 2018-08-22 20:20
Category: 安全
Tags: 微隔离
Slug: S7
Authors: nJcx
Summary: Linux环境微隔离之Netfilter ~



#### 介绍

   Linux 内核从1.1版本开始，就已经具备包过滤功能。在2.0内核中，开始采用Ipfwadm来操作内核的包过滤规则。到2.2版本时，Linux内核采用了 Ipchains来控制内核的包过滤规则。发展到2.4.x时，Ipchains被一个全新的包过滤管理工具Iptables所替代。新发布的2.6版内核也在安全方面进行了改进。

Linux提供的防火墙软件包内置于Linux内核中，是一种基于包过滤型的防火墙实现技术。其中心思想是根据网络层IP包头中的源地址、目的地址及包类型等信息来控制包的流向。更彻底的过滤则是检查包中的源端口、目的端口以及连接状态等信息。 Netfilter是Linux核心中一个通用架构，用于扩展各种服务的结构化底层服务。


Netfilter/iptables 项目由 Rusty Russe 创建于1998年，并于 1999 年建立了 Netfilter Core team，并在此后负责维护此项目，同时也于2000年3月合并进了 linux 2.3.x 版本的 linux 内核。Netfilter/iptables 有三部分组成，分别是Netfilter 框架/Iptables(内核空间)/Iptables 命令行工具(用户空间)。

Netfilter 是一个由Linux 内核提供的框架，可以进行多种网络相关的自定义操作。它提供一系列的表（tables），每个表由若干链（chains）组成，而每条链中可以由一条或数条规则（rule）组成。它可以和其它模块（如iptables模块和nat模块）结合起来实现包过滤功能。Iptables是一个管理内核包过滤的工具，可以加入、插入或删除核心包过滤表格中的规则。实际上真正来执行这些过滤规则的是Netfilter 。
