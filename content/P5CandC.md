Title: C&C的一些隐藏策略与防丢失
Date: 2018-06-07 02:01
Modified: 2018-06-07 02:01
Category: 安全
Tags: C&C
Slug: P5
Authors: nJcx
Summary: C&C的一些隐藏策略与防丢失~



#### 

```bash
https://github.com/alphaSeclab/awesome-rat.git
https://github.com/malwaredllc/byob.git
https://github.com/sweetsoftware/Ares.git
https://github.com/UBoat-Botnet/UBoat.git
https://github.com/sin5678/gh0st.git
https://github.com/alibawazeeer/rat-njrat-0.7d-modded-source-code.git
https://github.com/NYAN-x-CAT/RevengeRAT-Stub-CSsharp.git
```


#### 各种隧道，加密（icmp隧道/ssh隧道/dns隧道/http隧道）


#### DGA 算法

DGA的优点

1、使用DGA的僵尸网络有较为健壮的寻址方式，可对抗域名黑名单屏蔽、静态声望系统以及特征码检测系统。
2、DGA是一种理想的备用信道，可作为back up手段恢复僵尸网络控制，如Zeus v3。

DGA的缺点

1、需要逐一便利AGD，寻址效率低。
2、大量NXDomain流量导致通信易被检测发现。
3、如果AGD数量过多，出于时间和金钱成本开销，攻击者难以全部注册，防御人员可以抢注并通过sinkhole手段测量或劫持僵尸网络



#### 利用一些在线网站或者程序做为C2 Server


比如， gmail，github，twitter，telegram等等


```bash

https://github.com/maldevel/gdog

```
用Gmail 做C2 Server


```bash

https://github.com/maldevel/canisrufus

```

用Github 做C2 Server


```bash

https://github.com/blazeinfosec/bt2

```
用telegram 做C2 Server








