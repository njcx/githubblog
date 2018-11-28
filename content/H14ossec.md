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