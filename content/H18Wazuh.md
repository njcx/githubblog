Title: wazuh(ossec)学习记录
Date: 2017-05-28 17:20
Modified: 2017-05-28 17:20
Category: 安全
Tags: wazuh
Slug: H18
Authors: nJcx
Summary: 记录一下学习Wazuh 心路 ~

#### 介绍
Wazuh 是 ossec 一个分支，通过与ELK的结合，可以把相关的记录发到ELK之中，如果把bro 和 wazuh 都往elk里面打，就可以实现一个基于nids 和 hids的 soc。
#### 安装


```bash

yum groupinstall development tools -y

curl -Ls https://github.com/wazuh/wazuh/archive/v3.6.1.tar.gz | tar zx

```

然后 sh install.sh, 填写一些内容，就可以开始安装啦

#### 配置agent

