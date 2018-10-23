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

```bash

# curl -s https://packagecloud.io/install/repositories/rabbitmq/erlang/script.rpm.sh | sudo bash
# sudo yum install erlang-20.3.8.9-1.el7.centos.x86_64 (可以不用，由下面自行处理依赖，以免出现兼容性问题)

# curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.rpm.sh | sudo bash
# yum install rabbitmq-server-3.7.8-1.el7.noarch
``` 

这里注意rabbitmq-server 和 erlang 的兼容性



