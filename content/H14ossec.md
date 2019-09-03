Title: ossec 搭建与简单用法
Date: 2017-05-27 12:20
Modified: 2017-05-27 12:20
Category: 安全
Tags: ossec
Slug: H14
Authors: nJcx
Summary: 记录一下学习ossec 心路~
Status: draft


#### 介绍
OSSEC是一款开源的hids，可以运行于Windows, Linux, OpenBSD/FreeBSD, 以及 MacOS等操作系统中。包括日志分析，全面检测，root-kit检测，审计，实时报警以及联动响应等功能。

#### 安装


ip : 192.168.1.100   // server

ip ： 192.168.1.101  // agent 

涉及端口 ： 514，1514，48658  //注意防火墙

在192.168.1.101上安装server ，安装目录/opt/ossec

```bash

# curl -Ls https://github.com/ossec/ossec-hids/archive/3.1.0.tar.gz | tar zx 
# cd ossec-hids-3.1.0/ && sh install.sh

```

填写语言，然后选择server类型，填写smtp服务器，填写安装目录，即可编译安装完成

```bash
#/opt/ossec/bin/ossec-control start  //启动server
#/opt/ossec/bin/ossec-control stop   //停止server
```

在192.168.1.101上安装agent：
 
```bash

# curl -Ls https://github.com/ossec/ossec-hids/archive/3.1.0.tar.gz | tar zx 
# cd ossec-hids-3.1.0/ && sh install.sh

```

填写语言，然后选择agent类型，填写安装目录，server地址，等等，即可编译安装完成

```bash
#/opt/ossec/bin/ossec-control start  //启动agent
#/opt/ossec/bin/ossec-control stop   //停止agent
```


#### 目录结构

agent 目录结构

```bash

── active-response   //联动模块目录
│   └── bin 
│       ├── disable-account.sh
│       ├── firewalld-drop.sh
│       ├── firewall-drop.sh
│       ├── host-deny.sh
│       ├── ip-customblock.sh
│       ├── ipfw_mac.sh
│       ├── ipfw.sh
│       ├── npf.sh
│       ├── ossec-pagerduty.sh
│       ├── ossec-slack.sh
│       ├── ossec-tweeter.sh
│       ├── pf.sh
│       ├── restart-ossec.sh
│       └── route-null.sh
├── agentless  //无代理监控
│   ├── main.exp
│   ├── register_host.sh
│   ├── ssh_asa-fwsmconfig_diff
│   ├── ssh.exp
│   ├── ssh_foundry_diff
│   ├── ssh_generic_diff
│   ├── ssh_integrity_check_bsd
│   ├── ssh_integrity_check_linux
│   ├── sshlogin.exp
│   ├── ssh_nopass.exp
│   ├── ssh_pixconfig_diff
│   └── su.exp
├── bin  //可执行文件目录
│   ├── agent-auth
│   ├── manage_agents
│   ├── ossec-agentd
│   ├── ossec-control
│   ├── ossec-execd
│   ├── ossec-logcollector
│   ├── ossec-lua
│   ├── ossec-luac
│   ├── ossec-syscheckd
│   └── util.sh
├── etc    //配置目录
│   ├── client.keys
│   ├── internal_options.conf
│   ├── local_internal_options.conf
│   ├── localtime
│   ├── ossec.conf
│   ├── ossec-init.conf
│   └── shared   //cis安全基线/特征库
│       ├── acsc_office2016_rcl.txt
│       ├── cis_apache2224_rcl.txt
│       ├── cis_debianlinux7-8_L2_rcl.txt
│       └── win_malware_rcl.txt
├── logs   //日志目录
│   └── ossec.log
├── lua      //lua插件
│   ├── compiled
│   └── native
├── queue  //队列
│   ├── alerts
│   ├── diff
│   ├── ossec
│   ├── rids
│   └── syscheck
├── tmp   // 临时文件目录
└── var  //存放pid
    └── run
    
```

server 的目录结构

