Title: Linux环境下的Rootkit技术细节
Date: 2018-06-17 03:20
Modified: 2018-06-17 03:20
Category: 安全
Tags: Linux
Slug: O4
Authors: nJcx
Summary: Linux环境下的Rootkit技术细节~

#### 安装

```bash
https://github.com/f0rb1dd3n/Reptile.git
https://github.com/naworkcaj/bdvl.git
https://github.com/yaoyumeng/adore-ng.git
https://github.com/citypw/suterusu.git
https://github.com/jgamblin/Mirai-Source-Code.git
https://github.com/m0nad/Diamorphine.git
https://raw.githubusercontent.com/yzimhao/godpock/master/Rootkit/mafix.tar.gz
```

Rootkit 主要分为两种，一种是用户态的rootkit，一种是内核态的rootkit


   
1. 隐藏文件
入侵者需要做如下事情: 
  1) 替换一些系统常用命令如"ls", "du", "fsck"
  这可以通过重定向可执行文件技术达到，通过截获sys_execve()，无论何时系统尝试去执行"ls"程序的时候, 它都会被重定向到入侵者给定的其他程序。
  2) 在底层方面，他们通过把硬盘里的一些区域标记为坏块并把它的文件放在那里
  3) 或者把一些文件放入引导块里
  4) read系统调用劫持

2. 隐藏进程
  1) 替换"ps"、"top"程序
  2) 修改/proc下的内核变量
  3) 劫持read、getdents64系统调用，直接对指定进程进行过滤

3. 隐藏网络连接状态
  1) 修改/proc/net
  2) 对netfilter提供的回调点注册过滤函数

4. 隐藏sniffer
  1) 隐藏网络接口的杂拨模式
  通过替换劫持sys_ioctl()系统调用实现

5. 隐藏rootkit模块本身
  1) 隐藏lkm本身
  一个优秀的lkm程序必须很好地隐藏它自己。系统里的lkm是用单向链表连接起来的, 为了隐藏lkm本身我们必须把它从链表中移走以至于lsmod这样的命令不能把它显示出来。 
  2) 隐藏符号表
  通常的lkm中的函数将会被导出以至于其他模块可以使用它。因为我们是入侵者, 所以隐藏这些符号是必须的。幸运的是, 有一个宏可以供我们使用："EXPORT_NO_SYMBOLS"。 把这个宏放在lkm的最后可以防止任何符号的输出