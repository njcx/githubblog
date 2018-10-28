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

master 

包含kube-apiserver，kube-scheduler，kube-controller-manager

```bash

# yum install -y epel-release
# yum makecache 
# yum install -y etcd kubernetes-master kubernetes-client 

```

slave1

包含 kubelet，kube-proxy，kubectl


```bash
# yum install -y epel-release
# yum makecache 
# yum install -y kubernetes-node

```


slave2

```bash
# yum install -y epel-release
# yum makecache 
# yum install -y kubernetes-node

```

#### 配置

```bash
[root@localhost ~]# systemctl daemon-reload
[root@localhost ~]# systemctl enable etcd.service
[root@localhost ~]# systemctl start etcd.service
[root@localhost ~]# systemctl start kube-apiserver.service
[root@localhost ~]# systemctl start kube-controller-manager.service
[root@localhost ~]# systemctl start kube-scheduler.service
[root@localhost ~]# systemctl enable kube-apiserver.service
[root@localhost ~]# systemctl enable kube-controller-manager.service
[root@localhost ~]# systemctl enable kube-scheduler.service

```

slave1

```bash
[root@localhost ~]# systemctl daemon-reload
[root@localhost ~]# systemctl enable docker.service
[root@localhost ~]# systemctl start docker.service
[root@localhost ~]# systemctl enable kubelet.service
[root@localhost ~]# systemctl start kubelet.service
[root@localhost ~]# systemctl enable kube-proxy.service
[root@localhost ~]# systemctl start kube-proxy.service

```

slave2

```bash
[root@localhost ~]# systemctl daemon-reload
[root@localhost ~]# systemctl enable docker.service
[root@localhost ~]# systemctl start docker.service
[root@localhost ~]# systemctl enable kubelet.service
[root@localhost ~]# systemctl start kubelet.service
[root@localhost ~]# systemctl enable kube-proxy.service
[root@localhost ~]# systemctl start kube-proxy.service

```
