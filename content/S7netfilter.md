Title: Linux环境微隔离之Netfilter
Date: 2018-08-22 20:20
Modified: 2018-08-22 20:20
Category: 安全
Tags: 微隔离
Slug: S7
Authors: nJcx
Summary: Linux环境微隔离之Netfilter ~



#### 介绍

   Linux 内核从1.1版本开始，就已经具备包过滤功能。在2.0内核中，开始采用Ipfwadm(Alan Cox)来操作内核的包过滤规则,其代码主要来自Freebsd。到2.2版本时，Linux内核采用了 Ipchains来控制内核的包过滤规则。发展到2.4.x时，Ipchains被一个全新的包过滤管理工具Iptables所替代。新发布的2.6版内核也在安全方面进行了改进。

Linux提供的防火墙软件包内置于Linux内核中，是一种基于包过滤型的防火墙实现技术。其中心思想是根据网络层IP包头中的源地址、目的地址及包类型等信息来控制包的流向。更彻底的过滤则是检查包中的源端口、目的端口以及连接状态等信息。 Netfilter是Linux核心中一个通用架构，用于扩展各种服务的结构化底层服务。


Netfilter/iptables 项目由 Rusty Russe 创建于1998年，并于 1999 年建立了 Netfilter Core team，并在此后负责维护此项目，同时也于2000年3月合并进了 linux 2.3.x 版本的 linux 内核。Netfilter/iptables 有三部分组成，分别是Netfilter 框架/Iptables(内核空间)/Iptables 命令行工具(用户空间)。

Netfilter 是一个由Linux 内核提供的框架，可以进行多种网络相关的自定义操作。它提供一系列的表（tables），每个表由若干链（chains）组成，而每条链中可以由一条或数条规则（rule）组成。它可以和其它模块（如iptables模块和nat模块）结合起来实现包过滤功能。Iptables是一个管理内核包过滤的工具，可以加入、插入或删除核心包过滤表格中的规则。实际上真正来执行这些过滤规则的是Netfilter 。


Netfilter 在 Linux 内核中表现为一系列的hook, 并允许Linux 内核模块注册为回调函数，Linux内核模块通过回调函数操作网络报文。一共有5个钩子，如下

```bash

--->[NF_IP_PRE_ROUTING]--->[ROUTE]--->[NF_IP_FORWARD]--->[NF_IP_POST_ROUTING]--->
                              |                        ^
                              |                        |
                              |                     [ROUTE]
                              v                        |
                       [NF_IP_LOCAL_IN]        [NF_IP_LOCAL_OUT]
                              |                        ^
                              |                        |
                              v                        |

```


Netfilter Hook的意义:

	NF_IP_PRE_ROUTING: 位于路由之前，报文一致性检查之后（报文一致性检查包括: 报文版本、报文长度和checksum）。
	NF_IP_LOCAL_IN: 位于报文经过路由之后，并且目的是本机的。
	NF_IP_FORWARD：位于在报文路由之后，目的地非本机的。
	NF_IP_LOCAL_OUT: 由本机发出去的报文，并且在路由之前。
	NF_IP_POST_ROUTING: 所有即将离开本机的报文。
	
Linux 内核模块可以注册到任何的hook，注册的回调函数也必需指定优先级。当一个报文通过hook的时候，hook将会依据优先级调用回调函数。注册的回调函数，可以有五种返回，每种返回代表对报文不同的操作:

	NF_ACCEPT: 继续正常处理此报文，即允许报文通过。
	NF_DROP: 丢弃此报文，不再进行继续处理，即拒绝此报文。
	NF_STOLEN: 取走这个报文，不再继续处理。
	NF_QUEUE: 报文进行重新排队，可以将报文发到用户空间的程序，进行修改或者决定是拒绝或者允许。
	NF_REPEAT: 报文重新调用hook。


Iptables 是基于Netfilter框架实现的报文选择系统，其可以用于报文的过滤、网络地址转换和报文修改等功能。Iptables 本质上是包含了5个规则表，而规则表则包含了一些列的报文的匹配规则以及操作目标。以下对每个规则表进行了简单说明：

	Filter Table: 是一个默认的规则表，用于报文的过滤。他注册了三个链: INPUT、FORWARD和OUTPUT。
	NAT Table: 主要用于NAT转换，注册了四个链：PREROUTING、INPUT、OUTPUT和POSTROUTING。
	Mangle Table: 主要用于报文的修改，一共注册了五个链: PREROUTING、OUTPUT、INPUT、FORWARD和POSTROUTING
	Raw Table: 可以对报文不进行链路跟踪，其优先级在hook中注册很高，注册了两个链: PREROUTING和OUTPUT
	Security Table: 用于强制网络接入控制，注册了三个链：INPUT、OUTPUT 和 FORWARD
	操作目标指的是否允许报文通过，如果允许即为ACCEPT，拒绝则为DROP。
