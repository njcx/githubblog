Title: gitlab 的安装
Date: 2018-06-08 13:20
Modified: 2018-06-08 13:20
Category: gitlab
Tags: gitlab
Slug: H10
Authors: nJcx
Summary: gitlab安装与使用

#### 安装

gitlab 分为收费和免费的社区版，新建 /etc/yum.repos.d/gitlab-ce.repo，内容如下

```bash
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=0
enabled=1
```

```bash
# yum makecache
# yum install gitlab-ce
```

#### 配置

```bash

vim /etc/gitlab/gitlab.rb

```

external_url 'https://gitlab.xxx.com'

改为ip 或者域名


#### 遇到的问题

页面出现502，通过调高硬件配置，解决该问题