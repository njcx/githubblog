Title: suricata 学习记录
Date: 2017-05-27 12:20
Modified: 2017-05-27 12:20
Category: 安全
Tags: Suricata
Slug: K2
Authors: nJcx
Summary: suricata 学习记录
Status: draft
#### 介绍
suricata是一款开源高性能的多线程入侵检测系统，并支持ips（入侵防御）与nsm（网络安全监控）模式，完全兼容snort规则语法和支持lua脚本。使用标准的输入和输出格式，如YAML和JSON与现有SIEM，Splunk，ELK和其他数据库等工具的集成变得毫不费力。
#### 安装

```bash
yum install -y libpcap-devel libnet-devel pcre-devel gcc-c++ automake autoconf libtool make libyaml-devel zlib-devel file-devel jansson-devel nss-devel python-pip python-devel && pip install pyyaml
```

```bash
 curl -LS https://www.openinfosecfoundation.org/download/suricata-4.1.0.tar.gz | tar zx
```

```bash
 ./configure --prefix=/opt/suricata && make && make install && make install-full

```

到这里基本安装完成
#### 使用





