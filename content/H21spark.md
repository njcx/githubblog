Title: spark 集群搭建
Date: 2018-07-01 09:20
Modified: 2018-07-01 09:20
Category: Big data
Tags: spark
Slug: H21
Authors: nJcx
Summary: 记录一下spark集群的搭建 ~

#### 介绍
Spark是一个计算引擎,是加州大学伯克利分校的AMP实验室所开源的通用并行框架，是在 Scala中实现的，拥有如下模块，SQL、DataFrames、MLlib、GraphX、Spark Streaming。 开发者可以在同一个应用程序中无缝组合使用这些库。

#### 安装
版本 ：spark-2.3.2,jdk-8u181,scala-2.12.6

目录 : /opt

```bash

wget https://downloads.lightbend.com/scala/2.12.6/scala-2.12.6.tgz

https://mirrors.aliyun.com/apache/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz

wget http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz

```
tar -zxvf spark-2.3.2-bin-hadoop2.7.tgz && tar -zxvf jdk-8u181-linux-x64.tar.gz && tar -zxvf scala-2.12.6.tgz

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

然后再把spark 添加到环境变量里面

```bash
export SPARK_HOME=/opt/spark-2.3.2-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin
```

#### 配置


```bash

cp spark-env.sh.template spark-env.sh
　
```


vim spark-env.sh

```bash

export JAVA_HOME=/opt/jdk1.8.0_181
export SCALA_HOME=/opt/scala-2.12.6
export HADOOP_HOME=/opt/hadoop-2.7.7/
export HADOOP_CONF_DIR=/opt/hadoop-2.7.7/etc/hadoop
export SPARK_MASTER_IP=192.168.1.110
export SPARK_MASTER_HOST=192.168.1.110
export SPARK_LOCAL_IP=192.168.1.110
export SPARK_WORKER_MEMORY=1g
export SPARK_WORKER_CORES=2
export SPARK_HOME=/opt/spark-2.3.2-bin-hadoop2.7
export SPARK_DIST_CLASSPATH=$(/opt/hadoop-2.7.7/bin/hadoop classpath)

```

cp slaves.template slaves


```bash
Master
Slave1
Slave2
```

scp -r  spark-2.3.2-bin-hadoop2.7 root@192.168.1.108:/opt

scp -r  spark-2.3.2-bin-hadoop2.7 root@192.168.1.107:/opt

然后在Slave1 ，Slave2上添加 spark的环境变量

```bash

export SPARK_HOME=/opt/spark-2.3.2-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin

```
并且在 slave1 和 slave2 上修改spark-env.sh “export SPARK_LOCAL_IP=” 为本机ip。

启动 /sbin/start-all.sh

jps 验证

```bash

5809 Jps
5749 Worker
1882 DataNode

```

有个Worker即为成功





