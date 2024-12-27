Title: 环境变量、源和软件包名记录
Date: 2017-04-14  22:20
Modified: 2017-04-14  22:20
Category: 杂项
Tags: 环境变量和软件包名
Slug: J11
Authors: nJcx
Summary: 环境变量和软件包名以及依赖（方便粘贴）
Status: draft

####  环境变量

```bash
export JAVA_HOME=/opt/jdk1.8.0_181
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

export SCALA_HOME=/opt/scala-2.12.6
export PATH=$PATH:$SCALA_HOME/bin

export MAVEN_HOME=/opt/apache-maven-3.5.4
export PATH=${MAVEN_HOME}/bin:${PATH}


export HADOOP_HOME=/opt/hadoop-2.7.7/
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"

export SPARK_HOME=/opt/spark-2.3.2-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin

```

####  源

pip 源

```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

```

CentOS7 （清华）

记得备份

```bash

cp /etc/yum.repos.d/CentOS-Base.repo  /etc/yum.repos.d/CentOS-Base.repo.bak

cp /etc/yum.repos.d/epel.repo  /etc/yum.repos.d/epel.repo.bak

```


```bash

[base]
name=CentOS-$releasever - Base
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/os/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#released updates
[updates]
name=CentOS-$releasever - Updates
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/updates/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/extras/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus
baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos/$releasever/centosplus/$basearch/
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

```

```bash
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/7/$basearch
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 7 - $basearch - Debug
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/7/$basearch/debug
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 7 - $basearch - Source
baseurl=https://mirrors.tuna.tsinghua.edu.cn/epel/7/SRPMS
#mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-source-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

```


CentOS7 阿里源


```bash

curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

```

kali linux 

```bash

#阿里云
deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib 
deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib 

#清华大学 
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free 
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free 

#浙江大学 
deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free 
deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free 
```

mysql 源

```bash
rpm -ivh https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
```

#### 软件包 


```bash

yum groupinstall development tools

yum install -y pcre pcre-devel zlip zlib-devel openssl openssl-devel 

yum install python-devel python-pip python-virtualenv


yum install mongodb-server mariadb-server 

yum install redis 

yum install python36 python36-devel
 
 
```

#### nodejs


```bash

wget https://npm.taobao.org/mirrors/node/v10.14.2/node-v10.14.2-linux-x64.tar.gz 

```

```bash
export NODE_HOME=/root/node-v10.14.2-linux-x64
export PATH=$PATH:$NODE_HOME/bin
export NODE_PATH=$NODE_HOME/lib/node_modules
```
