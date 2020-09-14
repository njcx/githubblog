Title: Kubernetes集群安装
Date: 2018-08-08 20:20
Modified: 2018-08-08 20:20
Category: 安全
Tags: K8S
Slug: R8 
Authors: nJcx
Summary: Kubernetes集群安装~



#### 安装

一共3个节点，

```bash
10.10.252.215   master   
10.10.252.214   node1 
10.10.252.213   node2  
```

除了初始化，软件安装一致



k8s repo

```bash
[k8s]
name=k8s
enabled=1
gpgcheck=0
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/

```

base.repo

```bash
[base]
name=CentOS-$releasever - Base
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#released updates
[updates]
name=CentOS-$releasever - Updates
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus&infra=$infra
baseurl=https://mirrors.ustc.edu.cn/centos/$releasever/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

```




```bash

 cd /etc/yum.repos.d/
 wget http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
 vim k8s.repo
yum makecache
 yum install docker-ce  kubelet kubeadm kubectl -y

cat /etc/docker/daemon.json

{
"exec-opts": ["native.cgroupdriver=systemd"],  
"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}


cat > /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

 echo "1" >/proc/sys/net/bridge/bridge-nf-call-iptables

 setenforce 0
 swapoff -a


systemctl restart docker && systemctl enable docker 
 systemctl restart kubelet && systemctl enable kubelet



master node1 node2 上面内容一致


master执行

kubeadm init --kubernetes-version=1.19.0 --apiserver-advertise-address=10.10.252.215 --image-repository registry.aliyuncs.com/google_containers --service-cidr=10.10.0.0/16 --pod-network-cidr=10.244.0.0/16

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
 sudo chown $(id -u):$(id -g) $HOME/.kube/config


kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml


```





```bash

node1 node2 执行

 kubeadm join 10.10.252.215:6443 --token u3toqk.8j7fnn0lmajgvnvq     --discovery-token-ca-cert-hash sha256:49b37a021f9223d2f3af10d71a5ca47cc34e12d2c20147adfc61a6a4b90c4b97 
  
    
```



master 生成join语句脚本备用

```bash

#!/bin/bash

if [ $EUID -ne 0 ];then
    echo "You must be root (or sudo) to run this script"
    exit 1
fi

if [ $# != 1 ] ; then
    echo "Usage: $0 [master-hostname | master-ip-address]"
    echo " e.g.: $0 api.k8s.hiko.im"
    exit 1;
fi

token=`kubeadm token create`
cert_hash=`openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'`

echo "Refer the following command to join kubernetes cluster:"
echo "kubeadm join $1:6443 --token ${token} --discovery-token-ca-cert-hash sha256:${cert_hash}"


```