```bash

├── active-response    // 联动模块
│   └── bin
│       ├── disable-account.sh
│       ├── firewalld-drop.sh
│       ├── firewall-drop.sh
│       ├── host-deny.sh
│       ├── ip-customblock.sh
│       ├── ipfw_mac.sh
│       ├── ipfw.sh
│       ├── npf.sh
│       ├── ossec-pagerduty.sh
│       ├── ossec-slack.sh
│       ├── ossec-tweeter.sh
│       ├── pf.sh
│       ├── restart-ossec.sh
│       └── route-null.sh
├── agentless //无代理监控
│   ├── main.exp
│   ├── register_host.sh
│   ├── ssh_asa-fwsmconfig_diff
│   ├── ssh.exp
│   ├── ssh_foundry_diff
│   ├── ssh_generic_diff
│   ├── ssh_integrity_check_bsd
│   ├── ssh_integrity_check_linux
│   ├── sshlogin.exp
│   ├── ssh_nopass.exp
│   ├── ssh_pixconfig_diff
│   └── su.exp
├── bin    // 可执行文件目录
│   ├── agent_control
│   ├── clear_stats
│   ├── list_agents
│   ├── manage_agents
│   ├── ossec-agentlessd
│   ├── ossec-analysisd
│   ├── ossec-authd
│   ├── ossec-control
│   ├── ossec-csyslogd
│   ├── ossec-dbd
│   ├── ossec-execd
│   ├── ossec-logcollector
│   ├── ossec-logtest
│   ├── ossec-lua
│   ├── ossec-luac
│   ├── ossec-maild
│   ├── ossec-makelists
│   ├── ossec-monitord
│   ├── ossec-regex
│   ├── ossec-remoted
│   ├── ossec-reportd
│   ├── ossec-syscheckd
│   ├── rootcheck_control
│   ├── syscheck_control
│   ├── syscheck_update
│   ├── util.sh
│   └── verify-agent-conf
├── etc     // 配置目录
│   ├── client.keys
│   ├── decoder.xml
│   ├── internal_options.conf
│   ├── local_internal_options.conf
│   ├── localtime
│   ├── ossec.conf
│   ├── ossec-init.conf
│   └── shared   //cis安全基线/特征库
│       ├── acsc_office2016_rcl.txt
│       ├── cis_mysql5-6_community_rcl.txt
│       ├── cis_mysql5-6_enterprise_rcl.txt
│       ├── rootkit_files.txt
│       └── win_malware_rcl.txt
├── logs   // 日志目录
│   ├── active-responses.log
│   ├── alerts
│   ├── archives
│   ├── firewall
│   └── ossec.log
├── lua   //lua插件
│   ├── compiled
│   └── native
├── queue  //队列
│   ├── agent-info
│   ├── agentless
│   ├── alerts
│   ├── diff
│   ├── fts
│   ├── ossec
│   ├── rids
│   ├── rootcheck
│   └── syscheck
├── rules    // 规则存放目录
│   ├── apache_rules.xml
│   ├── mysql_rules.xml
│   ├── nginx_rules.xml
│   ├── ossec_rules.xml
│   ├── php_rules.xml
│   └── zeus_rules.xml
├── stats  
├── tmp
└── var  // 存放pid 文件
    └── run

```

#### 添加agent

先启动 server端

```bash
#/opt/ossec/bin/ossec-control start 

```
server 端会启动6个进程


```bash
Started ossec-execd...
Started ossec-analysisd...
Started ossec-logcollector...
Started ossec-remoted...
Started ossec-syscheckd...
Started ossec-monitord...

```


server添加agent

这里，先输入A添加，再输入E，导出KEY备用

```bash
#/opt/ossec/bin/manage_agents

```

```bash

[root@localhost bin]# ./manage_agents 

****************************************
* OSSEC HIDS v3.1.0 Agent manager.     *
* The following options are available: *
****************************************
   (A)dd an agent (A).
   (E)xtract key for an agent (E).
   (L)ist already added agents (L).
   (R)emove an agent (R).
   (Q)uit.
Choose your action: A,E,L,R or Q: A

- Adding a new agent (use '\q' to return to the main menu).
  Please provide the following:
   * A name for the new agent: 001
   * The IP Address of the new agent: 172.16.131.128
   * An ID for the new agent[001]: 001
Agent information:
   ID:001
   Name:001
   IP Address:192.168.1.101

Confirm adding it?(y/n): y
Agent added.


****************************************
* OSSEC HIDS v3.1.0 Agent manager.     *
* The following options are available: *
****************************************
   (A)dd an agent (A).
   (E)xtract key for an agent (E).
   (L)ist already added agents (L).
   (R)emove an agent (R).
   (Q)uit.
Choose your action: A,E,L,R or Q: E

Available agents:
   ID: 001, Name: 001, IP: 192.168.1.101
Provide the ID of the agent to extract the key (or '\q' to quit): 001

Agent key information for '001' is:
MDAxIDAwMSAxNzIuMTYuMTMxLjEyOCA4OTU0YTE5YTEzY2Q3MWQzMDFiNzVlZjA3YWRiN2NlNjQ0NzI2NWYxNjdjNzMzMTQ4ZjAzYmJjYTgyNzJmNDRl

** Press ENTER to return to the main menu.

```

然后启动 agent端

```bash
#/opt/ossec/bin/ossec-control start 

```
agent 端会启动4个进程

```bash
Started ossec-execd...
Started ossec-agentd...
Started ossec-logcollector...
Started ossec-syscheckd...
```
在这里输入I，导入server端的KEY

