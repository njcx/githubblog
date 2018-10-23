Title: docker应用实践
Date: 2017-01-15 10:20
Modified: 2017-01-15 10:20
Category: Linux
Tags: docker
Slug: B3
Authors: nJcx
Summary: 介绍一下docker 容器应用，记录一下学习过程
##安装
2017年4月测试正常,ubuntu16.04
```bash
sudo apt-get -y install \
  apt-transport-https \
  ca-certificates \
  curl

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
       $(lsb_release -cs) \
       stable"

sudo apt-get update
sudo apt-get -y install docker-ce

```

##Docker的三个基本概念
* 镜像
* 容器
* 仓库

容器是镜像的一次运行,修改需要提交,仓库是放镜像的地方,hub是放仓库的地方
##Docker的使用

[docker 常用命令记录](http://www.njcxs.cc/posts/B4.html)

##小结
Docker几乎就没有什么虚拟化的东西，并且直接复用了Host主机的OS，在Docker Engine层面实现了调度和隔离重量一下子就降低了好几个档次.Docker的容器利用了LXC，管理利用了namespaces 来做权限的控制和隔离,cgroups来进行资源的配置,并且还通过aufs来进一步提高文件系统的资源利用率。其中的 aufs 是个很有意思的东西，是 UnionFS的一种.他的思想和 git 有些类似，可以把对文件系统的改动当成一次 commit 一层层的叠加。这样的话多个容器之间就可以共享他们的文件系统层次，每个容器下面都是共享的文件系统层次，上面再是各自对文件系统改动的层次，这样的话极大的节省了对存储的需求，并且也能加速容器的启动。

这可以在单一Linux实体下运作，避免引导一个虚拟机造成的额外负担。Linux核心对名字空间的支持完全隔离了工作环境中应用程序的视野，包括进程树、网络、用户ID与挂载文件系统，而核心的cgroup提供资源隔离，包括CPU、内存、block I/O与网络。从0.9版本起，Dockers在使用抽象虚拟是经由libvirt的 LXC与systemd - nspawn提供界面的基础上，开始包括libcontainer库做为以自己的方式开始直接使用由Linux核心提供的虚拟化的设施，

那么什么是cgroups呢？cgroups，其名称源自控制组群（control groups）的简写，是Linux内核的一个功能，用来限制，控制与分离一个进程组群的资源（如CPU、内存、磁盘输入输出等）。最早的名称为进程容器（process containers）。在2007年时，因为在Linux内核中，容器（container）这个名词有许多不同的意义，为避免混乱，被重命名为cgroup，并且被合并到2.6.24版的内核中去。

LXC又是什么呢？LXC，其名称来自Linux软件容器（Linux Containers）的缩写，一种操作系统层虚拟化（Operating system–level virtualization）技术，为Linux内核容器功能的一个用户空间接口。它将应用软件系统打包成一个软件容器（Container），内含应用软件本身的代码，以及所需要的操作系统核心和库。通过统一的名字空间和共用API来分配不同软件容器的可用硬件资源，创造出应用程序的独立沙箱运行环境，使得Linux用户可以容易的创建和管理系统或应用容器。(感觉好像没有讲一样）

##一些应用
- 环境打包
- 应用隔离
- 基础镜像
