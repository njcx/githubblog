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
	- phpmyadmin4.8.1后台getshell
	- https://www.seebug.org/vuldb/ssvid-97355
	- PhpMyAdmin 4.3.0—4.6.2 授权用户远程命令执行漏洞
	- https://www.seebug.org/vuldb/ssvid-92209
	- phpmyadmin2.8.0.3任意文件包含漏洞
	- https://www.seebug.org/vuldb/ssvid-92339
	
- Jenkins
	- Jenkins 任意文件读取漏洞(CVE-2018-1999002)
	- https://www.seebug.org/vuldb/ssvid-97431
	- Jenkins “Java 反序列化”过程远程命令执行漏洞
	- https://www.seebug.org/vuldb/ssvid-89725

- Elk
	- Elasticsearch Kibana Console本地文件包含漏洞 (CVE-2018-17246)
	- https://www.seebug.org/vuldb/ssvid-97730
	- Elasticsearch Kibana跨站请求伪造漏洞
	- https://www.seebug.org/vuldb/ssvid-90026

- Gitlab
	- Gitlab Wiki API 远程命令执行漏洞 (CVE-2018-18649)
	- https://www.seebug.org/vuldb/ssvid-97723
	- GitLab application server 文件读取导致命令执行漏洞
	- https://www.seebug.org/vuldb/ssvid-92516
	- GitLab 模版 API 目录遍历漏洞 (CVE-2018-19856)
	- https://www.seebug.org/vuldb/ssvid-97708
	- GitLab 任意用户 authentication tokens 泄漏导致远程代码执行漏洞
	- https://www.seebug.org/vuldb/ssvid-92529

- Kubernetes
	- Kubernetes特权升级漏洞 (CVE-2018-1002105)
	- https://www.seebug.org/vuldb/ssvid-97707
	- Etcd REST API 未授权访问漏洞
	- https://www.seebug.org/vuldb/ssvid-97202

- Nagios
	- NagiosXI <= 5.4.12 commandline.php SQL injection(CVE-2018-10735)
	- NagiosXI <= 5.4.12 info.php SQL injection(CVE-2018-10736)
	- NagiosXI <= 5.4.12 logbook.php SQL injection(CVE-2018-10737)
	- NagiosXI <= 5.4.12 menuaccess.php SQL injection(CVE-2018-10738)
	- Nagios XI <=5.5.7 Reflect XSS#1
	- Nagios XI <=5.5.7 Reflect XSS#2
	- https://www.seebug.org/vuldb/ssvid-97699
	- https://www.seebug.org/vuldb/ssvid-97259	

- Apache CouchDB
	- Remote Code Execution in CouchDB(CVE-2017-12635)
	- https://www.seebug.org/vuldb/ssvid-96869
	- CouchDB未授权访问导致的任意系统命令执行漏洞
	- https://www.seebug.org/vuldb/ssvid-91597
	- Apache CouchDB Remote Privilege Escalations (CVE-2018-17188)
	- https://www.seebug.org/vuldb/ssvid-97732

- WebLogic

	- WebLogic 反序列化远程命令执行漏洞(CVE-2018-3252)
	- https://www.seebug.org/vuldb/ssvid-97673
	- WebLogic “Java 反序列化”过程远程命令执行漏洞
	- https://www.seebug.org/vuldb/ssvid-89726

- JBoss
    - JBOSSAS 5.x/6.x 反序列化命令执行漏洞（CVE-2017-12149）
    - https://www.seebug.org/vuldb/ssvid-96880
    - JBOSSAS 4.x 反序列化命令执行漏洞（CVE-2017-7504）
    - https://www.seebug.org/vuldb/ssvid-96881

-  WebSphere
	-  IBM WebSphere Application Server Admin Console File Disclosure
	-  https://www.seebug.org/vuldb/ssvid-97612
	-  IBM WebSphere Portal内存消耗拒绝服务漏洞
	-  https://www.seebug.org/vuldb/ssvid-89793
	-  WebSphere “Java 反序列化”过程远程命令执行漏洞 
	-  https://www.sebug.net/vuldb/ssvid-89727
	-  IBM WebSphere Application Server CRLF 注入漏洞
	-  https://www.seebug.org/vuldb/ssvid-89752

- Tomcat
	- Tomcat代码执行漏洞(CVE-2017-12615)
	- https://www.seebug.org/vuldb/ssvid-96557
	- Tomcat ​信息泄露漏洞(CVE-2017-12616 )
	- https://www.seebug.org/vuldb/ssvid-96562
	- Apache Tomcat 信息泄露漏洞（CVE-2016-6816）
	- https://www.seebug.org/vuldb/ssvid-92678

- Jetty
	- Jetty 6.1.x JSP Snoop Page Multiple Cross-Site Scripting Vulnerabilities
	- https://www.seebug.org/vuldb/ssvid-86772

- RabbitMQ
	- RabbitMQ Web Management < 3.7.6 - Cross-Site Request Forgery (Add Admin)
	- https://www.seebug.org/vuldb/ssvid-97394

- Supervisord
	- Supervisor Authenticated Remote Code Execution(CVE-2017-11610)
	- https://www.seebug.org/vuldb/ssvid-96316
 
- Openssl 
	- OpenSSL Heartbleed 漏洞 (心脏出血)
	- https://www.seebug.org/vuldb/ssvid-89231

