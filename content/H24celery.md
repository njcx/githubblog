Title: celery 实践笔记
Date: 2018-07-01 11:20
Modified: 2018-07-01 11:20
Category: Celery
Tags: Celery
Slug: H24
Authors: nJcx
Summary: 记录一下Celery 实践笔记 ~
Status: draft

#### 介绍
Celery(芹菜)是一个异步任务队列/基于分布式消息传递的作业队列。Celery建议的消息队列是RabbitMQ，但提供有限支持Redis。在Celery中几个基本的概念，需要先了解下。概念：Broker、Backend。

- 什么是broker？

broker是一个消息传输的中间件，其中Broker的中文意思是 经纪人，相当于包工头，活的分发都经过broker，这个broker有几个方案可供选择：RabbitMQ (消息队列)，Redis（缓存数据库），数据库（不推荐），等等

- 什么是backend？

通常程序发送的消息，发完就完了，可能都不知道对方时候接受了。为此，celery实现了一个backend，用于存储这些消息以及celery执行的一些消息和结果。Backend是在Celery的配置中的一个配置项 CELERY_RESULT_BACKEND ，作用是保存结果和状态，如果你需要跟踪任务的状态，那么需要设置这一项，可以是Database backend，也可以是Cache backend，具体可以参考这里：CELERY_RESULT_BACKEND 。至于 backend，就是数据库。backend我使用的是redis

![CELERY](../images/celery.png)

#### 安装

```bash

# wget http://download.redis.io/releases/redis-4.0.11.tar.gz
# tar -zxvf redis-4.0.11.tar.gz
# cd redis-4.0.11 && make && make install 

```

然后进入utils 目录

```bash

./install_server.sh

```

redis 就把 服务添加到 /etc/init.d/目录了，并且 开机自动启动了，服务名称redis_6379 ，如果更改了默认端口，服务名称就是 redis_端口号。

```bash

# curl -s https://packagecloud.io/install/repositories/rabbitmq/erlang/script.rpm.sh | sudo bash
# sudo yum install erlang-20.3.8.9-1.el7.centos.x86_64 (可以不用，由下面自行处理依赖，以免出现兼容性问题)

# curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.rpm.sh | sudo bash
# yum install rabbitmq-server-3.7.8-1.el7.noarch

```

#### 配置

vim /etc/rabbitmq/rabbitmq.config

```bash
[{rabbit, [{loopback_users, []}]}].
```

```bash

rabbitmq-plugins enable rabbitmq_management 

service rabbitmq-server start

```
启动

访问 http://IP:15672/，账号 ：guest ： guest


```bash


# rabbitmqctl add_user njcx test   

#创建了一个RabbitMQ用户,用户名为njcx，密码是test

# rabbitmqctl add_vhost njcxtest 

#  #创建了一个虚拟主机，主机名为njcxtest


# rabbitmqctl set_permissions -p njcxtest test ".*" ".*" ".*"

# 设置权限。允许用户njcx访问虚拟主机njcxtest，因为RabbitMQ通过主机名来与节点通信

```
