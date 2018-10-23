Title: centos7搭建rabbitmq
Date: 2017-05-28 20:20
Modified: 2017-05-28 20:20
Category: rabbitmq
Tags: rabbitmq
Slug: H23
Authors: nJcx
Summary: 记录一下学习rabbitmq心路~


#### 介绍


#### 安装

添加阿里源的centos7的源，包括epel源

```bash
# cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

# curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

# cp /etc/yum.repos.d/epel.repo  /etc/yum.repos.d/epel.repo.bak

# curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

```

