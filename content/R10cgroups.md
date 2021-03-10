Title: Linux的cgroups在HIDS-Agent 开发上的应用 
Date: 2018-07-18 02:20
Modified: 2018-07-18 02:20
Category: 安全
Tags: HIDS
Slug: R10 
Authors: nJcx
Summary: Linux的cgroups在HIDS-Agent 开发上的应用~


#### 介绍


cgroups 是Linux内核提供的一种可以限制单个进程或者多个进程所使用资源的机制，可以对 cpu，内存等资源实现精确的控制，Docker 就使用了 cgroups 提供的资源限制能力来完成cpu，内存等部分的资源控制。

cgroups 的全称是control groups，cgroups为每种可以控制的资源定义了一个子系统。典型的子系统介绍如下：

- cpu 子系统，主要限制进程的 cpu 使用率。
- cpuacct 子系统，可以统计 cgroups 中的进程的 cpu 使用报告。
- cpuset 子系统，可以为 cgroups 中的进程分配单独的 cpu 节点或者内存节点。
- memory 子系统，可以限制进程的 memory 使用量。
- blkio 子系统，可以限制进程的块设备 io。
- devices 子系统，可以控制进程能够访问某些设备。
- net_cls 子系统，可以标记 cgroups 中进程的网络数据包，然后可以使用 tc 模块（traffic control）对数据包进行控制。
- net_prio 子系统, 限制任务中网络流量的优先级.
- pids 子系统，  限制控制组中进程可以派生出的进程数量。
- freezer 子系统，可以挂起或者恢复 cgroups 中的进程。
namespace。


cgroup和namespace类似，也是将进程进行分组，但它的目的和namespace不一样，namespace是为了隔离进程组之间的资源，而cgroup是为了对一组进程进行统一的资源监控和限制。

cgroup分v1和v2两个版本，v1实现较早，最初版本是在 Linux 2.6.24，随着时间的推移，添加了越来越多的controller，而这些controller又各自独立开发，导致了controller之间很大的不一致，功能比较多，但是由于它里面的功能都是零零散散的实现的，所以规划的不是很好，导致了一些使用和维护上的不便，v2的出现就是为了解决v1中这方面的问题，随着v2一起引入内核的还有cgroup namespace。Linux 3.10 提供了作为试验特性的 Cgroups V2, 到了 Linux kernel 4.5 后 Cgroups V2 才成为正式特性。


Cgroup提供了一个原生接口并通过cgroupfs提供（从这句话我们可以知道cgroupfs就是Cgroup的一个接口的封装）。类似于procfs和sysfs，是一种虚拟文件系统。并且cgroupfs是可以挂载的，默认情况下挂载在/sys/fs/cgroup目录。使用 mount 挂载 cgroup 文件系统就可以使用配置这些controller了，系统通常已经挂载好了。Linux 通过虚拟文件系统的方式将功能和配置暴露给用户，这得益于 Linux 的虚拟文件系统（VFS），VFS 将具体文件系统的细节隐藏起来，给用户态一个统一的问题件系统 API 接口，

