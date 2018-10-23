Title: centos7搭建openvas 
Date: 2017-05-28 17:20
Modified: 2017-05-28 17:20
Category: 安全
Tags: openvas
Slug: H22
Authors: nJcx
Summary: 记录一下学习openvas心路~


#### 介绍
OpenVAS是一款开源的漏洞扫描攻击，主要用来检测网络或主机的安全性。其强大的扫描能力来自于集成数万个漏洞测试程序，这些测试程序以插件的形式提供，可以从官方网站免费更新.

![openvas1](../images/openvas1.jpg)

#### 安装

```bash

wget -q -O - http://www.atomicorp.com/installers/atomic |sh

```
然后，关闭selinux，修改/etc/selinux/config文件，将SELINUX=enforcing改为SELINUX=disabled

#### 启动

openvas-setup

openvas-check-setup

greenbone-nvt-sync

greenbone-scapdata-sync

greenbone-certdata-sync

openvasmd --rebuild


```bash
# openvassd
# openvasmd
```

```bash 
创建用户
openvasmd --create-user=admin --role=Admin
openvasmd --user=admin --new-password=*******

```
openvas-check-setup --v9

gsad --listen=0.0.0.0 --port=9392

然后访问 https://ip:9392

如果有异常，关闭防火墙就OK，或者开策略

- 启动： systemctl start firewalld
- 关闭： systemctl stop firewalld
- 查看状态： systemctl status firewalld 
- 开机禁用  ： systemctl disable firewalld
