Title: spark 集群搭建
Date: 2018-07-01 09:20
Modified: 2018-07-01 09:20
Category: 大数据
Tags: spark
Slug: H21
Authors: nJcx
Summary: 记录一下spark集群的搭建 ~

#### 介绍
Spark是一个计算引擎,是加州大学伯克利分校的AMP实验室所开源的通用并行框架，是在 Scala中实现的，拥有如下模块，SQL、DataFrames、MLlib、GraphX、Spark Streaming。 开发者可以在同一个应用程序中无缝组合使用这些库。

#### 安装
版本 ：spark-2.2.2 ,jdk-8u181,scala-2.12.6

目录 : /opt

```bash

wget https://downloads.lightbend.com/scala/2.12.6/scala-2.12.6.tgz

wget https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.2.2/spark-2.2.2-bin-hadoop2.7.tgz

wget http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz

```
tar -zxvf spark-2.2.2-bin-hadoop2.7.tgz && tar -zxvf jdk-8u181-linux-x64.tar.gz

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

#### 