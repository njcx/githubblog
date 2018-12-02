Title: rootkit的检测工具使用介绍
Date: 2017-05-27 14:20
Modified: 2017-05-27 14:20
Category: 安全
Tags: rootkit
Slug: K3
Authors: nJcx
Summary: rootkit的检测工具使用介绍

#### 介绍
chkrootkit和rootkit hunter
#### chkrootkit安装
```bash
yum install gcc gcc-c++ net-snmp-utils net-tools make glibc-static -y

```

```bash
curl -LS ftp://ftp.pangeia.com.br/pub/seg/pac/chkrootkit.tar.gz |  tar zx  && cd chkrootkit-0.52 && make sense

```

#### chkrootkit使用

```bash

./chkrootkit | grep INFECTED

```

我测试了一下，新安装的centos7.3，居然,额

```bash
Searching for Linux.Xor.DDoS ... INFECTED: Possible Malicious Linux.Xor.DDoS installed

```


#### rootkit hunter 安装

```bash

curl -LS  https://nchc.dl.sourceforge.net/project/rkhunter/rkhunter/1.4.6/rkhunter-1.4.6.tar.gz | tar zx && cd rkhunter-1.4.6 && sh installer.sh --layout default --install
 
```
#### rootkit hunter 使用

```bash

/usr/local/bin/rkhunter --propupd

# 更新整个文件属性数据库
 
/usr/local/bin/rkhunter -c  --sk --rwo
 
#  -c                                  --check 
#  --rwo, --report-warnings-only       --Show only warning messages
#  --sk,                               --skip-keypress

```

