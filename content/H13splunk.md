Title: splunk 实践
Date: 2018-06-05 08:20
Modified: 2018-06-05 08:20
Category: splunk
Tags: splunk
Slug: H13
Authors: nJcx
Summary: 记录一下splunk 的安装与使用

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
# tar -zxvf splunkforwarder-7.2.0-8c86330ac18-Linux-x86_64.tgz

```

./splunk enable boot-start  

这里会提示接受协议，输入账号密码，同时会把splunk 添加到启动项里面，并且可以通过service splunk start 使用了，服务端就搭建OK了

