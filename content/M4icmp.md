Title: NIDS 中的 ICMP隐蔽隧道检测
Date: 2018-07-07 20:20
Modified: 2018-07-07 20:20
Category: 安全
Tags: nids
Slug: M4
Authors: nJcx
Summary:  NIDS 中的 ICMP隐蔽隧道检测 ~


#### 介绍

![icmp](../images/tcpip.gif)

我们先介绍一下 ICMP协议，ICMP的内容是放在ip数据包的数据部分里传输的，ICMP是基于IP协议工作的，我们要区别于传输层，它仍然属于网络层协议。ICMP报文包含在IP数据报中，IP报头在ICMP报文的最前面。一个ICMP报文包括IP报头（至少20字节）、ICMP报头（至少八字节）和ICMP报文（属于ICMP报文的数据部分）。当IP报头中的协议字段值为1时，就说明这是一个ICMP报文。ICMP报文如下图所示：

![icmp](../images/icmp.png)

![icmp](../images/icmpfield.png)


从上图看，也就是说，我们重点关注 Checksum 字段和Data字段，因为我们改变Data字段的时候，Checksum也要改变,我们把我们的payload或者数据放到Data字段里面即可.我们分别使用，Linux和Windows测试一下， Linux ping 发出的Data的内容为 ：!\"#$%&'()*+,-./01234567  ， Windows ping 的发出的Data的内容为 abcdefghijklmnopqrstuvwabcdefghi

如图，我们用wireshark抓的包

![icmp](../images/wiresharkicmp.jpeg)


#### 安装

