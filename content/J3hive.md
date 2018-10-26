Title: hive 实践笔记
Date: 2018-07-02 13:20
Modified: 2018-07-02 13:20
Category: Big data
Tags: hive
Slug: J3
Authors: nJcx
Summary: 记录一下hive实践笔记 ~


#### 介绍


#### 安装

系统：CentOS 7.3 

目录： /opt 

```bash

wget https://mirrors.aliyun.com/apache/hive/stable-2/apache-hive-2.3.3-bin.tar.gz | tar -zxvf 

```

```bash
export HIVE_HOME={{pwd}}
export PATH=$HIVE_HOME/bin:$PATH
```

#### 配置