Title: ossec 学习记录
Date: 2017-05-27 12:20
Modified: 2017-05-27 12:20
Category: 安全
Tags: ossec
Slug: H14
Authors: nJcx
Summary: 记录一下学习ossec 心路~

#### 介绍



#### 安装


ip : 192.168.1.100  server

ip ： 192.168.1.101  agent 

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
├── agentless
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
│   └── shared   //cis安全基线目录
│       ├── acsc_office2016_rcl.txt
│       ├── cis_apache2224_rcl.txt
│       ├── cis_debianlinux7-8_L2_rcl.txt
│       └── win_malware_rcl.txt
├── logs   //日志目录
│   └── ossec.log
├── lua      //lua插件
│   ├── compiled
│   └── native
├── queue
│   ├── alerts
│   ├── diff
│   ├── ossec
│   ├── rids
│   └── syscheck
├── tmp
└── var
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
├── agentless
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
│   └── shared   // cis安全基线目录
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
├── queue
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
└── var
    └── run

```