Title: ELK 实践
Date: 2018-06-05 09:20
Modified: 2018-06-05 09:20
Category: Big data
Tags: elk
Slug: H12
Authors: nJcx
Summary: 记录一下ELK的使用过程 

#### 安装


下载 elk 组件备用

```bash

https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.2.0-linux-x86_64.tar.gz
https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-6.2.0-linux-x86_64.tar.gz
https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-6.2.0-linux-x86_64.tar.gz
https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-6.2.0-linux-x86_64.tar.gz
https://artifacts.elastic.co/downloads/beats/heartbeat/heartbeat-6.2.0-linux-x86_64.tar.gz
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.0.tar.gz
https://artifacts.elastic.co/downloads/kibana/kibana-6.2.0-linux-x86_64.tar.gz
https://artifacts.elastic.co/downloads/logstash/logstash-6.2.0.tar.gz
https://artifacts.elastic.co/downloads/kibana-plugins/x-pack-6.2.0.zip/x-pack-6.2.0.zip

```
- Packetbeat： 网络数据（收集网络流量数据）
- Metricbeat： 指标 （收集系统、进程和文件系统级别的 CPU 和内存使用情况等数据）
- Filebeat： 日志文件（收集文件数据）
- Winlogbeat： windows事件日志（收集 Windows 事件日志数据）
- Auditbeat：审计数据 （收集审计日志）
- Heartbeat：运行时间监控 （收集系统运行时的数据）
- Logstash: 过滤和传输
- Elasticsearch ： 存储与搜索引擎
- Kibana：前端 


安装jdk 和 scala
(scala 和 kafka备用，可不装)

```bash

https://downloads.lightbend.com/scala/2.12.6/scala-2.12.6.tgz
http://mirrors.hust.edu.cn/apache/kafka/2.0.0/kafka_2.12-2.0.0.tgz
http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz

```

```bash

cd /opt && download  ALL  && tar -zxvf  ALL

```

配置环境变量

```bash

echo -e "export JAVA_HOME=/opt/jdk1.8.0_181 \n\
export JRE_HOME=\${JAVA_HOME}/jre \n\
export CLASSPATH=.:\${JAVA_HOME}/lib:\${JRE_HOME}/lib \n\
export PATH=\${JAVA_HOME}/bin:\$PATH \n\
export SCALA_HOME=/opt/scala-2.12.6 \n\
export PATH=\$PATH:\$SCALA_HOME/bin \n\
" >> /etc/profile && source /etc/profile

```


#### 配置 elasticsearch 

两个节点：
172.16.131.134（master）
172.16.131.133（slave）


添加hosts文件

```bash
172.16.131.133 slave_1
172.16.131.134 master
```

vim /etc/security/limits.conf

```bash
* soft nofile 65536
* hard nofile 131072
* soft nproc 2048
* hard nproc 4096
```

vim /etc/sysctl.conf 

```bash
vm.max_map_count = 655360
```
sysctl -p

```bash
[root@localhost local]# groupadd elk
[root@localhost local]# useradd -g elk elk
```

```bash
[root@localhost local]# cd /opt 
[root@localhost local]# chown -R elk:elk elasticsearch-6.2.0
```


master 节点: 其他同上，es配置如下


```bash
cluster.name: elasticsearch
node.name: master
node.master: true  # 意思是该节点为主节点
node.data: false  # 表示这不是数据节点
network.host: 0.0.0.0  # 监听全部ip
http.port: 9200  # es服务的端口号
discovery.zen.ping.unicast.hosts:['172.16.131.133','172.16.131.134']
```

slave节点： 其他同上，es配置如下


```bash
cluster.name: elasticsearch
node.name: slave_1
node.master: false # 意思是该节点不是主节点
node.data: true  # 表示这是数据节点
network.host: 0.0.0.0  # 监听全部ip
http.port: 9200  # es服务的端口号
discovery.zen.ping.unicast.hosts:['172.16.131.133','172.16.131.134']
```

关闭防火墙（生产环境不应该关闭）

```bash
systemctl status firewalld.service
systemctl stop firewalld.service
systemctl disable firewalld.service
```
./elasticsearch -d 启动两个节点


测试

