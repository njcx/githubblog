Title: saltstack 实践笔记
Date: 2018-07-01 19:20
Modified: 2018-07-01 19:20
Category: saltstack
Tags: saltstack
Slug: J1
Authors: nJcx
Summary: 记录一下saltstack实践笔记 ~


#### 介绍


#### 安装

服务端：172.16.131.134

```bash
yum install -y epel-release
yum install -y salt-master salt-minion
```

```bash
service salt-master start
service salt-minion start
chkconfig salt-master on
chkconfig salt-minion on
setenforce 0
```

客服端：172.16.131.136

```bash

yum install -y epel-release
yum install -y salt-minion

```

```bash
service salt-minion start
chkconfig salt-minion on
setenforce 0
```


#### 配置

 vim /etc/salt/minion

```bash
master: 172.16.131.134
```
 
 
 vim /etc/salt/master
  
 ```bash
 auto_accept: True
 ```
 
 service salt-minion restart
 
 service salt-master restart


