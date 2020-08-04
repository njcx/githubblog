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

DGA是恶意程序所使用的一种DNS技术，用于隐藏C2服务器。恶意软件通常使用它们来逃避基于域名的防火墙、NIDS拦截。使用DGA的恶意软件将不断尝试连接生成的DGA域名列表里面的域名，直到完成C2通信。DGA算法最早是在2008年的Conficker恶意软件中发现的。Conficker的第一个变体（变体A）每天使用日期作为种子来产生250个不同的域名。后来FBI进行了报复，逆向了Conficker，并注册恶意软件使用的所有域（真的假的？）。随着Conficker恶意软件的发展，引入了另外4种恶意软件变体（从B到E），变体C每天生成超过50,000个域，从中随机选择仅500个域以尝试与C&C服务器进行通信。

![botnet1](../images/botnets1.png)

传统僵尸网络基础架构

![botnet2](../images/botnets2.png)

DGA僵尸网络基础架构


Banjori  DGA 域名生成

```python

def map_to_lowercase_letter(s):
    return ord('a') + ((s - ord('a')) % 26)

def next_domain(domain):
    dl = [ord(x) for x in list(domain)]
    dl[0] = map_to_lowercase_letter(dl[0] + dl[3])
    dl[1] = map_to_lowercase_letter(dl[0] + 2*dl[1])
    dl[2] = map_to_lowercase_letter(dl[0] + dl[2] - 1)
    dl[3] = map_to_lowercase_letter(dl[1] + dl[2] + dl[3])
    return ''.join([chr(x) for x in dl])

seed = 'earnestnessbiophysicalohax.com' # 15372 equal to 0 (seed = 0)
domain = seed
for i in range(1000):
    print(domain)
    domain = next_domain(domain)

```

```bash

zfrpestnessbiophysicalohax.com
hdquestnessbiophysicalohax.com
umcuestnessbiophysicalohax.com
hrbyestnessbiophysicalohax.com
ysrtestnessbiophysicalohax.com
kgteestnessbiophysicalohax.com
hfsnestnessbiophysicalohax.com
njxfestnessbiophysicalohax.com
lpagestnessbiophysicalohax.com
kacuestnessbiophysicalohax.com

```


DGA的优点

1、使用DGA的僵尸网络有较为健壮的寻址方式，可对抗DNS域名黑名单拦截、态势感知系统以及特征码检测系统。
2、DGA是一种理想的备用信道，可作为back up手段恢复僵尸网络控制。

DGA的缺点

1、需要逐一遍历DGA，寻址效率低。
2、大量NX Domain流量导致通信易被检测发现。
3、如果DGA数量过多，出于时间和金钱成本开销，攻击者难以全部注册，安全人员可以抢注并通过sink hole手段劫持僵尸网络



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








