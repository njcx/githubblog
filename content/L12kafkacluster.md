Title: kafka 集群搭建实践笔记
Date: 2018-07-04 19:20
Modified: 2018-07-04 19:20
Category: Big data
Tags: kafka
Slug: L12
Authors: nJcx
Summary: 记录一下kafka 集群搭建 ~
Status: draft

#### 安装
实验环境： vmware fusion 

- 先做一个CentOS 7.3 x64 的模板


```bash

#cd /opt

# yum install wget java-1.8.0-openjdk  java-1.8.0-openjdk-devel -y
# wget  https://downloads.lightbend.com/scala/2.12.8/scala-2.12.8.tgz
# wget  http://mirrors.hust.edu.cn/apache/kafka/2.1.0/kafka_2.12-2.1.0.tgz
# tar -zxvf kafka_2.12-2.1.0.tgz && tar -zxvf scala-2.12.8.tgz
# rm -rf kafka_2.12-2.1.0.tgz  scala-2.12.8.tgz

```
然后，添加scala的环境变量

```bash
vim /etc/profile
```

填入

```bash
export SCALA_HOME=/opt/scala-2.12.8
export PATH=$PATH:$SCALA_HOME/bin
```

```bash
source  /etc/profile
  
```
然后，把宿主机的key 加入 ssh的 authorized_keys，目前这个模板就做好了


- 把模板拷贝4份

IP如下，对应加入hostname

```bash

172.16.202.139    kafka1
172.16.202.141    kafka2
172.16.202.140    kafka3
172.16.202.142    kafka4

```

然后加入宿主机的hosts文件里面，这样安装就OK了，宿主机就可以很方便的通过主机名访问对应的主机了


#### 配置 
zk集群 搭建的记录如下

[zookeeper 集群搭建](https://www.njcx.bid/posts/M2.html)


然后，进入 kafka的配置conf文件夹，修改vim server.properties

```bash
broker.id=2
listeners=PLAINTEXT://172.16.202.141:9092
message.max.byte=5242880
default.replication.factor=2
replica.fetch.max.bytes=5242880
zookeeper.connect=172.16.202.144:2181,172.16.202.143:2181,172.16.202.145:2181

```

这里主要修改 broker.id 和 listeners 的ip，然后进入bin目录里面

```bash
./kafka-server-start.sh -daemon ../config/server.properties

```

集群就启动了，我们进 zk 任何一个节点，

```bash
# ./zkCli.sh

[zk: localhost:2181(CONNECTED) 8] ls /brokers/ids
[1, 2, 3, 4]
[zk: localhost:2181(CONNECTED) 9] get /brokers/ids/1
{"listener_security_protocol_map":{"PLAINTEXT":"PLAINTEXT"},"endpoints":["PLAINTEXT://172.16.202.139:9092"],"jmx_port":-1,"host":"172.16.202.139","timestamp":"1547395229963","port":9092,"version":4}
cZxid = 0x100000066
ctime = Sun Jan 13 11:00:29 EST 2019
mZxid = 0x100000066
mtime = Sun Jan 13 11:00:29 EST 2019
pZxid = 0x100000066
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x100002b6c820004
dataLength = 198
numChildren = 0
[zk: localhost:2181(CONNECTED) 10]


```

可以看到4个节点



#### 测试


```bash

#./ kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test_topic

创建 test_topic

#./kafka-topics.sh --list --zookeeper localhost:2181

查看是否创建 test_topic

#./kafka-console-producer.sh --broker-list localhost:9092 --topic  test_topic

创建生产者

#./kafka-console-consumer.sh --zookeeper localhost:2181 --topic  test_topic --from-beginning

创建消费者

# ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic  test_topic --from-beginning (新版本kafka .90版本之后)

创建消费者（新版本）	

```

#### 高可用HA


#### 监控

推荐使用

```bash
kafka-eagle

https://github.com/smartloli/kafka-eagle/archive/v1.2.8.tar.gz

```

```bash

export KE_HOME=/opt/kafka_eagle
export PATH=$PATH:$KE_HOME/bin

```


```bash
######################################
# multi zookeeper&kafka cluster list
######################################
kafka.eagle.zk.cluster.alias=cluster1
cluster1.zk.list=127.0.0.1:2181
#cluster2.zk.list=xdn10:2181,xdn11:2181,xdn12:2181

######################################
# zk client thread limit
######################################
kafka.zk.limit.size=25

######################################
# kafka eagle webui port
######################################
kafka.eagle.webui.port=8048

######################################
# kafka offset storage
######################################
cluster1.kafka.eagle.offset.storage=kafka
cluster2.kafka.eagle.offset.storage=zk

######################################
# enable kafka metrics
######################################
kafka.eagle.metrics.charts=false
kafka.eagle.sql.fix.error=false

######################################
# kafka sql topic records max
######################################
kafka.eagle.sql.topic.records.max=5000

######################################
# alarm email configure
######################################
kafka.eagle.mail.enable=false
kafka.eagle.mail.sa=alert_sa
kafka.eagle.mail.username=alert_sa@163.com
kafka.eagle.mail.password=mqslimczkdqabbbh
kafka.eagle.mail.server.host=smtp.163.com
kafka.eagle.mail.server.port=25

######################################
# alarm im configure
######################################
#kafka.eagle.im.dingding.enable=true
#kafka.eagle.im.dingding.url=https://oapi.dingtalk.com/robot/send?access_token=

#kafka.eagle.im.wechat.enable=true
#kafka.eagle.im.wechat.url=https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=
#kafka.eagle.im.wechat.touser=
#kafka.eagle.im.wechat.toparty=
#kafka.eagle.im.wechat.totag=
#kafka.eagle.im.wechat.agentid=

######################################
# delete kafka topic token
######################################
kafka.eagle.topic.token=keadmin

######################################
# kafka sasl authenticate
######################################
kafka.eagle.sasl.enable=false
kafka.eagle.sasl.protocol=SASL_PLAINTEXT
kafka.eagle.sasl.mechanism=PLAIN

######################################
# kafka jdbc driver address
######################################
kafka.eagle.driver=org.sqlite.JDBC
kafka.eagle.url=jdbc:sqlite:/opt/kafka_eagle/db/ke.db
kafka.eagle.username=root
kafka.eagle.password=root

```




