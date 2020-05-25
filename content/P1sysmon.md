Title: Windows攻防之sysmon的使用与绕过
Date: 2018-06-07 03:20
Modified: 2018-06-07 03:20
Category: 安全
Tags: Windows
Slug: P1
Authors: nJcx
Summary: Windows攻防之sysmon的使用与绕过~

#### 介绍


  Sysmon是微软的一款免费的轻量级系统监控工具。它通过系统服务和驱动程序实现记录进程创建，网络连接以及文件创建时间更改的详细信息，并把相关的信息写入并展示在windows的日志事件里。我们可以通过读取Windows的日志，了解Windows的安全状态。

  Sysmon安装后分为用户态系统服务，驱动两部分，用户态通过ETW(Event Tracing for Windows)实现对网络数据记录，通过EventLog对驱动返回的数据进行解析，驱动部分则通过进、线程，模块的回调函数收集进程相关的信息，通过Minifilter文件过滤驱动和注册表回调函数记录访问文件、注册表的数据。
  
   从功能上来讲，Sysmon是一款优秀的HIDS、EDR的主机入侵检测引擎，其依托于Windows内核层进、线程，模块，注册表回调，及文件过滤驱动针对相应的行为进行实时的增、删、改信息收集并通过ETW存储并展示于Windows日志。