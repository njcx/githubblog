Title: Snort 学习记录
Date: 2017-05-27 13:20
Modified: 2017-05-27 13:20
Category: 安全
Tags: Snort
Slug: K1
Authors: nJcx
Summary: Snort 学习记录
Status: draft
#### 介绍
在1998年，Marty Roesch先生用C语言开发了开放源代码(Open Source)的入侵检测系统Snort.直至今天，Snort已发展成为一个多平台(Multi-Platform),实时(Real-Time)流量分析，网络IP数据包(Pocket)记录等特性的强大的网络入侵检测/防御系统(Network Intrusion Detection/Prevention System),即NIDS/NIPS.Snort符合通用公共许可(GPL——GNU General Pubic License),在网上可以通过免费下载获得Snort,并且只需要几分钟就可以安装并开始使用它。snort基于libpcap。

#### 安装

```
# curl -Ls https://www.snort.org/downloads/snort/snort-2.9.12.tar.gz | tar zx

# curl -Ls https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz | tar zx

# yum install luagit luagit-devel flex bison libdnet-devel libdnet libpcap libpcap-devel gcc gcc-c++ pcre-devel zlib-devel -y

如果这里找不到luagit，那就编译一个吧
git clone http://luajit.org/git/luajit-2.0.git
cd luajit-2.0 && make && make install 

# cd daq-2.0.6 && ./configure  && make && make install

# cd snort-2.9.12 && ./configure --enable-sourcefire --prefix=/opt/snort && make && make install

# cp -r etc /opt/snort/
# cp -r preproc_rules/ /opt/snort/etc/
# mkdir -p /opt/snort/log
# mkdir -p /opt/snort/etc/rules
# touch /opt/snort/etc/rules/black_list.rules
# touch /opt/snort/etc/rules/white_list.rules
# touch /opt/snort/etc/rules/local.rules 

# cd /opt/snort && curl -Ls https://www.snort.org/downloads/community/community-rules.tar.gz | tar zx

# cd /opt/snort/community-rules && cp * /opt/snort/etc/rules/ 

```

```bash

[root@localhost bin]# ./snort -V

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.12 GRE (Build 325)
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014-2018 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.5.3
           Using PCRE version: 8.32 2012-11-30
           Using ZLIB version: 1.2.7
           
```


#### 使用





