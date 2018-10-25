Title: Zabbix实践笔记
Date: 2018-07-01 16:20
Modified: 2018-07-01 16:20
Category: Zabbix
Tags: zabbix
Slug: H25
Authors: nJcx
Summary: 记录一下Zabbix实践笔记 ~


#### 介绍


#### 安装

```bash

sudo tee -a /etc/yum.repos.d/zabbix.repo >> EOF
[zabbix]
name=Zabbix Official Repository - $basearch
baseurl=https://mirrors.aliyun.com/zabbix/zabbix/4.0/rhel/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ZABBIX-A14FE591
EOF

```
这里没有用zabbix官网的源，不知道是不是挂了，一直time out，所以我把baseurl 改为阿里源的。

```bash
yum install zabbix-server-mysql zabbix-web-mysql zabbix-agent -y
```
这里会报错

Requires: libiksemel.so.3()(64bit)
           
           
```bash

# wget ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/home:/aevseev/CentOS_CentOS-6/x86_64/iksemel-1.4-20.1.x86_64.rpm
# yum install iksemel-1.4-20.1.x86_64.rpm
 
```
```bash

yum install mariadb-server -y

```


#### 配置


