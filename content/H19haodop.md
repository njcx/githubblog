Title: hadoop 集群搭建
Date: 2018-07-01 08:20
Modified: 2018-07-01 08:20
Category: Big data
Tags: hadoop
Slug: H19
Authors: nJcx
Summary: 记录一下hadoop搭建 ~
Status: draft

#### 介绍
Hadoop是一个开源框架，它允许在整个集群使用简单编程模型计算机的分布式环境存储并处理大数据。它的目的是从单一的服务器到上千台机器的扩展，每一个台机都可以提供本地计算和存储。Hadoop的框架最核心的设计就是：HDFS和MapReduce。HDFS为海量的数据提供了存储，则MapReduce为海量的数据提供了计算。NameNode是一个通常在 HDFS 实例中的单独机器上运行的软件。它负责管理文件系统名称空间和控制外部客户机的访问。DataNode也是一个通常在 HDFS实例中的单独机器上运行的软件。DataNode 响应来自 HDFS 客户机的读写请求。它们还响应来自 NameNode 的创建、删除和复制块的命令。MapReduce是处理大量半结构化数据集合的编程模型。

#### 安装

版本：hadoop-2.7.7 , jdk-8u181

目录：/opt

```bash
wget http://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz 

wget http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz

```
tar -zxvf hadoop-2.7.7.tar.gz && tar -zxvf jdk-8u181-linux-x64.tar.gz

```bash

echo -e "export JAVA_HOME=/opt/jdk1.8.0_181 \n\
export JRE_HOME=\${JAVA_HOME}/jre \n\
export CLASSPATH=.:\${JAVA_HOME}/lib:\${JRE_HOME}/lib \n\
export PATH=\${JAVA_HOME}/bin:\$PATH \n\
" >> /etc/profile && source /etc/profile

```


#### 配置

3台 vps

```bash
192.168.1.110  Master
192.168.1.107  Slave1
192.168.1.108  Slave2
```
把上面的内容加入master节点　vim /etc/hosts

```bash

scp /etc/hosts root@192.168.1.107:/etc
scp /etc/hosts root@192.168.1.108:/etc

```

vim /etc/ssh/sshd_config

```bash
RSAAuthentication yes # 启用 RSA 认证
PubkeyAuthentication yes # 启用公钥私钥配对认证方式
AuthorizedKeysFile .ssh/authorized_keys # 公钥文件路径（和上面生成的文件同）
```

```bash
scp  /etc/ssh/sshd_config root@192.168.1.107:/etc/ssh/
scp  /etc/ssh/sshd_config root@192.168.1.108:/etc/ssh/
```

生成ssh-key  ：  ssh-keygen -t rsa -P ''

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
在这里把彼此的公钥都加入进去，也随便把控制机的公钥加入了

```bash
scp ~/.ssh/authorized_keys root@192.168.1.108:~/.ssh/
scp ~/.ssh/authorized_keys root@192.168.1.107:~/.ssh/
```
  
 加入hadoop环境变量配置
 
 
```bash

export HADOOP_HOME=/opt/hadoop-2.7.7/
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"

``` 
/opt/hadoop-2.7.7目录下创建数据存放的文件夹，tmp、hdfs、hdfs/data、hdfs/name

配置hadoop-2.7.7/etc/hadoop目录下的core-site.xml

```xml

 <configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/opt/hadoop-2.7.7/tmp</value>
    </property>
    <property>
        <name>io.file.buffer.size</name>
        <value>131702</value>
    </property>
 </configuration>
 
```
配置hadoop-2.7.7/etc/hadoop目录下的hdfs-site.xml

```xml

 <configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/opt/hadoop-2.7.7/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/opt/hadoop-2.7.7/dfs/data</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>2</value>
    </property>
    <property>
    <name>dfs.webhdfs.enabled</name>
    <value>true</value>
    </property>
 </configuration>
 
```

配置hadoop-2.7.7/etc/hadoop目录下的mapred-site.xml

```xml

<configuration>
    <property>  
        <name>mapreduce.framework.name</name>  
        <value>yarn</value>  
    </property>  
</configuration>

```
配置hadoop-2.7.7/etc/hadoop目录下的yarn-site.xml

```xml

<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>

```


然后在 hadoop-env.sh 里面添加如下，不然可能会出现 JAVA_HOME找不到现象。

```bash
export JAVA_HOME=/opt/jdk1.8.0_181

```

vim slaves 

```bash
Slave1
Slave2

```
然后把hadoop文件夹scp 到slave1，slave2

```bash
scp -r hadoop-2.7.7 root@192.168.1.107:/opt
scp -r hadoop-2.7.7 root@192.168.1.108:/opt
```

在master机器上，任意目录输入 hdfs namenode -format 格式化namenode，第一次使用需格式化一次，之后就不用再格式化，如果改一些配置文件了，可能还需要再次格式化

启动 ： start-all.sh

输入 jps 查看当前java的进程

