Title: Windows&Linux环境的痕迹清理
Date: 2018-06-09 03:20
Modified: 2018-06-09 03:20
Category: 安全
Tags: 安全
Slug: O11
Authors: nJcx
Summary: Windows&Linux环境的痕迹清理~


渗透使用跳板已经是默认的了，那么最小化攻击日志，也是必须的。你是VPN也好，3389也罢，ssh中转，代理都行。直接连接攻击目标并且留下大量日志，是愚蠢的

#### Windows 痕迹清理



#### Linux痕迹清理


```bash

[root@localhost root]# echo > /var/log/wtmp //此文件默认打开时乱码，可查到ip等信息
[root@localhost root]# last //此时即查不到用户登录信息

[root@localhost root]# echo > /var/log/btmp //此文件默认打开时乱码，可查到登陆失败信息
[root@localhost root]# lastb //查不到登陆失败信息


[root@localhost root]# history -c //清空历史执行命令
修改/etc/profile，把HISTSIZE改为想记录的条数
[root@localhost root]# echo > ./.bash_history //或清空用户目录下的这个文件即可


[root@localhost root]# vi /root/history //新建记录文件
[root@localhost root]# history -c //清除记录 
[root@localhost root]# history -r /root/history.txt //导入记录 
[root@localhost root]# history //查询导入结果


清空命令记录

1）echo "'" > log.txt
2）echo > log.txt ，这种文件里会存在空格
3）cat /dev/null > log.txt



不记录历史命令
unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG;

export HISTFILE=/dev/null;

export HISTSIZE=0;

export HISTFILESIZE=0


此方法仅在交互的shell中有效，并且会使上下箭头重复最近命令这功能失效。还有一种方法就是在进入主机的时候就备份一下.bash_history，当退出的时候就把备份的文件还原一下。



一般需要清理的日志有：lastlog、utmp(utmpx)、wtmp(wtmpx)、messages、syslog、sulog

web日志的清理：access.log 和auth.log 位置在/var/log/

shell记录：.sh_history(ksh)，.history(csh)，或.bash_history(bash)等



```