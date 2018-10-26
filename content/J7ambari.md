Title: ambari 实践笔记
Date: 2018-07-03 19:20
Modified: 2018-07-03 19:20
Category: Big data
Tags: ambari
Slug: J7
Authors: nJcx
Summary: 记录一下ambari实践笔记 ~


#### 介绍


#### 安装

系统：CentOS7.3

```bash

# wget https://mirrors.aliyun.com/apache/ambari/ambari-2.7.1/apache-ambari-2.7.1-src.tar.gz 
# tar -zxvf apache-ambari-2.7.1-src.tar.gz
# cd apache-ambari-2.7.1-src

mvn versions:set -DnewVersion=2.7.1.0.0 
pushd ambari-metrics
mvn versions:set -DnewVersion=2.7.1.0.0
popd


```
```bash

mvn -B clean install rpm:rpm -DnewVersion=2.7.1.0.0 -DbuildNumber=90430db08a5f543a97d97918cf5f711f2786ad8a -DskipTests -Dpython.ver="python >= 2.6"

```

- server安装

编译后，在如下目录查找，ambari-server/target/rpm/ambari-server/RPMS/noarch/

```bash

yum install ambari-server*.rpm
 
```
```bash
ambari-server setup
ambari-server start
```

- agent 安装
编译后，在如下目录查找，ambari-agent/target/rpm/ambari-agent/RPMS/x86_64/ 

```bash
yum install ambari-agent*.rpm
```

vim /etc/ambari-agent/ambari.ini

```bash
[server]
hostname=localhost

```
ambari-agent start


#### 配置