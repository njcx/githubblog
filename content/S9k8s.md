Title: K8S安全建设经验试分享
Date: 2018-08-28 20:20
Modified: 2018-08-28 20:20
Category: 安全
Tags: 企业安全建设
Slug: S9
Authors: nJcx
Summary: K8S安全建设经验试分享 ~



#### 介绍

k8s环境的安全主要来自3个方向：


1， images 镜像的安全问题

2,  k8s 的配置和使用问题

3， k8s 自身组件和操作系统及其依赖组件的安全问题


```bash

#  cd /etc/yum.repos.d/
#  wget http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
#  yum makecache
#  yum install docker-ce  -y  && systemctl start docker && systemctl enable docker


#  vim /etc/docker/daemon.json

{
"exec-opts": ["native.cgroupdriver=systemd"],  
"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}

# systemctl  restart  docker 

```

```bash

#  curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# chmod +x /usr/local/bin/docker-compose

# wget  https://github.com/goharbor/harbor/releases/download/v2.2.3/harbor-offline-installer-v2.2.3.tgz

# tar xf harbor-offline-installer-v2.2.3.tgz 
# cp harbor.yml.tmpl harbor.yml

# ./prepare 
# ./install.sh  --with-trivy  --with-chartmuseum 
 
```
![agent](../images/1501625901938_.pic_hd.jpg)


![agent](../images/1521625902561_.pic_hd.jpg)


![agent](../images/1541625902778_.pic.jpg)


![agent](../images/1561625902819_.pic.jpg)

![agent](../images/1571625903101_.pic.jpg)

![agent](../images/1581625903216_.pic.jpg)

![agent](../images/15.50.15.png)


![agent](../images/15.49.51.png)


![agent](../images/image.png)


![agent](../images/imag1e.png)



```bash

json_output: true
json_include_output_property: true
http_output:
  enabled: true
  url: "http://localhost:2801"

```





https://github.com/falcosecurity/falcosidekick.git


```bash


elasticsearch:
   hostport: "http://10.10.116.177:9201" # http://{domain or ip}:{port}, if not empty, Elasticsearch output is enabled
   index: "falco" # index (default: falco)
   type: "event"
   minimumpriority: "" # minimum priority of event for using this output, order is emergency|alert|critical|error|warning|notice|informational|debug or "" (default)
   suffix: "daily" # date suffix for index rotation : daily (default), monthly, annually, none
   mutualtls: false # if true, checkcert flag will be ignored (server cert will always be checked)
   checkcert: true # check if ssl certificate of the output is valid (default: true)
   username: "" # use this username to authenticate to Elasticsearch if the username is not empty (default: "")
   password: "" # use this password to authenticate to Elasticsearch if the password is not empty (default: "")

kafka:
  hostport: "" # Apache Kafka Host:Port (ex: localhost:9092). Defaults to port 9092 if no port is specified after the domain, if not empty, Kafka output is enabled
  topic: "" # Name of the topic, if not empty, Kafka output is enabled
  # minimumpriority: "debug" # minimum priority of event for using this output, order is emergency|alert|critical|error|warning|notice|informational|debug or "" (default)
  
  
  ```