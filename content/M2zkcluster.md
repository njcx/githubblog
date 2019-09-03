Title: zookeeper 集群搭建实践笔记
Date: 2018-07-04 20:20
Modified: 2018-07-04 20:20
Category: Big data
Tags: kafka
Slug: M2
Authors: nJcx
Summary: zookeeper 集群搭建实践笔记 ~
Status: draft

#### 介绍

zk 集群数量一般为2*n+1比较好，因为zk的工作节点是超过半数才能对外提供服务，三台中超过两台超过半数，允许一台挂掉。最好不要使用偶数台。例如：如果有4台，那么挂掉一台还剩下三台，如果再挂掉一台就不能行了，因为是要超过半数。

#### 安装

我们使用了如下环境，CentOS7 X64 

```bash

172.16.202.144    zk1
172.16.202.143    zk2
172.16.202.145    zk3


```


```bash

# yum install -y wget java-1.8.0-openjdk  java-1.8.0-openjdk-devel 
# cd /opt && wget https://archive.apache.org/dist/zookeeper/zookeeper-3.4.12/zookeeper-3.4.12.tar.gz
# tar -zxvf zookeeper-3.4.12.tar.gz

```
```bash

// 复制zoo.cfg文件
cp zoo_sample.cfg zoo.cfg
// 打开zoo.cfg文件，然后按后面的配置信息进行配置
vim zoo.zfg

```

```bash
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/opt/zookeeper-3.4.12/zkdata
dataLogDir=/opt/zookeeper-3.4.12/zklog
clientPort=2181
server.1=172.16.202.144:12888:13888
server.2=172.16.202.143:12888:13888
server.3=172.16.202.145:12888:13888
```
填入这三个地址。第一个端口是master和slave之间的通信端口，默认是2888，第二个端口是leader选举的端口，集群刚启动的时候选举或者leader挂掉之后进行新的选举的端口默认是3888.然后

```bash
scp zoo.cfg root@172.16.202.143：/opt/zookeeper-3.4.12/conf
scp zoo.cfg root@172.16.202.145：/opt/zookeeper-3.4.12/conf
```

同样在 另外两个机器下面，zk目录下面创建 zkdata 和 zklog目录，这里的myid代表机器编号，不相同就OK，然后

```bash

echo "1" > /opt/zookeeper-3.4.12/zkdata/myid  // zk1
echo "2" > /opt/zookeeper-3.4.12/zkdata/myid  // zk2
echo "3" > /opt/zookeeper-3.4.12/zkdata/myid  // zk3

```


然后，把3台vps 的防火墙都关了（生产环境请开策略）

```bash

systemctl stop  firewalld && ystemctl disable  firewalld   // zk1
systemctl stop  firewalld && ystemctl disable  firewalld   // zk2
systemctl stop  firewalld && ystemctl disable  firewalld   // zk3

```


然后。在3台vps上都启动


```bash
[root@zk1 bin]# ./zkServer.sh start

[root@zk1 bin]# ./zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/zookeeper-3.4.12/bin/../conf/zoo.cfg
Mode: follower


[root@zk2 bin]# ./zkServer.sh start
[root@zk2 bin]# ./zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /opt/zookeeper-3.4.12/bin/../conf/zoo.cfg
Mode: leader

```


