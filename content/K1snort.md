Title: Snort 学习记录
Date: 2017-05-27 13:20
Modified: 2017-05-27 13:20
Category: 安全
Tags: Snort
Slug: K1
Authors: nJcx
Summary: Snort 学习记录

#### 介绍


#### 安装

```
# curl -Ls https://www.snort.org/downloads/snort/snort-2.9.12.tar.gz | tar zx

# curl -Ls https://www.snort.org/downloads/snort/daq-2.0.6.tar.gz | tar zx

# yum install luagit luagit-devel flex bison libdnet-devel libdnet libpcap libpcap-devel gcc gcc-c++ pcre-devel zlib-devel -y

# cd daq-2.0.6 && ./configure  && make && make install

# cd snort-2.9.12 && ./configure --enable-sourcefire --prefix=/opt/snort && make && make install

# cd /opt/snort && curl -Ls https://www.snort.org/downloads/community/community-rules.tar.gz | tar zx

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