```bash
[root@localhost bin]# /opt/ossec/bin/manage_agents


****************************************
* OSSEC HIDS v3.1.0 Agent manager.     *
* The following options are available: *
****************************************
   (I)mport key from the server (I).
   (Q)uit.
Choose your action: I or Q: I

* Provide the Key generated by the server.
* The best approach is to cut and paste it.
*** OBS: Do not include spaces or new lines.

Paste it here (or '\q' to quit): MDAxIDAwMSAxNzIuMTYuMTMxLjEyOCA4OTU0YTE5YTEzY2Q3MWQzMDFiNzVlZjA3YWRiN2NlNjQ0NzI2NWYxNjdjNzMzMTQ4ZjAzYmJjYTgyNzJmNDRl

Agent information:
   ID:001
   Name:001
   IP Address:192.168.1.101

Confirm adding it?(y/n): y
Added.
** Press ENTER to return to the main menu.

```
当然，我们也可以用server 的 ossec-authd 工具添加key

```bash

server #/opt/ossec/bin/ossec-authd -p 1515

agent  #/opt/ossec/bin/agent-auth -m 192.168.1.100 -p 1515

```
这样也可以实现添加agent


通过 netstat -anlp | grep ossec ，可以查看agent（48658端口）与server （1514）通过udp通讯

```bash

192.168.1.101:48658    192.168.1.100:1514

```

#### 使用说明

- Log monitoring/analysis   进程和log监控

进程和log的监控，agent默认就是启用的，也就是说agent只要启动了，就会向server发采集到的内容,由server的规则判断是否异常，agent的配置项决定怎么发送，OSSEC日志检测为实时检测，所监控的日志会通过1514端口发送到服务端。


- Syscheck    系统完整性检测

命令替换在应急响应中很常见，经常被替换掉的命令例如ps、netstat、ss、lsof等等。另外还有SSH后门。完整性检测的工作方式是Agent周期性的扫描系统文件，并将检验和发送给Server端。Server端存储并进行比对，发现修改是发出告警。OSSEC通过查找系统中关键文件的md5/sha1校验和的变化来完成这一工作。默认情况下每6个小时，但频率或时间/日是可配置的。


- Rootcheck    rootkit 检测

在 /opt/ossec/etc/shared目录下面，存在该文件rootkit_files.txt，该文件中包含了rootkit常用的文件名

```bash

# Blank lines and lines starting with '#' are ignored.
#
# Each line must be in the following format:
# file_name ! Name ::Link to it
#
# Files that start with an '*' will be searched in the whole system.

# Volc Rootkit
usr/lib/volc            ! Volc Rootkit ::
usr/bin/volc            ! Volc Rootkit ::

# Illogic
lib/security/.config    ! Illogic Rootkit ::rootkits/illogic.php
usr/bin/sia             ! Illogic Rootkit ::rootkits/illogic.php
etc/ld.so.hash          ! Illogic Rootkit ::rootkits/illogic.php
*/uconf.inv             ! Illogic Rootkit ::rootkits/illogic.php

# T0rnkit
usr/src/.puta           ! t0rn Rootkit ::rootkits/torn.php
usr/info/.t0rn          ! t0rn Rootkit ::rootkits/torn.php
lib/ldlib.tk            ! t0rn Rootkit ::rootkits/torn.php
etc/ttyhash             ! t0rn Rootkit ::rootkits/torn.php
```
对比rootkit_trojans.txt文件中二进制文件特征。

```bash

# Blank lines and lines starting with '#' are ignored.
#
# Each line must be in the following format:
# file_name !string_to_search!Description

# Common binaries and public trojan entries
ls          !bash|^/bin/sh|dev/[^clu]|\.tmp/lsfile|duarawkz|/prof|/security|file\.h!
env         !bash|^/bin/sh|file\.h|proc\.h|/dev/|^/bin/.*sh!
echo        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
chown       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
chmod       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
chgrp       !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
cat         !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cl]|^/bin/.*sh!
bash        !proc\.h|/dev/[0-9]|/dev/[hijkz]!
sh          !proc\.h|/dev/[0-9]|/dev/[hijkz]!
uname       !bash|^/bin/sh|file\.h|proc\.h|^/bin/.*sh!
date        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^cln]|^/bin/.*sh!
du          !w0rm|/prof|file\.h!

```
agent扫描整个文件系统，检测异常文件和异常的权限设置，文件属主是root，但是其他用户可写是非常危险的，rootkit将会扫描这些文件。同时还会检测具有suid权限的文件、隐藏的文件和目录。另外还会检测隐藏端口、隐藏进程、/dev目录、网卡混杂模式等。rootkit的检测配置如下：

