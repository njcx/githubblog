Title: centos6.8 下lvs+keepalived高并发实践
Date: 2016-01-01 10:20
Modified: 2016-01-01 10:20
Category: Linux
Tags: 集群，HA
Slug: A1
Authors: nJcx
Summary: 介绍一下linux下lvs+keepalived　搭建过程，记录一下学习过程
##安装
- yum install -y keepalived 
- yum install -y ipvsadm
##配置
MASTER
```bash
vrrp_instance VI_1 {
            state MASTER            # 状态实际MASTER
            interface eth0            # 监听网卡切换
            virtual_router_id 51
            priority 100                # 优先级（越大优先级越高）
            advert_int 1
            authentication {
                auth_type PASS
                auth_pass 1111
            }
            virtual_ipaddress {        # 虚拟IP地址列表，即VIP
                172.28.14.227
                172.28.14.228
                172.28.14.229
            }
        }
        virtual_server 172.28.14.227 8080 {
            delay_loop 6
            lb_algo wlc
            lb_kind DR                    # DR模式
            persistence_timeout 50
            protocol TCP
            real_server 172.28.19.100 8080 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 8080
                }
            }
            real_server 172.28.19.101 8080 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 8080
                }
            }
            real_server 172.28.19.102 8080 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 8080
                }
            }
        }
        virtual_server 172.28.14.228 25 {
            delay_loop 6
            lb_algo wlc
            lb_kind DR                    # DR模式
            persistence_timeout 50
            protocol TCP
            real_server 172.28.19.103 25 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 25
                }
            }
            real_server 172.28.19.104 25 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 25
                }
            }
            real_server 172.28.19.105 25 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 25
                }
            }
        }
        virtual_server 172.28.14.229 21 {
            delay_loop 6
            lb_algo wlc
            lb_kind DR                    # DR模式
            persistence_timeout 50
            protocol TCP
            real_server 172.28.19.106 21 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 21
                }
            }
            real_server 172.28.19.107 21 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 21
                }
            }
            real_server 172.28.19.108 21 {
                weight 1                  # 权重（权重越高处理的请求越多）
                TCP_CHECK {
                    connect_timeout 3
                    nb_get_retry 3
                    delay_before_retry 3
                    connect_port 21
                }
            }
        }
```
BACKUP
```bash
        vrrp_instance VI_1 {
            state BACKP            # 状态实际BACKUP
            ...
            priority 99                # 优先级99（比MASTER优先级100低）
            ...
        }
```
realserver

```bash
 #!/bin/bash
        VIP=172.28.14.227
        . /etc/rc.d/init.d/functions
        case "$1" in
        start)
            echo 1 > /proc/sys/net/ipv4/conf/lo/arp_ignore
            echo 2 > /proc/sys/net/ipv4/conf/lo/arp_announce
            echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
            echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce
            ifconfig lo:0 $VIP broadcast $VIP netmask 255.255.255.255 up
            /sbin/route add -host $VIP dev lo:0
            sysctl -p > /dev/null 2>&1
            echo "realserver start OK"
            ;;
        stop)
            echo 0 > /proc/sys/net/ipv4/conf/lo/arp_ignore
            echo 0 > /proc/sys/net/ipv4/conf/lo/arp_announce
            echo 0 > /proc/sys/net/ipv4/conf/all/arp_ignore
            echo 0 > /proc/sys/net/ipv4/conf/all/arp_announce
            ifconfig lo:0 down
            /sbin/route del $VIP > /dev/null 2>&1
            echo "realserver stoped"
            ;;
        *)
            echo "Usage:$0 {start|stop}"
            exit 1
        esac
        exit 0
```

##测试
把两个web server 页面设置不同实测.
