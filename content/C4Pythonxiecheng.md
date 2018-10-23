Title: Python的协程以及通过多进程加协程进行性能调优
Date: 2017-04-2 10:20
Modified: 2017-04-2 10:20
Category: Python
Tags: Python
Slug: C4
Authors: nJcx
Summary: 记录一下Python性能调优的一些方式
####介绍
不管是进程还是线程，每次阻塞、切换都需要陷入系统调用，都会带来一定的开销，但是,协程不参与系统调度，完全是用户可控的。下面，就简单的介绍一下有关Python协程的使用，以及用Python 多进程加协程进行性能调优。同时，我也写了有关Python  多进程和多线程相关的博文。如下：

[Python 的多线程](B8.html)

[Python的多进程](C2.html)