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
第一种：攻击者伪造大量的SYN+ACK包发送给目标主机，目标主机每收到一个SYN+ACK数据包时，都会去自己的TCP连接表中查看有没有与ACK的发送者建立连接 ，如果有则发送ACK包完成TCP连接，如果没有则发送ACK+RST 断开连接。但是在查询过程中会消耗一定的CUP计算资源。如果瞬间收到大量的SYN+ACK数据包，将会消耗服务器的大量cpu资源，导致正常的连接无法建立或增加延迟，甚至造成服务器瘫痪、死机。

第二种：利用TCP三次握手的ACK+SYN应答，攻击者向不同的服务器发送大量的SYN请求，这些SYN请求数据包的源IP均为受害主机IP，这样就会有大量的SYN+ACK应答数据包发往受害主机，从而占用目标的网络带宽资源，形成拒绝服务。


- TCP RST Flood 


#### UDP

- UDP Flood

#### ICMP

- ICMP Echo Flood     

- ICMP Blacknurse  


#### 应用层反射

- DNS 反射   (放大倍数28 to 54）
- NTP 反射  (放大倍数556.9）
-  Memcached 反射（放大倍数10,000 to 51,000）
-  等等（LDAP/TFTP/SSDP/SNMP）