我们测试一下，Linux 的icmp 的隐藏后门[ish](https://sourceforge.net/projects/icmpshell/files/ish/)，如果是Windows，推荐 [icmpsh](https://github.com/inquisb/icmpsh)， 

受控机CentOS7 ：172.19.25.53

控制机Parrot Linux ：172.19.25.73

我们在受控机上编译（make linux），启动 ishd，在控制机上启动 ./ish 172.19.25.53

![icmp](../images/ish.jpeg)

我们可以在 Data 里面可以看到一个ls

![icmp](../images/ishwireshark.jpeg)

我们可以在响应里面发现 相关目录的数据

![icmp](../images/wireshark1.jpeg)


可以看出，payload 是放在Data字段的

我们总结一下ICMP隐蔽隧道的特征：

1、ICMP隧道短时间会产生大量 ICMP 数据包，用来数据发送，可能存在大于 64 比特的数据包。

2、ICMP隧道发送的 ICMP 数据包前后Data字段不一样，而且响应数据包中 payload 跟请求数据包不一致。

3、ICMP 数据包的协议标签可能存在特殊字段。例如，icmptunnel 会在所有的 ICMP Data 前面增加 ‘TUNL’ 标记以用于识别隧道

4，Data 里面可能存在一些系统命令


防御和检测手段：

1，禁止 ping（不太可能），会影响到很多运维和安全检测设备的运行。

2，ICMP Data字段 形成一个白名单，不在白名单内的告警

```
pass icmp any any -> any any (msg:"Whitecap: OSX or Linux ICMP Echo Request"; icode:0; itype:8; dsize:56; content:"!\"#$%&'()*+,-./01234567"; classtype:misc-activity; sid:5110001; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: OSX or Linux ICMP Echo Reply"; icode:0; itype:0; dsize:56; content:"!\"#$%&'()*+,-./01234567"; classtype:misc-activity; sid:5110002; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Windows XP/7/8 ICMP Echo Request"; icode:0; itype:8; dsize:32; content:"abcdefghijklmnopqrstuvwabcdefghi"; classtype:misc-activity; sid:5110003; rev:1; nocase;)
pass icmp any any -> any any (msg:"Whitecap: Windows XP/7/8 ICMP Echo Reply"; icode:0; itype:0; dsize:32; content:"abcdefghijklmnopqrstuvwabcdefghi"; classtype:misc-activity; sid:5110004; rev:1; nocase;)
pass icmp any any -> any any (msg:"Whitecap: Nmap ICMP Echo Request"; icode:0; itype:8; dsize:0; classtype:misc-activity; sid:5110005; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Nmap ICMP Echo Reply"; icode:0; itype:0; dsize:0; classtype:misc-activity; sid:5110006; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Group Policy Slow Link Detection"; icode:0; itype:8; dsize:>1400; content:"WANG2"; classtype:misc-activity; sid:5110007; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Group Policy Slow Link Detection"; icode:0; itype:0; dsize:>1400; content:"WANG2"; classtype:misc-activity; sid:5110008; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Solarwinds Status Query"; icode:0; itype:8; dsize:23; content:"SolarWinds Status Query"; classtype:misc-activity; sid:5110009; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Solarwinds Status Query"; icode:0; itype:0; dsize:23; content:"SolarWinds Status Query"; classtype:misc-activity; sid:5110010; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Domain Controller ICMP Traffic"; icode:0; itype:8; dsize:1; content:"?"; classtype:misc-activity; sid:5110011; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Domain Controller ICMP Traffic"; icode:0; itype:0; dsize:1; content:"?"; classtype:misc-activity; sid:5110012; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: McAfee ICMP ping Request"; icode:0; itype:8; dsize:36; content:"EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"; offset:3; classtype:misc-activity; sid:5110013; rev:2;)
pass icmp any any -> any any (msg:"Whitecap: McAfee ICMP ping Reply"; icode:0; itype:0; dsize:36; content:"EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"; offset:3; classtype:misc-activity; sid:5110014; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Lots of Xs"; icode:0; itype:8; dsize:32; content:"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"; classtype:misc-activity; sid:5110015; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Lots of Xs"; icode:0; itype:0; dsize:32; content:"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"; classtype:misc-activity; sid:5110016; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: DHCP ICMP Duplicate IP Check"; icode:0; itype:8; dsize:11; content:"DhcpIcmpChk"; classtype:misc-activity; sid:5110017; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: DHCP ICMP Duplicate IP Check"; icode:0; itype:0; dsize:11; content:"DhcpIcmpChk"; classtype:misc-activity; sid:5110018; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Solarwinds ICMP Version 5"; icode:0; itype:8; dsize:<80; content:"SolarWinds.Net ICMP Version 5.0.4.16Copyright  1995-2005 SolarWinds.Net"; classtype:misc-activity; sid:5110019; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Solarwinds ICMP Version 5"; icode:0; itype:0; dsize:<80; content:"SolarWinds.Net ICMP Version 5.0.4.16Copyright  1995-2005 SolarWinds.Net"; classtype:misc-activity; sid:5110020; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Solarwinds Sonar ICMP Scan"; icode:0; itype:8; dsize:24; content:"Orion Network Sonar Scan"; classtype:misc-activity; sid:5110021; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: Solarwinds Sonar ICMP Scan"; icode:0; itype:0; dsize:24; content:"Orion Network Sonar Scan"; classtype:misc-activity; sid:5110022; rev:1;)
pass icmp any any -> $DNS_SERVERS any (msg:"Whitecap: ICMP to DNS Servers"; icode:0; itype:8; dsize:<57; classtype:misc-activity; threshold:type limit, track by_src, count 1, seconds 60; sid:5110500; rev:2;) 
pass icmp any any -> $DNS_SERVERS any (msg:"Whitecap: ICMP to DNS Servers"; icode:0; itype:0; dsize:<57; classtype:misc-activity; threshold:type limit, track by_src, count 1, seconds 60; sid:5110501; rev:2;) 
pass icmp any any -> any any (msg:"Whitecap: Domain controller to domain controller"; icode:0; itype:8; dsize:32; content:"|00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00|"; classtype:misc-activity; threshold:type limit, track by_src, count 1, seconds 60; sid:5110502; rev:2;)
pass icmp any any -> any any (msg:"Whitecap: Domain controller to domain controller"; icode:0; itype:0; dsize:32; content:"|00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00|"; classtype:misc-activity; threshold:type limit, track by_src, count 1, seconds 60; sid:5110503; rev:2;)
pass icmp any any -> any any (msg:"Whitecap: All As"; icode:0; itype:8; dsize:64; content:"|AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA|"; classtype:misc-activity; sid:5110504; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: All As"; icode:0; itype:0; dsize:64; content:"|AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA|"; classtype:misc-activity; sid:5110505; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: All 0s"; icode:0; itype:8; dsize:56; content:"|00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00|"; classtype:misc-activity; sid:5110506; rev:1;)
pass icmp any any -> any any (msg:"Whitecap: All 0s"; icode:0; itype:0; dsize:56; content:"|00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00|"; classtype:misc-activity; sid:5110507; rev:1;)
pass icmp [$ICMP_SRC_HOSTS_IGNORE] any -> any any (msg:"ICMP Pass: Ignore Hosts"; icode:0; itype:8; classtype:misc-activity; sid:5111000; rev:1;)
pass icmp [$ICMP_SRC_HOSTS_IGNORE] any -> any any (msg:"ICMP Pass: Ignore Hosts"; icode:0; itype:0; classtype:misc-activity; sid:5111001; rev:1;)
pass icmp any any -> [$ICMP_DST_HOSTS_IGNORE] any (msg:"ICMP Pass: Ignore Hosts"; icode:0; itype:8; classtype:misc-activity; sid:5111002; rev:1;)
pass icmp any any -> [$ICMP_DST_HOSTS_IGNORE] any (msg:"ICMP Pass: Ignore Hosts"; icode:0; itype:0; classtype:misc-activity; sid:5111003; rev:1;)
```

3,检测包大于多少，或者发送频率高于某个数，报警


```
alert icmp any any -> any any (msg:"Whitecap Echo Request Payload > 100 bytes"; icode:0; itype:8; dsize:>100; classtype:misc-activity; sid:5113000; rev:1;)
alert icmp any any -> any any (msg:"Whitecap Echo Reply Payload > 100 bytes"; icode:0; itype:0; dsize:>100; classtype:misc-activity; sid:5113001; rev:1;)
```

4, 检测 Data里面包含的特殊字段报警（例子是检测base64）

```
drop icmp any any -> any any (msg:"LOCAL ICMP Large ICMP Packet (Base64)"; dsize:>800; content:"="; pcre:"/^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$/"; reference:url,www.notsosecure.com/2015/10/15/icmp-tunnels-a-case-study/; classtype:bad-unknown; sid:1000028; rev:1;)
```