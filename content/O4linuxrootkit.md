Title: Linux环境下的Rootkit技术细节
Date: 2022-09-20 20:20
Modified: 2022-09-20 20:20
Category: 安全
Tags: Linux
Slug: O4
Authors: nJcx
Summary: Linux环境下的Rootkit技术细节~

#### 安装

```bash
https://github.com/f0rb1dd3n/Reptile.git
https://github.com/yaoyumeng/adore-ng.git
https://github.com/citypw/suterusu.git
https://github.com/m0nad/Diamorphine.git
https://github.com/unix-thrust/beurk.git
https://github.com/mempodippy/vlany.git
https://github.com/hanj4096/wukong.git
https://github.com/ldpreload/Medusa.git
https://github.com/mav8557/Father.git
https://github.com/imlk0/yark.git

```

linux rootkit 主要分为两种，一种是用户态的rootkit，一种是内核态的rootkit。rootkit的主要目的是为了隐蔽地获取对操作系统的控制权或访问权限，同时尽量避免被检测到。用户态的rootkit主要是动态链接库（LD_PRELOAD）注入，通过设置环境变量 LD_PRELOAD 来加载恶意的共享库。这种方法可以拦截并修改标准库函数的行为，例如文件操作、网络通信等，从而隐蔽地执行某些操作，还有替换相关系统命令完成(通过替换ps、top、ls、ss、netstat等系统工具)。内核态的rootkit主要是可装载内核模块（LKM）实现， 主要是修改操作系统的核心部分，修改内部的数据结构或者进行系统函数HOOK，以此来隐藏其存在，例如隐藏特定的文件、进程和网络连接等。


无论是用户态rootkit还是内核的rootkit，都会把隐藏自己，作为核心功能存在， 都会有下面4个核心功能点，只是实现的方法，各有不同。
 
-  隐藏文件

-  隐藏进程

-  隐藏网络连接状态

-  隐藏rootkit模块本身。


#### 用户态动态链接库（LD_PRELOAD）注入

LD_PRELOAD 是 Linux 环境下的一个环境变量，它允许用户指定在程序运行前优先加载的动态链接库（shared object）。通过这种方式，可以实现函数劫持（hook），即替换或增强某些函数的功能。这在调试、性能分析以及安全领域非常有用。当你设置 LD_PRELOAD 并运行一个程序时，Linux 动态链接器会首先加载由 LD_PRELOAD 指定的共享库中的符号（functions, variables等），然后才去加载其他依赖的库。这意味着你可以定义与标准库中同名的函数，在你的共享库中实现自定义逻辑，并在调用原版函数之前或之后执行额外的操作，或者完全替代它们。


实现方法：

- 编写共享库：首先，你需要编写一个共享库，其中包含你想要hook的函数的实现。
- 编译共享库：使用 -fPIC 和 -shared 标志来编译你的代码，生成一个共享对象文件（.so）。
- 设置 LD_PRELOAD：在运行目标程序之前，通过设置 LD_PRELOAD 环境变量指向你的共享库，如 export LD_PRELOAD=/path/to/your/library.so。

运行程序：当程序运行时，动态链接器将首先加载你指定的库，从而覆盖或添加原有函数的行为。

一个简单的例子来展示如何使用 LD_PRELOAD 来 hook 标准库中的 puts 函数。这个例子将拦截对 puts 的调用，并在实际调用之前打印一条自定义消息。

```bash

#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>

// 原始的 puts 函数指针
static int (*original_puts)(const char*) = NULL;

int puts(const char *s) {
    // 如果这是第一次调用，则获取原始的 puts 函数地址
    if (!original_puts) {
        original_puts = dlsym(RTLD_NEXT, "puts");
    }

    printf("Intercepted call to puts with argument: %s\n", s);
    
    // 调用原始的 puts 函数
    return original_puts(s);
}


```

```bash
gcc -shared -fPIC -o demo.so demo.c -ldl

-shared 表示生成共享库。
-fPIC 生成与位置无关的代码，这对于共享库是必需的。
-ldl 链接 libdl 库，用于动态加载符号。

```

测试程序 test_program.c 如下：

```bash

#include <stdio.h>

int main() {
    puts("Hello, World!");
    return 0;
}


gcc -o test_program test_program.c


export LD_PRELOAD=$PWD/demo.so
./test_program


```


```bash

Intercepted call to puts with argument: Hello, World!
Hello, World!

```


文件隐藏

	HOOK open、opendir、readdir等函数， 隐藏特定文件名
	
	

进程隐藏

	HOOK ps、top等命令相关的函数调用， 通常HOOK readdir、getdents函数来隐藏特定进程
	



这段代码是一个自定义的 readdir 函数，用于过滤特定进程的目录项。主要功能如下：

- 初始化原始 readdir 函数指针。
- 进入循环读取目录项。
- 如果目录为 /proc 且进程名匹配，则跳过该目录项。
- 返回非过滤的目录项。

	
```bash
struct dirent* readdir(DIR *dirp)                                       
{                                                                       
    if(original_##readdir == NULL) {                                    
        original_##readdir = dlsym(RTLD_NEXT, #readdir);               
        if(original_##readdir == NULL)                                  
        {                                                              
            fprintf(stderr, "Error in dlsym: %s\n", dlerror());         
        }                                                               
    }                                                                   
                                                                        
    struct dirent* dir;                                                 
                                                                        
    while(1)                                                            
    {                                                                   
        dir = original_##readdir(dirp);                                 
        if(dir) {                                                       
            char dir_name[256];                                         
            char process_name[256];                                     
            if(get_dir_name(dirp, dir_name, sizeof(dir_name)) &&        
                strcmp(dir_name, "/proc") == 0 &&                       
                get_process_name(dir->d_name, process_name) &&          
                strcmp(process_name, process_to_filter) == 0) {         
                continue;                                               
            }                                                           
        }                                                               
        break;                                                          
    }                                                                   
    return dir;                                                         
}


```


网络连接隐藏

	HOOK netstat命令的相关函数调用， 一般会HOOK readdir/getdents来隐藏特定端口的连接






#### 内核态可装载内核模块（LKM）


内核态的rootkit主要是可装载内核模块（LKM）实现， 主要是修改操作系统的核心部分，修改内部的数据结构或者进行系统函数HOOK。那么我们就聚焦关注两个点：修改哪些数据结构， 怎么HOOK与HOOK哪些函数。


##### 修改哪些数据结构



##### 怎么HOOK与HOOK哪些函数

当某个程序需要借助网络、文件系统或其他系统特定活动进行工作时，它就必须经过内核。也就是说，在此时它将使用系统调用。我们可以使用一个名为Strace的工具。Strace将会列出程序所使用的系统调用。

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


在Linux系统中，如果我们想在内核中运行代码，我们可以借助于可装载内核模块（LKM）。一些有用的内核符号就会被内核导出，我们便能够去使用它们，或者也可以通过kallsyms_lookup_name函数来获取。在内核中，我们需要拦截getdents调用，并对它返回的值进行更改。那么，接下来要解决的问题就是我们要如何Hook getdents。


在内核之中，存在一个系统调用表。其中的系统调用编号（系统调用发生时rax的值）是其Handler在其表中的偏移量。
系统调用表位于sys_call_table，它是系统内核的一块区间，其作用是将调用号和服务函数连接起来，当系统调用某一个syscall，就会通过sys_call_table查找到该服务函数。
 