Title: kubernetes 了解一下
Date: 2018-07-03 20:20
Modified: 2018-07-03 20:20
Category: kubernetes
Tags: kubernetes
Slug: H9
Authors: nJcx
Summary: Kubernetes安装与使用

#### 介绍

master 节点

- etcd 非关系型数据库
- flannel 实现夸主机的容器网络的通信
- kube-apiserver 核心组件，所有组件均与其通信，提供Http Restful接口
- kube-controller-manager 集群内部管理中心，负责各类资源管理，如RC，Pod，命名空间等
- kube-scheduler 调度组件，负责node的调度

slave节点
- kubelet Node节点中核心组件，负责执行Master下发的任务 
- kube-proxy 代理，负责kubelet与apiserver网络。相当于负载均衡，将请求转到后端pod中

![k8s](../images/k8s.png)
#### 安装


```bash

# wget http://download.redis.io/releases/redis-4.0.11.tar.gz
# tar -zxvf redis-4.0.11.tar.gz
# cd redis-4.0.11 && make && make install 

```
