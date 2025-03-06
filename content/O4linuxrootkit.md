Title: Linux环境下的Rootkit技术细节
Date: 2022-06-20 20:20
Modified: 2022-06-20 20:20
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

Linux Rootkit 主要分为两种，一种是用户态的rootkit，一种是内核态的rootkit. Rootkit 主要的目的干坏事且隐藏自己，像个鬼影，隐藏自身的文件、进程、网络连接、rootkit模块本身。用户态的rootkit主要是替换相关命令完成(通过替换ps、top、ls、ss、netstat等系统工具)，内核态的rootkit主要是可装载内核模块（LKM）实现。

 


内核态的rootkit，我们主要靠挂钩hook技术来实现，系统调用hook，函数api hook，还有一种，直接内核对象操作系统，主要通过/dev/mem、/dev/kmem设备直接操作内存，从而对内核进行修改
    
    
 
当某个程序需要借助网络、文件系统或其他系统特定活动进行工作时，它就必须经过内核。也就是说，在此时它将使用系统调用。我们使用了一个名为Strace的工具。Strace将会列出程序所使用的系统调用。

```bash
# yum -y install strace
#cd /bin && strace ls 

ioctl(1, TIOCGWINSZ, 0x7ffedb86fcd0)    = -1 ENOTTY (Inappropriate ioctl for device)
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
getdents(3, /* 1036 entries */, 32768)  = 32744
brk(NULL)                               = 0xc6f000
brk(0xc99000)                           = 0xc99000
brk(NULL)                               = 0xc99000
brk(NULL)                               = 0xc99000
brk(0xc90000)                           = 0xc90000
brk(NULL)                               = 0xc90000
mmap(NULL, 311296, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f60ea4a8000
getdents(3, /* 32 entries */, 32768)    = 1096
getdents(3, /* 0 entries */, 32768)     = 0

```
我们需要关注的系统调用是getdents函数。




 

可装载内核模块（LKM）
在Linux系统中，如果我们想在内核中运行代码，我们可以借助于可装载内核模块（LKM）。本文将不会花用太多篇幅阐述它是如何工作的，大家可以参考这一篇文章（链接）。我们的思路是将自定义的模块加载到内核。一些有用的内核符号就会被内核导出，我们便能够去使用它们，或者也可以通过kallsyms_lookup_name函数来获取。在内核中，我们需要拦截getdents调用，并对它返回的值进行更改。此外，我们也希望可以稍微隐藏一下自己的行为，由于该模块是在系统中，因此就不会那么明显。

那么，接下来要解决的问题就是我们要如何Hook getdents，以及Linux内核会如何响应系统调用。

 

系统调用表
在内核之中，存在一个系统调用表。其中的系统调用编号（系统调用发生时rax的值）是其Handler在其表中的偏移量。在Windows系统中，由于PatchGuard内核保护系统的存在，系统调用表是无法接触到的。但在Linux系统中，我们就可以避开它。

需要注意的是，如果我们将系统调用表弄乱，将会造成非常严重的问题，这样的PoC无疑是愚蠢的，所以还是要考虑将Hook放置在其他地方。

系统调用表位于sys_call_table，它是系统内核的一块区间，其作用是将调用号和服务连接起来，当系统调用某一个进程时，就会通过sys_call_table查找到该程序。然而，它并不是一个可导出并供使用的Linux内核符号，因此，我们有下面这4种方式可供选择：

暴力搜索。这种方式更适用于32位系统上，但在64位系统上也是理论上可行的。
找到使用系统调用表的函数。有几个使用sys_call_table符号的函数，如果我们通过这些函数进行解析，就可以找到它们的引用。
在其他地方寻找。其实，如果不在内核中寻找，也是非常容易找到的。
不使用系统调用表。这是一个最好的方案，如果我们不在系统调用表上Hook，我们还可以将Hook放在Handler上。
针对这个简单的模块，我们会选择上面的第3种方式。不使用系统调用表的方式也比较有趣，我将会在后续另写一篇文章进行讲解。对于第3种方式，我们只需要读取并分析/boot/System.map-$(uname -r)文件即可。我们的这一操作，可以在将自身添加到内核的同时进行，由此就确保会得到正确的地址。在我的代码中，build_and_install.sh进行了这项工作。我生成了一个将使用可装载内核模块（LKM）编译的头文件。

smap="/boot/System.map-$(uname -r)"
echo -e "#pragma once" &gt; ./sysgen.h
echo -e "#include <linux/fs.h>" >> ./sysgen.h
symbline=$(cat $smap | grep '\Wsys_call_table$')
set $symbline
echo -e "void** sys_call_table = (void**)0x$1;" >> ./sysgen.h
 

关于Hook
系统调用表是只读的，但当我们在内核中的时候，这并不会成为较大的阻碍因素。在内核中，CR0是一个控制寄存器，可以修改处理器的操作方式。其中的第16位是写保护标志所在的位置，如果该标志为0，CPU就可以让内核写入只读页。Linux为我们提供了两个很有帮助的函数，可以用于修改CR0寄存器，分别是write_cr0和read_cr0。

在我的代码中，我通过 write_cr0(read_cr0() & (~WRITE_PROTECT_FLAG)); 关闭了写保护机制，随后在 #define WRITE_PROTECT_FLAG (1<<16)通过 write_cr0(read_cr0() | WRITE_PROTECT_FLAG)；将其重新打开。

随后，将当前getdents Handler的入口保存，这样我就可以在删除模块时恢复原样。之后，我们使用 sys_call_table[GETDENTS_SYSCALL_NUM] = sys_getdents_new;写了一个新的Handler。

其中的sys_getdents_new函数，只负责运行原始处理程序，并检查其结果，删除任何以我们指定前缀开头或是与我们模块有关的条目。

 

从/proc/modules实现隐藏
在Linux系统中，/proc/文件系统作为用户空间与内核之间的接口。它们并不是传统意义上的文件，在打开、写入或读取proc文件时，它会调用内核中的处理程序，动态地得到所需信息并进行相应操作。通过Hook /proc/modules文件的Read Handler，我们可以筛选出任何引用到我们模块的相应行。为了实现这一点，首先需要知道/proc/modules在内核中注册的位置。

我在Github上搜索了“proc_create(“modules”)“的源代码，并找到了以下几行：

static int __init proc_modules_init(void){

proc_create("modules", 0, NULL, &proc_modules_operations);

return 0;

}
由此看来，proc_modules_operations是一个包含Handler函数的结构。尽管它并不是一个导出的符号，但我们已经在使用System.map文件了，就不妨再使用一次它。

一旦它被导入，放置Hook的过程就会非常简单，proc_modules_operations->read = proc_modules_read_new;。在proc_modules_read_new中，我们还进行和之前一样的读取，并筛选出我们需要的相应行。

 

结论
至此，我们就拥有了第一个Linux rootkit。此后，我们还可以通过在系统调用表之外进行Hook，以及通过在内核中隐藏模块来改进。

希望上述内容已经讲解得足够清楚明白，如果大家有任何问题，或者发现我的代码中存在任何Bug，请随时提出。我也期待能有更多人提出Rootkit方面的更深入分析并相互学习。







   
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
  