```bash
  <rootcheck>
    <rootkit_files>/root/ossec/etc/shared/rootkit_files.txt</rootkit_files>
    <rootkit_trojans>/root/ossec/etc/shared/rootkit_trojans.txt</rootkit_trojans>
    <system_audit>/root/ossec/etc/shared/system_audit_rcl.txt</system_audit>
    <system_audit>/root/ossec/etc/shared/cis_debian_linux_rcl.txt</system_audit>
    <system_audit>/root/ossec/etc/shared/cis_rhel_linux_rcl.txt</system_audit>
    <system_audit>/root/ossec/etc/shared/cis_rhel5_linux_rcl.txt</system_audit>
  </rootcheck>
  
```
测试一下，agent在tmp下面创建一个文件

```bash

touch /tmp/mcliZokhb

```

然后在服务端

```bash

/opt/ossec/bin/agent_control -r -u 001

```
```bash

cat /opt/ossec/queue/rootcheck/*

```
可以看到

```bash
!1499925300!1499150323 Starting rootcheck scan.

!1499925927!1499150951 Ending rootcheck scan.

!1499925300!1499925300 Rootkit 'Bash' detected by the presence of file '/tmp/mcliZokhb'.

```
在报警日志中可以看到，
tail -f alerts.log

```bash

[root@ossec_server alerts]# tail -f alerts.log
** Alert 1544505860.0: mail  - ossec,rootcheck,
2018 Dec 11 00:24:20 (001) 172.16.131.142->rootcheck
Rule: 510 (level 7) -> 'Host-based anomaly detection event (rootcheck).'
Rootkit 'Bash' detected by the presence of file '/tmp/mcliZokhb'.

```

#### 添加规则

```bash
https://ossec-docs.readthedocs.io/en/latest/syntax/head_rules.html

https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html
```

添加了一个

```bash

<rule id="100002" level="8">
      <if_sid>18104</if_sid>
      <srcip>!127.0.0.1</srcip>
      <srcip>!172.16.131.1</srcip>
      <description>login from Unknow Host</description>
      <group>authentication_success</group>
 </rule>

```

#### 告警输出

以下配置都在 server端的 /opt/ossec/etc/ossec.conf 改动添加

- syslog 

```bash
<syslog_output>
  <server>10.10.10.127</server>
  <port>515</port>
  <level>6</level>
</syslog_output>
```

```bash
#/opt/ossec/bin/ossec-control enable client-syslog
#/opt/ossec/bin/ossec-control restart
```

- 告警E-mail发送

先配置smtp 服务器

```bash
    <global>
        <email_notification>yes</email_notification>
        <email_to>me@example.com</email_to>
        <smtp_server>mx.example.com..</smtp_server>
        <email_from>ossec@example.com</email_from>
  </global>
```
再配置收件人，触发条件

```bash
<email_alerts>
    <email_to>bb@y.z</email_to>
    <rule_id>123, 124</rule_id>
    <do_not_delay />
    <do_not_group />
</email_alerts>
```

然后重启服务端

```bash
#/opt/ossec/bin/ossec-control restart

```

- json


输出到json

```bash

<ossec_config>
  <global>
    <jsonout_output>yes</jsonout_output>
    ...
  </global>
  ...
</ossec_config>

```
然后重启服务端

```bash
#/opt/ossec/bin/ossec-control restart

```

- 输出到MySQL数据库

```bash

/opt/ossec/bin/ossec-control enable database

```

```bash

<ossec_config>
    <database_output>
        <hostname>192.168.2.30</hostname>
        <username>ossecuser</username>
        <password>ossecpass</password>
        <database>ossec</database>
        <type>mysql</type>
    </database_output>
</ossec_config>

```
其中表结构在 ossec-hids-3.1.0/src/os_dbd 下面

```bash
# mysql -u root -p

mysql> create database ossec;

mysql> grant INSERT,SELECT,UPDATE,CREATE,DELETE,EXECUTE on ossec.* to ossecuser@<ossec ip>;
Query OK, 0 rows affected (0.00 sec)

mysql> set password for ossecuser@<ossec ip>=PASSWORD('ossecpass');
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> quit

# mysql -u root -p ossec < mysql.schema

```
重启服务端
```bash
/opt/ossec/bin/ossec-control restart
```

#### 联动模块

/opt/ossec/etc/ossec.conf中相应配置如下,在当rule级别大于等于5时触发，封禁时间为60S

```bash

  <command>

    <name>host-deny</name>

    <executable>host-deny.sh</executable>

    <expect>srcip</expect>

    <timeout_allowed>yes</timeout_allowed>

  </command>
  
  

  <active-response>

    <command>host-deny</command>

    <location>local</location>

    <level>5</level>

    <timeout>30</timeout>

  </active-response>
  
```


#### 常用命令


```bash

# /opt/ossec/bin/agent_control -R 001   //server重启agent程序（仅仅是程序，不是机器，001是agent的编号) 

```