```bash

curl -GET 0.0.0.0:9200/_cat/health?v

curl -GET 0.0.0.0:9200/_cat/indices?v

curl -GET 0.0.0.0:9200/_cluster/health?pretty

curl -GET 0.0.0.0:9200/_cluster/state?pretty

```

#### 配置  kibna


```bash

server.port: 8080
server.host: "172.16.131.134"
elasticsearch.url: "http://localhost:9200"
logging.dest: /opt/kibana-6.1.2-linux-x86_64/log/kibana.log
elasticsearch.username: "kibana"
elasticsearch.password: "kibanapassword"

```

./kibana & 启动

- Discover   //搜索
- visualization  // 统计图
- Dashboard  // 看板
- Timelion //时间序列

bin/kibana-plugin install  file:///opt/x-pack-6.2.0.zip

bin/elasticsearch-plugin install file:///opt/x-pack-6.2.0.zip

/usr/share/logstash/bin/logstash-plugin install x-pack file:///opt/x-pack-6.2.0.zip


xpack.monitoring.elasticsearch.url: "http://ip:9200"



##### 配置logstash



```bash

xpack.monitoring.elasticsearch.url: "http://ip:9200"
xpack.monitoring.elasticsearch.username: logstash_system
xpack.monitoring.elasticsearch.password: pwd

```


# x-pack


```bash

curl -u elastic:pwd  -XPUT 'http://127.0.0.1:9200/_xpack/license' -H "Content-Type: application/json" -d @license.json

```
license.json

```bash
{"license":{"uid":"f19eabab-77ae-4ccd-b90c-f20e5605e625",
"type":"platinum",
"issue_date_in_millis":1542153600000,
"expiry_date_in_millis":2524579200999,
"max_nodes":100,
"issued_to":"nj cx (baidu)",
"issuer":"WebForm",
"signature":"AAAAAwAAAA1neEkkwW17TBDufpgpAAABmC9ZN0hjZDBGYnVyRXpCOW5Bb3FjZDAxOWpSbTVoMVZwUzRxVk1PSmkxaktJRVl5MUYvUWh3bHZVUTllbXNPbzBUemtnbWpBbmlWRmRZb25KNFlBR2x0TXc2K2p1Y1VtMG1UQU9TRGZVSGRwaEJGUjE3bXd3LzRqZ05iLzRteWFNekdxRGpIYlFwYkJiNUs0U1hTVlJKNVlXekMrSlVUdFIvV0FNeWdOYnlESDc3MWhlY3hSQmdKSjJ2ZTcvYlBFOHhPQlV3ZHdDQ0tHcG5uOElCaDJ4K1hob29xSG85N0kvTWV3THhlQk9NL01VMFRjNDZpZEVXeUtUMXIyMlIveFpJUkk2WUdveEZaME9XWitGUi9WNTZVQW1FMG1DenhZU0ZmeXlZakVEMjZFT2NvOWxpZGlqVmlHNC8rWVVUYzMwRGVySHpIdURzKzFiRDl4TmM1TUp2VTBOUlJZUlAyV0ZVL2kvVk10L0NsbXNFYVZwT3NSU082dFNNa2prQ0ZsclZ4NTltbU1CVE5lR09Bck93V2J1Y3c9PQAAAQAERQE/JDSC3INTJO4W5B1Hs7Ug+A9crNoVzQJOgjIdzP/U+A8XRc7Fb1APo+aCD+a6x4Sl+7/2p4HjjdF5G/n5GJYTMpOZ0CBOnq3VghGlmZsyWktqR8kiVPmt1J3a0TS2J8Np0s1ZCBsGhUXoy7CG1vTErUOjeJg2AgR3McXCm/WTzLjEVM/GZ1/u0qzEsxEUXGbRAFDLfQ9q9v6sIxUSybV42zLJKSTZJb/AJluGy0vQpLmRnEccKfKpzWGCYRaJg00K+LI6xs1RA8NJuXaahcwVBF+Osxi+/CWPdgXnlkJTcjKr6WzVjC7VNYOdVXu4sp3NefiinRWmfPGFYOQH",
"start_date_in_millis":1542153600000}}

```


```bash

wget https://artifacts.elastic.co/downloads/logstash/logstash-6.2.0.rpm

wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie;" http://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz


export JAVA_HOME=/opt/jdk1.8.0_191
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

ln -s /opt/jdk1.8.0_191/bin/java /usr/bin/java

```

