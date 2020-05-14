Title: DDoS种类与防御
Date: 2018-06-07 01:20
Modified: 2018-06-07 01:20
Category: 安全
Tags: DDOS
Slug: P4
Authors: nJcx
Summary: DDoS种类与防御~


#### 工具

```bash
https://github.com/GinjaChris/pentmenu.git
https://github.com/OffensivePython/Saddam.git
https://github.com/649/Memcrashed-DDoS-Exploit
```

#### TCP

- SYN FLOOD 

SYN FLOOD攻击是在TCP三次握手过程中产生的。攻击者通过发送大量伪造的带有SYN标志位的TCP报文，与目标主机建立了很多虚假的半开连接，在服务器返回SYN+ACK数据包后，攻击者不对其做出响应，也就是不返回ACK数据包给服务器，这样服务器就会一直等待直到超时。这种攻击方式会使目标服务器连接资源耗尽、链路堵塞，从而达到拒绝服务的目的。SYN FLOOD攻击图示如下

- ACK FLOOD

ACK FLOOD攻击是利用TCP三次握手过程。这里可以分为两种。
第一种：攻击者伪造大量的SYN+ACK包发送给目标主机，目标主机每收到一个SYN+ACK数据包时，都会去自己的TCP连接表中查看有没有与ACK的发送者建立连接 ，如果有则发送ACK包完成TCP连接，如果没有则发送ACK+RST 断开连接。但是在查询过程中会消耗一定的cpu计算资源。如果瞬间收到大量的SYN+ACK数据包，将会消耗服务器的大量cpu资源，导致正常的连接无法建立或增加延迟，甚至造成服务器瘫痪、死机。

第二种：利用TCP三次握手的ACK+SYN应答，攻击者向不同的服务器发送大量的SYN请求，这些SYN请求数据包的源IP均为受害主机IP，这样就会有大量的SYN+ACK应答数据包发往受害主机，从而占用目标的网络带宽资源，形成拒绝服务。


- TCP RST Flood 


#### UDP

- UDP Flood

UDP协议与TCP协议不同， UDP是一个无连接协议。使用UDP协议传输数据之前，客户端和服务器之间不建立连接，UDP Flood属于带宽类攻击，黑客们通过僵尸网络向目标服务器发起大量的UDP报文，可以使用小数据包(64字节)进行攻击,也可以使用大数据包(大于1500字节,以太网MTU为1500字节)进行攻击。大量小数据包会增大网络设备处理数据包的压力；而对于大数据包，网络设备需要进行分片、重组，迅速造成链路拥塞


#### ICMP

- ICMP Echo Flood     
ICMP协议位于IP层，主要通过含有ICMP功能的主机与路由器之间发送ICMP数据包，来达到实现信息查询和错误通知的功能。因此攻击者利用icmp获取主机信息，时间、路由信息等。所以为攻击者创造了极大得便利条件。攻击者通过足够快的数据包速度和足够的带宽，对目标发出攻击请求，造成网络拥堵。

- ICMP Blacknurse  

BlackNurse攻击基于Type3（Destination Unreachable） Code3（Port Unreachable）——端口不可达，当目标端口不可达，所发出的ICMP包都会返回源。攻击者可以通过发这种特定的ICMP包令大多数服务器防火墙的CPU过载。一旦设备抛弃的包到了临界值15Mbps至18Mbps（每秒4万到5万个包），设备就会直接停止响应。


- ICMP Smurf攻击

攻击者向网关发送ICMP请求包，并将该ICMP请求报文的源地址伪造成受害主机IP地址，目的地址为广播地址。路由器在接受到该数据包，发现目的地址是广播地址，就会将该数据包广播出去，局域网内所有的存活主机都会受到一个ICMP请求包，源地址是受害主机IP。接下来受害主机就会收到该网络内所有主机发来的ICMP应答报文，通过大量返回的ICMP应答报文来淹没受害主机，最终导致网络阻塞，受害主机崩溃。


#### 应用层反射

- DNS 反射   (放大倍数28 to 54）
- NTP 反射  (放大倍数556.9）
-  Memcached 反射（放大倍数10,000 to 51,000）
-  等等（LDAP反射/TFTP反射/SSDP反射/SNMP反射）



´´