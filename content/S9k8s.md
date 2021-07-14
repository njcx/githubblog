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

容器是基于镜像构建的，如果镜像本身就是一个恶意镜像或是一个存在漏洞的镜像，那么基于它搭建的容器自然就是不安全的了，故镜像安全直接决定了容器安全。

2,  k8s 的配置和使用问题

Kubernetes 的服务在正常启动后会开启两个端口：8080，6443。两个端口都是提供 Api Server 服务的，一个可以直接通过 Web 访问，另一个可以通过 kubectl 客户端进行调用。如果没有合理的配置验证和权限，那么攻击者就可以通过这两个接口去获取容器的权限，甚至通过创建自定义的容器去获取宿主机的权限。etcd是一个高可用的key-value数据库，它为k8s集群提供底层数据存储。一旦etcd被黑客拿下，就意味着整个k8s集群失陷。etcd最大的安全风险是未授权访问。

3， k8s 自身组件和操作系统及其依赖组件的安全问题

比如， docker-runc CVE-2019-5736 和 containerd-shim CVE-2020-15257容器逃逸







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


```bash

/projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/vulnerabilities  


curl -X GET "http://172.16.116.5/api/v2.0/projects/library/repositories/fastjson/artifacts/1.2.24/additions/vulnerabilities" -H "accept: application/json" -H "X-Request-Id: 111"

```



![agent](../images/image.png)



k8s 基线

https://github.com/aquasecurity/kube-bench


```
$ kubectl apply -f job.yaml
job.batch/kube-bench created

$ kubectl get pods
NAME                      READY   STATUS              RESTARTS   AGE
kube-bench-j76s9   0/1     ContainerCreating   0          3s

# Wait for a few seconds for the job to complete
$ kubectl get pods
NAME                      READY   STATUS      RESTARTS   AGE
kube-bench-j76s9   0/1     Completed   0          11s

# The results are held in the pod's logs
kubectl logs kube-bench-j76s9
[INFO] 1 Master Node Security Configuration
[INFO] 1.1 API Server

```


![agent](../images/WechatIMG298.jpeg)


![agent](../images/WechatIMG299.jpeg)




kube-bench和kube-hunter是aquasec的开源工具，它们可以在Kubernetes集群中寻找安全问题。它们在Kubernetes基础架构堆栈中分析安全状况的方法有所区别。kube-bench主要用于让你的实践符合CIS的标准，而kube-hunter则关注你要暴露的漏洞。它们两个结合使用，可以为我们确定合规性提供一个很好的视角。

让我们先从kube-bench开始，它会根据CIS的安全性最佳实践检查Kubernetes是否部署。kube-bench可以运行在本地或在你的Kubernetes环境中作为容器。一旦部署完成，kube-bench会根据要执行的测试以及不同的Kubernetes版本，为你提供一些用于master或节点的配置文件。需要注意的是，配置文件会被写入YAML。那意味着你可以对它们进行调整以适应你的测试，或者当CIS或Kubernetes公开更多测试时直接采用它们即可。


```bash

pip install kube-hunter

```


![agent](../images/WeChatacd04043ac589270629b297a810ec9d3.png)

kube-hunter会在你的环境内部或外部运行扫描功能，以让你了解在你的Kubernetes平台中的安全性漏洞。kube-hunter可以在集群内部或外部、在任何机器上作为一个容器运行。当你进入集群DNS或IP之后，kube-hunter就会开始查看你当前打开的端口、运行测试并查看是否存在任何漏洞。然后，你将会获得大量相关信息，可以帮助你确定下一步应该如何执行。

kube-hunter的默认状态是“passive”，这意味着它将查找诸如Kubernetes SSL证书中的电子邮件地址之类的内容，并检查开放端口、代理服务和dashboard。在“active”状态中，kube-hunter将会查找其他弱点，并利用发现的弱点来进一步探索漏洞，因此它十分强大。虽然kube-hunter不会查看容器镜像内部(有其他工具可以专门查看此处)，但它可以运行可能暴露数据泄露或有危害的电子邮件地址的测试。




K8S runtime 的监控



Falco 由 Sysdig 于 2016 年创建，是第一个作为孵化级项目加入 CNCF 的运行时安全项目。Falco可以对Linux系统调用行为进行监控，主要是用的eBPF技术。Falco的主要功能如下：
从内核运行时采集Linux系统调用。
提供了一套强大的规则引擎，用于对Linux系统调用行为进行监控。
当系统调用违反规则时，会触发相应的告警。


```bash

curl -s https://falco.org/repo/falcosecurity-3672BA8F.asc | apt-key add -
echo "deb https://download.falco.org/packages/deb stable main" | tee -a /etc/apt/sources.list.d/falcosecurity.list

apt-get update -y
apt-get -y install linux-headers-$(uname -r)
apt-get install -y falco


```


```bash

rpm --import https://falco.org/repo/falcosecurity-3672BA8F.asc
curl -s -o /etc/yum.repos.d/falcosecurity.repo https://falco.org/repo/falcosecurity-rpm.repo

yum -y install kernel-devel-$(uname -r)

yum -y install falco

```


https://falco.org/docs/getting-started/installation/


![agent](../images/imag1e.png)




```bash

json_output: true
json_include_output_property: true
http_output:
  enabled: true
  url: "http://localhost:2801"

```





https://github.com/falcosecurity/falcosidekick.git



![agent](../images/WechatIMG171123.jpeg)



```bash

elasticsearch:
   hostport: "http://10.10.116.177:9201" 
   index: "falco" 
   type: "event"
   minimumpriority: "" 
   suffix: "daily" 
   mutualtls: false 
   checkcert: true 
   username: "" 
   password: "" 


kafka:
  hostport: "" 
  topic: "" 
  # minimumpriority: "debug" 
  
  
```