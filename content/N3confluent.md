Title: 使用Confluent替换Kafka
Date: 2018-07-17 20:20
Modified: 2018-07-17 20:20
Category: 安全
Tags: Kafka
Slug: N3
Authors: nJcx
Summary:  尝试使用Kafka connector写es ~
Status: draft

#### 安装


``` bash

wget  https://packages.confluent.io/archive/5.3/confluent-5.3.1-2.12.tar.gz

```

启动

```bash

./zookeeper-server-start -daemon ../etc/kafka/zookeeper.properties 

./kafka-server-start -daemon ../etc/kafka/server.properties 


```