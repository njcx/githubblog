Title: bro 打log进kafka
Date: 2018-06-06 13:20
Modified: 2018-06-06 13:20
Category: bro
Tags: bro
Slug: H7
Authors: nJcx
Summary: bro 打log进kafka

#### 安装

bro的安装参照[bro安装](https://www.njcx.bid/posts/H11.html)

编译 librdkafka

```bash

二选一

# wget https://github.com/edenhill/librdkafka/archive/v0.11.5.tar.gz

# tar -zxvf v0.11.5.tar.gz

# cd librdkafka-0.11.5 && ./configure && make && make install


# yum install librdkafka  librdkafka-devel -y
 
```

把bro 添加到环境变量  （/etc/profile）

```bash
export BRO_HOME=/opt/bro
export PATH=$PATH:$BRO_HOME/bin

```

注意：

bro-2.5.5.tar.gz  解压后的源码目录不要删除，后面有用


```bash
#  pip install zkg
#  zkg autoconfig
```

bro-pkg 是bro的包管理器，在包安装的过程中，会依赖bro源码目录，不然某些bro插件安装会报错

安装metron-bro-plugin-kafka插件

```bash
#  zkg install apache/metron-bro-plugin-kafka --version master
```





编译 bro 的 kafka插件

```bash

#cd bro-2.5.5/aux/plugins/kafka/
# ./configure --bro-dist=../../.. --install-root=/opt/bro/lib/bro/plugins
# make && make install

```

测试

```bash
# bro -N Bro::Kafka
Bro::Kafka - Writes logs to Kafka (dynamic, version 0.1)
```
#### 配置


```bash
@load Bro/Kafka/logs-to-kafka.bro
redef Kafka::logs_to_send = set(Conn::LOG, HTTP::LOG);
redef Kafka::kafka_conf = table(
    ["metadata.broker.list"] = "localhost:9092"
);
redef Kafka::topic_name = "bro";
```
启动

```bash
#./broctl deploy
#./broctl start

```



#### 测试

```bash

#./ kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic bro

创建 bro topic

#./kafka-topics.sh --list --zookeeper localhost:2181

查看是否创建bro

#./kafka-console-producer.sh --broker-list localhost:9092 --topic bro

创建生产者

#./kafka-console-consumer.sh --zookeeper localhost:2181 --topic bro --from-beginning

创建消费者

# ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bro --from-beginning (新版本kafka .90版本之后)

创建消费者（新版本）	

```






