Title: MySQL主从复制解决方案实践
Date: 2016-01-02 10:20
Modified: 2016-01-02 10:20
Category: Linux
Tags: MySQL
Slug: A2
Authors: nJcx
Summary: 介绍一下linux下mysql主从复制搭建过程，记录一下学习过程
Status: draft

##测试环境
- kvm
- ubuntu16.04 server x2

![mysql1](../images/mysql1.png)

##安装mysql
```bash
 apt-get install -y mysql-server

```
##配置
```bash
mysql>create user repl; //创建新用户
//repl用户必须具有REPLICATION SLAVE权限，除此之外没有必要添加不必要的权限，密码为mysql。说明一下192.168.0.%，这个配置是指明repl用户所在服务器，这里%是通配符，表示192.168.0.0-192.168.0.255的Server都可以以repl用户登陆主服务器。当然你也可以指定固定Ip。
mysql> GRANT REPLICATION SLAVE ON *.* TO 'repl'@'192.168.122.%' IDENTIFIED BY '123456';

```


