Title: Python的多进程
Date: 2017-03-29 10:20
Modified: 2017-03-29 10:20
Category: Python
Tags: Python
Slug: C2
Authors: nJcx
Summary: 记录一下Python性能调优的一些方式
####简介
进程是静态代码的一次执行过程，在面向进程设计的系统（如早期的UNIX，Linux 2.4及更早的版本）中，进程是程序的基本执行实体；在面向线程设计的系统（如当代多数操作系统、Linux 2.6及更新的版本）中，进程本身不是基本运行单位，而是线程的容器。程序本身只是指令、数据及其组织形式的描述，进程才是程序（那些指令和数据）的真正运行实例。

进程包括下列数据：

- 那个程序的可运行机器码的一个在内存的映像。
- 分配到的内存（通常是虚拟的一个内存区域）。内存的内容包括可运行代码、特定于进程的数据（输入、输出）、调用堆栈、堆栈（用于保存运行时运输中途产生的数据）。
- 分配给该进程的资源的操作系统描述符，诸如文件描述符（Unix术语）或文件句柄（Windows）、数据源和数据终端。
- 安全特性，诸如进程拥有者和进程的权限集（可以容许的操作）。
- 处理器状态（内文），诸如寄存器内容、物理内存定址等。当进程正在运行时，状态通常存储在寄存器，其他情况在内存。

Unix/Linux操作系统提供了一个fork()系统调用，Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程，在Windows系统上，可以通过multiprocessing实现多进程，Windows平台通过pickle序列化 实现父进程与子进程沟通，如果multiprocessing在Windows下调用失败了，检查pickle过程中是否出现异常。

####multiprocessing使用
-  Process
- Lock
- Semaphore
- Event
-  Queue
- Pipe
- Pool

通过创建Process类的对象来创建进程，Process([group [, target [, name [, args [, kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。name为别名。group实质上不使用。

```python

# -*- coding: utf-8 -*-
import os
from multiprocessing import Process

def findx(name):
    print name 
    print '子进程(%s)' % ( os.getpid())

if __name__=='__main__':
    print '父进程 (%s)' % os.getpid()
    p = Process(target=findx, args=(' 我是宝宝',))
    print '开始'
    p.start()
    p.join()
    print '结束'
    
  """  
父进程 (10037)
开始
我是宝宝
子进程(10038)
结束
"""
    
```

如果我们需要建一个进程池，供使用时从中随机选取一个进程处理任务，我们需要使用Pool类，一般情况下，Pool默认创建的进程数等于CPU核心数，Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])，

```python
# -*- coding: utf-8 -*-
import os
from multiprocessing import Pool

def findx(name):
    print name
    print '子进程(%s)' % ( os.getpid())

if __name__=='__main__':
    print '父进程 (%s)' % os.getpid()
    p =  Pool(4)
    for x in range(4):
        p.apply_async(findx,args=(x,))
    print '开始'
    p.close()
    p.join()
    print '结束'
    
```

进程之间肯定是需要通信的，multiprocessing提供了相关封装，简单介绍一下 Queue的使用

```python

from multiprocessing import Process, Queue

def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)

def read(q):
    while True:
        value = q.get()
        print 'Get %s from queue.' % value

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    
```

Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
 
get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。


