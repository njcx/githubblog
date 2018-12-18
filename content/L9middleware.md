Title: 常见中间件（middleware） 0day合集
Date: 2017-06-8 15:20
Modified: 2017-06-8 15:20
Category: 安全
Tags: middleware
Slug: L9
Authors: nJcx
Summary:  常见中间件（middleware） 0day合集


- redis 未授权公网访问
	- https://www.seebug.org/vuldb/ssvid-89715


- Mongodb RCE
    - MongoDB before 2.0.9 and 2.2.x before 2.2.4
    - https://www.exploit-db.com/exploits/24935

- MongoDB 未授权访问
    - https://www.freebuf.com/articles/database/125127.html

- Memcached Server SASL 身份认证远程命令执行漏洞CVE-2016-8706(RCE)
    - Memcached 1.4.31(tested)
    - https://www.seebug.org/vuldb/ssvid-92507

- Memcached Server Update 远程代码执行漏洞

    - https://www.seebug.org/vuldb/ssvid-92506

- Memcached Server Append/Prepend 远程代码执行漏洞

    - https://www.seebug.org/vuldb/ssvid-92505

- Atlassian Jira 登陆后可以上传执行代码

    - https://www.exploit-db.com/exploits/45851/

- Atlassian Confluence 任意文件读取和目录遍历漏洞 (CVE-2015-8399)
    - Atlassian Confluence < 5.8.17
    - https://www.seebug.org/vuldb/ssvid-92416

- Atlassian Bitbucket Server远程代码执行漏洞（CVE-2018-5225）

    - Atlassian Bitbucket Server 5.8.0 < 5.8.2
    - Atlassian Bitbucket Server 5.7.0 < 5.7.3
    - Atlassian Bitbucket Server 5.6.0 < 5.6.5
    - Atlassian Bitbucket Server 5.5.0 < 5.5.8
    - Atlassian Bitbucket Server 4.13.0 < 5.4.8

    - https://www.linuxidc.com/Linux/2018-03/151578.htm

- Zabbix  SQL注入漏洞
    - 2.2.x, 3.0.0-3.0.3
    - 在Zabbix中有两个文件存在SQL注入漏洞，分别是jsrpc.php和latest.php，存在漏洞参数分别为：profileIdx2和toggle_ids
    - https://blog.csdn.net/Jiajiajiang_/article/details/84064957
    - https://www.jisec.com/sec/703.html

- Phpmyadmin

- Jenkins

- Elk

- Gitlab

- Kubernetes

- Nagios

- Apache CouchDB

- WebLogic

- JBoss
    - JBOSSAS 5.x/6.x 反序列化命令执行漏洞（CVE-2017-12149）
    - https://www.seebug.org/vuldb/ssvid-96880
    - JBOSSAS 4.x 反序列化命令执行漏洞（CVE-2017-7504）
    - https://www.seebug.org/vuldb/ssvid-96881

-  WebSphere

- Tomcat

- Jetty

- RabbitMQ


