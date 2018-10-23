Title: Jenkins 了解一下
Date: 2018-06-07 13:20
Modified: 2018-06-07 13:20
Category: jenkins
Tags: jenkins
Slug: H8
Authors: nJcx
Summary: Jenkins 安装和使用

#### 安装
方法1：

```bash
# sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

#sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

# yum install jenkins

```

方法2：

```bash

# wget https://pkg.jenkins.io/redhat-stable/jenkins-2.138.1-1.1.noarch.rpm

# rpm -ivh jenkins-2.138.1-1.1.noarch.rpm
```

```bash
jenkins的目录结构：
/usr/lib/jenkins/jenkins.war     WAR包 
/etc/sysconfig/jenkins       　　 配置文件
/var/lib/jenkins/        　　　　   默认的JENKINS_HOME目录
/var/log/jenkins/jenkins.log      Jenkins日志文件
```
 vim /etc/init.d/jenkins 最下面加上jdk实际的目录，不然报错

```bash
 
	candidates="
	/etc/alternatives/java
	/usr/lib/jvm/java-1.6.0/bin/java
	/usr/lib/jvm/jre-1.6.0/bin/java
	/usr/lib/jvm/java-1.7.0/bin/java
	/usr/lib/jvm/jre-1.7.0/bin/java
	/usr/lib/jvm/java-1.8.0/bin/java
	/usr/lib/jvm/jre-1.8.0/bin/java
	/usr/bin/java
	/opt/jdk1.8.0_144/bin/java
	
```

service jenkins start

chkconfig jenkins on

cat /var/lib/jenkins/secrets/initialAdminPassword

读取密码，用该密码登录，默认端口8080


#### 使用

进去是时候遇到，No such plugin: cloudbees-folder，通过地址栏里面输入：ip:port/restart


