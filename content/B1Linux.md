Title: Linux 运维常用命令总结
Date: 2017-01-13 10:20
Modified: 2017-01-13 10:20
Category: Linux
Tags: Linux
Slug: B1
Authors: nJcx
Summary: Linux 运维常用命令总结
## Linux 运维常用命令总结

很多都是从网上收集的和自己总结的
 
- 网卡绑定多IP

ifconfig eth0:1 192.168.1.99 netmask 255.255.255.0
 
- 设置DNS、网关

echo "nameserver 202.16.53.68" >> /etc/resolv.conf
route add default gw 192.168.1.1
 
- 查看系统版本

lsb_release -a

cat /etc/issue

- 查看系统信息

uname -a

- 查看物理CPU个数

cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
 
 - 查看当前登录用户:
 
root@debian:/home/njcx# who

njcx     :0           2017-05-21 08:11 (:0)

njcx     pts/0        2017-05-21 18:24 (:0.0)

第一列是用户名,
第二列是连接的终端,tty表示显示器,pts表示远程连接,
第三列是登陆时间,

- 查看登录用户行为:
root@debian:/home/njcx# w

 18:32:52 up 10:21,  2 users,  load average: 0.74, 0.35, 0.23
 
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

njcx     :0       :0               08:11   ?xdm?  38:14   0.31s x-session-manag

njcx     pts/0    :0.0             18:24    1.00s  0.09s  3.44s mate-terminal

users 表示当前系统登陆用户总数为2。

LOAD AVERAGE 与后面的数字一起表示系统在过去1，5，10分钟内的负载程度，数值越小，系统负载越轻。

从第二行开始构成一个表格，共有8个栏目，分别显示各个用户正在做的事情及该用户所占用的系统资料。

USER：显示登陆用户帐号名。用户重复登陆，该帐号也会重复出现。

TTY：用户登陆所用的终端。

FROM：显示用户在何处登陆系统。

LOGIN@：是LOGIN AT的意思，表示登陆进入系统的时间。

IDLE：用户空闲时间，从用户上一次任务结束后，开始记时。

JCPU：一终端代号来区分，表示在某段时间内，所有与该终端相关的进程任务所耗费的CPU时间。

PCPU：指WHAT域的任务执行后耗费的CPU时间。

WHAT：表示当前执行的任务

当登陆系统用户很多的时候，可以在W后面加上某个用户名，则会查看该用户执行任务的情况

- 强制踢出登陆用户

pkill -KILL -t pts/1
 
- tar命令

tar.gz

 压缩：tar -zcvf archive_name.tar.gz directory_to_compress
 
解压缩： tar -zxvf archive_name.tar.gz

tar.bz2

压缩  ： tar -jcvf test.tar.bz2 test

解压： tar -jxvf test.tar.bz2 
 
- 将本地80端口的请求转发到8080端口，当前主机外网IP为202.96.85.46

A PREROUTING -d 202.96.85.46 -p tcp -m tcp --dport 80 -j DNAT --to-destination 192.168.9.10:8080

- 在11月份内，每天的早上6点到12点中，每隔2小时执行一次/usr/bin/httpd.sh

crontab -e

0 6-12/2 * 11 * /usr/bin/httpd.sh
 
- 查看占用端口8080的进程

netstat -tnlp | grep 8080

lsof -i:8080
 
- 在Shell环境下,如何查看远程Linux系统运行了多少时间?

ssh user@被监控主机ip "uptime"
 
- 查看CPU使用情况的命令

""每5秒刷新一次，最右侧有CPU的占用率的数据

vmstat 5

""top 然后按Shift+P，按照进程处理器占用率排序
top

- 查看磁盘空间占用情况

df -hl
 
- 查看内存使用情况的命令

""用free命令查看内存使用情况

free -m

""top 然后按Shift+M, 按照进程内存占用率排序

top
 
- 修复文件系统

fsck –yt ext3 /

-t 指定文件系统

-y 对发现的问题自动回答yes
 
- read 命令5秒后自动退出

read -t 5
 
- vi编辑器(涉及到修改，添加，查找)

插入(insert)模式

i　　　　光标前插入

I　　　　光标行首插入

a　　　　光标后插入

A　　　　光标行尾插入

o　　　　光标所在行下插入一行，行首插入

O　　　　光标所在行上插入一行，行首插入

G　　　　移至最后一行行首

nG　　　　移至第n行行首

n+　　　　下移n行，行首

n-　　　　上移n行，行首

:/str/　　　　　　　　　　从当前往右移动到有str的地方

:?str?　　　　　　　　　　从当前往左移动到有str的地方

:s/str1/str2/　　　　　　将找到的第一个str1替换为str2　
　
:s/str2/str2/g　　　　　　将当前行找到的所有str1替换为str2

:n1,n2s/str1/str2/g　　　　将从n1行至n2行找到的所有的str1替换为str2

:1,.s/str1/str2/g　　　　　　将从第1行至当前行的所有str1替换为str2

:.,$s/str1/str2/g　　　　　　将从当前行至最后一行的所有str1替换为str2

- linux服务器之间相互复制文件

copy 本地文件1.sh到远程192.168.9.10服务器的/data/目录下

scp /etc/1.sh king@192.168.9.10:/data/
 
copy远程192.168.9.10服务器/data/2.sh文件到本地/data/目录

scp king@192.168.9.10:/data/2.sh /data/
 

- 如何查看目标主机192.168.0.1开放那些端口

nmap -PS 192.168.0.1
 

- 如何查看当前系统使用了那些库文件

ldconfig -v
 
- 如何查看网卡的驱动版本

ethtool -i eth0
 
- 使用tcpdump来监视主机192.168.0.1的tcp的80端口

tcpdump tcp port 80 host 192.168.0.1                                               
 

 

