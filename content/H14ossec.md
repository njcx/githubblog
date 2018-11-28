Title: ossec 学习记录
Date: 2017-05-27 12:20
Modified: 2017-05-27 12:20
Category: 安全
Tags: ossec
Slug: H14
Authors: nJcx
Summary: 记录一下学习ossec 心路~

#### 问题


下载地址

ip : 192.168.1.100  server

ip ： 192.168.1.101  agent 

安装server ，安装目录/opt/ossec

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

填写语言，然后选择agent类型，填写安装目录，等等，即可编译安装完成

```bash
#/opt/ossec/bin/ossec-control start  //启动agent
#/opt/ossec/bin/ossec-control stop   //停止agent
```


#### 

agent 目录结构

```bash

── active-response
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
├── bin
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
├── etc
│   ├── client.keys
│   ├── internal_options.conf
│   ├── local_internal_options.conf
│   ├── localtime
│   ├── ossec.conf
│   ├── ossec-init.conf
│   └── shared
│       ├── acsc_office2016_rcl.txt
│       ├── cis_apache2224_rcl.txt
│       ├── cis_debianlinux7-8_L1_rcl.txt
│       ├── cis_debianlinux7-8_L2_rcl.txt
│       ├── cis_debian_linux_rcl.txt
│       ├── cis_mysql5-6_community_rcl.txt
│       ├── cis_mysql5-6_enterprise_rcl.txt
│       ├── cis_rhel5_linux_rcl.txt
│       ├── cis_rhel6_linux_rcl.txt
│       ├── cis_rhel7_linux_rcl.txt
│       ├── cis_rhel_linux_rcl.txt
│       ├── cis_sles11_linux_rcl.txt
│       ├── cis_sles12_linux_rcl.txt
│       ├── cis_win10_enterprise_L1_rcl.txt
│       ├── cis_win10_enterprise_L2_rcl.txt
│       ├── cis_win2012r2_domainL1_rcl.txt
│       ├── cis_win2012r2_domainL2_rcl.txt
│       ├── cis_win2012r2_memberL1_rcl.txt
│       ├── cis_win2012r2_memberL2_rcl.txt
│       ├── cis_win2016_domainL1_rcl.txt
│       ├── cis_win2016_domainL2_rcl.txt
│       ├── cis_win2016_memberL1_rcl.txt
│       ├── cis_win2016_memberL2_rcl.txt
│       ├── rootkit_files.txt
│       ├── rootkit_trojans.txt
│       ├── system_audit_rcl.txt
│       ├── system_audit_ssh.txt
│       ├── win_applications_rcl.txt
│       ├── win_audit_rcl.txt
│       └── win_malware_rcl.txt
├── logs
│   └── ossec.log
├── lua
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

.
├── active-response
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
├── bin
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
├── etc
│   ├── client.keys
│   ├── decoder.xml
│   ├── internal_options.conf
│   ├── local_internal_options.conf
│   ├── localtime
│   ├── ossec.conf
│   ├── ossec-init.conf
│   └── shared
│       ├── acsc_office2016_rcl.txt
│       ├── cis_apache2224_rcl.txt
│       ├── cis_debianlinux7-8_L1_rcl.txt
│       ├── cis_debianlinux7-8_L2_rcl.txt
│       ├── cis_debian_linux_rcl.txt
│       ├── cis_mysql5-6_community_rcl.txt
│       ├── cis_mysql5-6_enterprise_rcl.txt
│       ├── cis_rhel5_linux_rcl.txt
│       ├── cis_rhel6_linux_rcl.txt
│       ├── cis_rhel7_linux_rcl.txt
│       ├── cis_rhel_linux_rcl.txt
│       ├── cis_sles11_linux_rcl.txt
│       ├── cis_sles12_linux_rcl.txt
│       ├── cis_win10_enterprise_L1_rcl.txt
│       ├── cis_win10_enterprise_L2_rcl.txt
│       ├── cis_win2012r2_domainL1_rcl.txt
│       ├── cis_win2012r2_domainL2_rcl.txt
│       ├── cis_win2012r2_memberL1_rcl.txt
│       ├── cis_win2012r2_memberL2_rcl.txt
│       ├── cis_win2016_domainL1_rcl.txt
│       ├── cis_win2016_domainL2_rcl.txt
│       ├── cis_win2016_memberL1_rcl.txt
│       ├── cis_win2016_memberL2_rcl.txt
│       ├── rootkit_files.txt
│       ├── rootkit_trojans.txt
│       ├── system_audit_rcl.txt
│       ├── system_audit_ssh.txt
│       ├── win_applications_rcl.txt
│       ├── win_audit_rcl.txt
│       └── win_malware_rcl.txt
├── logs
│   ├── active-responses.log
│   ├── alerts
│   ├── archives
│   ├── firewall
│   └── ossec.log
├── lua
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
├── rules
│   ├── apache_rules.xml
│   ├── apparmor_rules.xml
│   ├── arpwatch_rules.xml
│   ├── asterisk_rules.xml
│   ├── attack_rules.xml
│   ├── cimserver_rules.xml
│   ├── cisco-ios_rules.xml
│   ├── clam_av_rules.xml
│   ├── courier_rules.xml
│   ├── dnsmasq_rules.xml
│   ├── dovecot_rules.xml
│   ├── dropbear_rules.xml
│   ├── exim_rules.xml
│   ├── firewalld_rules.xml
│   ├── firewall_rules.xml
│   ├── ftpd_rules.xml
│   ├── hordeimp_rules.xml
│   ├── ids_rules.xml
│   ├── imapd_rules.xml
│   ├── linux_usbdetect_rules.xml
│   ├── local_rules.xml
│   ├── mailscanner_rules.xml
│   ├── mcafee_av_rules.xml
│   ├── ms1016_usbdetect_rules.xml
│   ├── msauth_rules.xml
│   ├── ms_dhcp_rules.xml
│   ├── ms-exchange_rules.xml
│   ├── ms_firewall_rules.xml
│   ├── ms_ftpd_rules.xml
│   ├── ms_ipsec_rules.xml
│   ├── ms-se_rules.xml
│   ├── mysql_rules.xml
│   ├── named_rules.xml
│   ├── netscreenfw_rules.xml
│   ├── nginx_rules.xml
│   ├── nsd_rules.xml
│   ├── openbsd-dhcpd_rules.xml
│   ├── openbsd_rules.xml
│   ├── opensmtpd_rules.xml
│   ├── ossec_rules.xml
│   ├── owncloud_rules.xml
│   ├── pam_rules.xml
│   ├── php_rules.xml
│   ├── pix_rules.xml
│   ├── policy_rules.xml
│   ├── postfix_rules.xml
│   ├── postgresql_rules.xml
│   ├── proftpd_rules.xml
│   ├── proxmox-ve_rules.xml
│   ├── psad_rules.xml
│   ├── pure-ftpd_rules.xml
│   ├── racoon_rules.xml
│   ├── roundcube_rules.xml
│   ├── rules_config.xml
│   ├── sendmail_rules.xml
│   ├── smbd_rules.xml
│   ├── solaris_bsm_rules.xml
│   ├── sonicwall_rules.xml
│   ├── spamd_rules.xml
│   ├── squid_rules.xml
│   ├── sshd_rules.xml
│   ├── symantec-av_rules.xml
│   ├── symantec-ws_rules.xml
│   ├── syslog_rules.xml
│   ├── sysmon_rules.xml
│   ├── systemd_rules.xml
│   ├── telnetd_rules.xml
│   ├── trend-osce_rules.xml
│   ├── unbound_rules.xml
│   ├── vmpop3d_rules.xml
│   ├── vmware_rules.xml
│   ├── vpn_concentrator_rules.xml
│   ├── vpopmail_rules.xml
│   ├── vsftpd_rules.xml
│   ├── web_appsec_rules.xml
│   ├── web_rules.xml
│   ├── wordpress_rules.xml
│   └── zeus_rules.xml
├── stats
├── tmp
└── var
    └── run

```