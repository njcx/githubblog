Title: splunk 实践
Date: 2018-06-05 08:20
Modified: 2018-06-05 08:20
Category: splunk
Tags: splunk
Slug: H13
Authors: nJcx
Summary: 记录一下splunk 的安装与使用
Status: draft


#### 安装

分两部分，splunk 和 splunkforwarder，前者相当于server，后者相当于agent，agent用于过滤和传输日志

```bash

https://download.splunk.com/products/splunk/releases/7.2.0/linux/splunk-7.2.0-8c86330ac18-Linux-x86_64.tgz

https://download.splunk.com/products/universalforwarder/releases/7.2.0/linux/splunkforwarder-7.2.0-8c86330ac18-Linux-x86_64.tgz

wget -O splunk-7.2.0-8c86330ac18-Linux-x86_64.tgz 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.0&product=splunk&filename=splunk-7.2.0-8c86330ac18-Linux-x86_64.tgz&wget=true'

wget -O splunkforwarder-7.2.0-8c86330ac18-Linux-x86_64.tgz 'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=7.2.0&product=universalforwarder&filename=splunkforwarder-7.2.0-8c86330ac18-Linux-x86_64.tgz&wget=true'

```

解压

```bash

# tar -zxvf splunk-7.2.0-8c86330ac18-Linux-x86_64.tgz

```

```bash

./splunk start --accept-license  //第一次使用，自动接收许可

./splunk enable boot-start   //设置开机启动

./splunk start   //启动splunk

./splunk stop    //停止splunk

./splunk restart   //重启splunk

./splunk status    //查看splunk状态

./splunk version   //查看splunk版

```


这里会提示接受协议，输入账号密码，同时会把splunk 添加到启动项里面，并且可以通过service splunk start 使用了，服务端就搭建OK了

#### 配置 splunkforwarder


```bash
# tar -zxvf splunkforwarder-7.2.0-8c86330ac18-Linux-x86_64.tgz
./splunk start --accept-license
./splunk enable boot-start

./splunk show splunkd-port //查看端口

./splunk set splunkd-port 8090 //修改端口

./splunk edit user admin -password ‘admin’ -role admin -auth admin:changeme  //修改密码
```

#### 使用

server 端的默认的端口是8089

```bash

	Checking http port [8000]: open
	Checking mgmt port [8089]: open
	Checking appserver port [127.0.0.1:8065]: open
	Checking kvstore port [8191]: open
	
```
agent 端的端口变成 ,因为在本机测试，防止冲突

```bash

Checking mgmt port [8090]: open

```

