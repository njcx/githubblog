Title: Etcd在HIDS-Agent配置管理和健康监测上的应用 
Date: 2018-08-12 20:20
Modified: 2018-08-12 20:20
Category: 安全
Tags: HIDS
Slug: R11 
Authors: nJcx
Summary: Etcd在HIDS-Agent配置管理和健康监测上的应用 ~


#### 介绍

etcd是CoreOS团队于2013年6月发起的开源项目，它的目标是构建一个高可用的分布式键值(key-value)数据库。etcd内部采用raft协议作为一致性算法，etcd基于Go语言实现。

etcd作为服务发现系统，有以下的特点：

- 简单：安装配置简单，而且提供了HTTP API进行交互，使用也很简单
- 安全：支持SSL证书验证
- 快速：根据官方提供的benchmark数据，每个实例每秒1000+次写操作
- 可靠：采用raft算法，实现分布式系统数据的可用性和一致性

etcd项目地址：https://github.com/etcd-io/etcd

下载地址： https://github.com/etcd-io/etcd/releases/download/v3.4.14/etcd-v3.4.14-linux-amd64.tar.gz

etcd 是许多其他项目的核心组件。最值得注意的是，它是 Kubernetes 的首要数据存储，也是容器编排的实际标准系统。使用 etcd， 云原生应用可以保持更为一致的运行时间，而且在个别服务器发生故障时也能正常工作。应用从 etcd 读取数据并写入到其中；通过分散配置数据，为节点配置提供冗余和弹性。

#### Etcd应用场景

etcd比较多的应用场景是用于服务发现，服务发现(Service Discovery)要解决的是分布式系统中最常见的问题之一，即在同一个分布式集群中的进程或服务如何才能找到对方并建立连接。

从本质上说，服务发现就是要了解集群中是否有进程在监听upd或者tcp端口，并且通过名字就可以进行查找和链接。

要解决服务发现的问题，需要下面三大支柱，缺一不可。

一个强一致性、高可用的服务存储目录。
基于Ralf算法的etcd天生就是这样一个强一致性、高可用的服务存储目录。

一种注册服务和健康服务健康状况的机制。
用户可以在etcd中注册服务，并且对注册的服务配置key TTL，定时保持服务的心跳以达到监控健康状态的效果。

一种查找和连接服务的机制。
通过在etcd指定的主题下注册的服务业能在对应的主题下查找到。


#### Etcd vs Zookeeper

提供配置共享和服务发现的系统比较多，其中最为大家熟知的是 Zookeeper，而 etcd 可以算得上是后起之秀了。在项目实现、一致性协议易理解性、运维、安全等多个维度上，etcd 相比 zookeeper 都占据优势。

本文选取 Zookeeper 作为典型代表与 etcd 进行比较，而不考虑 Consul 项目作为比较对象，原因为 Consul 的可靠性和稳定性还需要时间来验证（项目发起方自身服务并未使用Consul，自己都不用)。

- 一致性协议： etcd 使用 Raft 协议，Zookeeper 使用 ZAB（类PAXOS协议），前者容易理解，方便工程实现；
- 运维方面：etcd 方便运维，Zookeeper 难以运维；
- 数据存储：etcd 多版本并发控制（MVCC）数据模型 ， 支持查询先前版本的键值对
- 项目活跃度：etcd 社区与开发活跃，Zookeeper 开发缓慢；
- API：etcd 提供 HTTP+JSON, gRPC 接口，跨平台跨语言，Zookeeper 需要使用其客户端；
访问安全方面：etcd 支持 HTTPS 访问，Zookeeper 在这方面缺失；



#### Etcd vs Redis

尽管etcd和redis都是键值存储，随着技术的演进，二者在功能上也有逐渐相似的趋势，但二者在许多方面都有很大区别。
etcd的爆火来源于k8s用etcd做服务发现，而redis的兴起则来源于memcache缓存本身的局限性。
etcd的重点是利用raft算法做分布式一致性，强调各个节点之间的通信、同步，确保各节点数据和事务的一致性，使得服务发现工作更稳定；

redis也可以做主从同步和读写分离，但节点一致性强调的是数据，不是事务。redis的注册和发现只能通过pub和sub实现，安全性不能保证（断线重连之后不会将历史信息推送给客户端，需要自己做一个定时轮询），延时也比etcd v3高。

etcd v3的底层采用boltdb做存储，value直接持久化；redis是一个内存数据库，它的持久化方案有aof和rdb，在宕机时都或多或少会丢失数据。
