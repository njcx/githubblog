Title: Zabbix4.0实践笔记
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
gpgkey=https://mirrors.aliyun.com/zabbix/RPM-GPG-KEY-ZABBIX
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

首先启动MariaDB
```bash
systemctl start mariadb
```
设置开机启动
```bash
systemctl enable mariadb
```
接下来进行MariaDB的相关简单配置
```bash
mysql_secure_installation
```
首先是设置密码，会提示先输入密码
配置MariaDB的字符集

vim /etc/my.cnf

```bash

[mysqld]
init_connect='SET collation_connection = utf8_general_ci' 
init_connect='SET NAMES utf8' 
character-set-server=utf8 
collation-server=utf8_general_ci 
skip-character-set-client-handshake

```

vim /etc/my.cnf.d/client.cnf
在[client]中添加

```bash
default-character-set=utf8
```

vim /etc/my.cnf.d/mysql-clients.cnf
在[mysql]中添加

```bash
default-character-set=utf8
```
全部配置完成，重启mariadb

```bash
systemctl restart mariadb
```
之后进入MariaDB查看字符集

```bash
mysql> show variables like "%character%";show variables like "%collation%";
```

```bash

mysql> create database zabbix;
mysql> grant all privileges on zabbix.* to njcx@localhost identified by 'qwaszxerdfcv';
mysql> quit;

```

```bash

 zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -unjcx -p zabbix
 
```

启动 zabbix_server 报错

```bash

29225:20180714:084923.611 cannot start preprocessing service: Cannot bind socket to "/var/run/zabbix/zabbix_server_preprocessing.sock": [13] Permission denied.

```
关闭selinux 即可, 先临时关闭，setenforce 0

vim /etc/selinux/config

```
SELINUX=disabled

```
永久关闭

```bash
# vim /etc/php.ini
date.timezone = Asia/Shanghai

```

