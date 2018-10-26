Title: kafka安装与使用
Date: 2018-06-04 13:20
Modified: 2018-06-04 13:20
Category: Big data
Tags: kafka
Slug: H5
Authors: nJcx
Summary: kafka相关

#### 安装

地址 

```bash

https://downloads.lightbend.com/scala/2.12.6/scala-2.12.6.tgz

http://mirrors.hust.edu.cn/apache/kafka/2.0.0/kafka_2.12-2.0.0.tgz

http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz

```

下载并且解压


```bash

cd /opt && download  ALL  && tar -zxvf  ALL

```

配置环境变量

```bash

echo -e "export JAVA_HOME=/opt/jdk1.8.0_181 \n\
export JRE_HOME=\${JAVA_HOME}/jre \n\
export CLASSPATH=.:\${JAVA_HOME}/lib:\${JRE_HOME}/lib \n\
export PATH=\${JAVA_HOME}/bin:\$PATH \n\

export SCALA_HOME=/opt/scala-2.12.6 \n\
export PATH=\$PATH:\$SCALA_HOME/bin \n\
" >> /etc/profile && source /etc/profile

```



安装 kafka-manage

配置sbt 国内源

```bash 
#cd ~ && vim .sbt/repositories

```

```ini

[repositories]
local
aliyun: http://maven.aliyun.com/nexus/content/groups/public
typesafe: http://repo.typesafe.com/typesafe/ivy-releases/, [organization]/[module]/(scala_[scalaVersion]/)(sbt_[sbtVersion]/)[revision]/[type]s/[artifact](-[classifier]).[ext], bootOnly

```
编译

```bash

#git clone https://github.com/yahoo/kafka-manager

#cd kafka-manager && ./ sbt clean dist

# cd target/universal/     可执行文件所在目录

```

有点慢，搞杯茶喝喝，3杯茶都喝了,还是找个已经编译好的吧

```bash

git clone  https://github.com/njcx/kafka-manage-bin.git

```

#### ZooKeeper

默认端口2181

```bash

# cd /opt && wget http://mirrors.hust.edu.cn/apache/zookeeper/stable/zookeeper-3.4.12.tar.gz

# tar -zxvf zookeeper-3.4.12.tar.gz

# cd zookeeper-3.4.12/conf 

# cp zoo_sample.cfg zoo.cfg && cd ../bin
 
# ./zkServer.sh start

```

#### Kafka 

```bash

# cd kafka_2.12-1.0.0/bin

# ./kafka-server-start.sh  -daemon ../config/server.properties


```


#### kafka-manage 

```bash
# cd /opt/kafka-manage-bin/bin

# nohup ./kafka-manager >> kafka-manager.log  2>&1 &

```


#### 管理





