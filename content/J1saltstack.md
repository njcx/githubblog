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
 auto_accept: True //这样服务端就可以自动接收key
 ```
 
 service salt-minion restart
 
 service salt-master restart


使用 salt-key -L 即可查看

```bash
Accepted Keys:
master
slave_1
Denied Keys:
Unaccepted Keys:

```

测试  salt '*' test.ping 

```bash

slave_1:
    True
master:
    True
    
```

测试 salt '*' cmd.run "df -h"

```bash

    Filesystem               Size  Used Avail Use% Mounted on
    /dev/mapper/centos-root   17G  5.0G   13G  30% /
    devtmpfs                 871M     0  871M   0% /dev
    tmpfs                    883M   12K  883M   1% /dev/shm
    tmpfs                    883M  9.6M  873M   2% /run
    tmpfs                    883M     0  883M   0% /sys/fs/cgroup
    /dev/sda1               1014M  130M  885M  13% /boot
    tmpfs                    177M     0  177M   0% /run/user/0
master:
    Filesystem               Size  Used Avail Use% Mounted on
    /dev/mapper/centos-root   17G  4.9G   13G  29% /
    devtmpfs                 871M     0  871M   0% /dev
    tmpfs                    883M   16K  883M   1% /dev/shm
    tmpfs                    883M  9.6M  873M   2% /run
    tmpfs                    883M     0  883M   0% /sys/fs/cgroup
    /dev/sda1               1014M  130M  885M  13% /boot
    tmpfs                    177M     0  177M   0% /run/user/0
    
```

如上，只是简单的测试，还有比较有趣的 grains，pillar
