Title: Snort 学习记录
Date: 2017-05-27 13:20
Modified: 2017-05-27 13:20
Category: 安全
Tags: Snort
Slug: K1
Authors: nJcx
Summary: Snort 学习记录

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
# mkdir -p /opt/snort/log

# wget https://www.snort.org/rules/snortrules-snapshot-29111.tar.gz?oinkcode=bcc56dad6b79c5929c7f70985501f7dbabf9dab1 -O snortrules-snapshot-29111.tar.gz

# cd /opt/ && curl -Ls https://www.snort.org/downloads/community/community-rules.tar.gz | tar zx

# cp -r rules preproc_rules so_rules snort
# cd /opt/community-rules && cp community.rules /opt/snort/rules/ 

# mkdir -p /opt/snort/snort_dynamicrules

# touch /opt/snort/rules/black_list.rules
# touch /opt/snort/rules/white_list.rules

```
然后在 /opt/snort/etc/snort.conf 相关的行数改为下面这个样子

```bash
246 # path to dynamic preprocessor libraries
247 dynamicpreprocessor directory /opt/snort/lib/snort_dynamicpreprocessor/
248
249 # path to base preprocessor engine
250 dynamicengine /opt/snort/lib/snort_dynamicengine/libsf_engine.so
251
252 # path to dynamic rules libraries
253 dynamicdetection directory /opt/snort/snort_dynamicrules
652 include $RULE_PATH/community.rules

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

测试配置文件

```bash
/opt/snort/bin/snort -T -c /opt/snort/etc/snort.conf
```

```bash
[ Port Based Pattern Matching Memory ]
+- [ Aho-Corasick Summary ] -------------------------------------
| Storage Format    : Full-Q
| Finite Automaton  : DFA
| Alphabet Size     : 256 Chars
| Sizeof State      : Variable (1,2,4 bytes)
| Instances         : 267
|     1 byte states : 252
|     2 byte states : 15
|     4 byte states : 0
| Characters        : 216598
| States            : 167409
| Transitions       : 27834173
| State Density     : 64.9%
| Patterns          : 10745
| Match States      : 11141
| Memory (MB)       : 86.63
|   Patterns        : 1.23
|   Match Lists     : 2.80
|   DFA
|     1 byte states : 1.56
|     2 byte states : 80.58
|     4 byte states : 0.00
+----------------------------------------------------------------
[ Number of patterns truncated to 20 bytes: 607 ]

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.12 GRE (Build 325)
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014-2018 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.

▽
           Using libpcap version 1.5.3
           Using PCRE version: 8.32 2012-11-30
           Using ZLIB version: 1.2.7

           Rules Engine: SF_SNORT_DETECTION_ENGINE  Version 3.0  <Build 1>
           Preprocessor Object: appid  Version 1.1  <Build 5>
           Preprocessor Object: SF_DNP3  Version 1.1  <Build 1>
           Preprocessor Object: SF_MODBUS  Version 1.1  <Build 1>
           Preprocessor Object: SF_GTP  Version 1.1  <Build 1>
           Preprocessor Object: SF_REPUTATION  Version 1.1  <Build 1>
           Preprocessor Object: SF_SIP  Version 1.1  <Build 1>
           Preprocessor Object: SF_SDF  Version 1.1  <Build 1>
           Preprocessor Object: SF_DCERPC2  Version 1.0  <Build 3>
           Preprocessor Object: SF_SSLPP  Version 1.1  <Build 4>
           Preprocessor Object: SF_DNS  Version 1.1  <Build 4>
           Preprocessor Object: SF_SSH  Version 1.1  <Build 3>
           Preprocessor Object: SF_SMTP  Version 1.1  <Build 9>
           Preprocessor Object: SF_IMAP  Version 1.0  <Build 1>
           Preprocessor Object: SF_POP  Version 1.0  <Build 1>
           Preprocessor Object: SF_FTPTELNET  Version 1.2  <Build 13>

Snort successfully validated the configuration!
Snort exiting

```
测试通过


#### 使用

/opt/snort/bin/snort -c /opt/snort/etc/snort.conf -i ens33 -l /opt/snort/log -D

这里通过 -i 指定网卡， -c 指定配置文件，  通过-l 指定log 输出的目录，通过 -D 把进程放到后面运行，就可以在 /opt/snort/log 下面看到警告了



