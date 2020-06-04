Title: Windows环境的下提权方式总结
Date: 2018-06-14 03:20
Modified: 2018-06-14 03:20
Category: 安全
Tags: Windows
Slug: O5
Authors: nJcx
Summary: Windows环境的下提权方式总结~

#### 安装

工具镇楼：

```bash
https://github.com/SecWiki/windows-kernel-exploits

https://github.com/AonCyberLabs/Windows-Exploit-Suggester  //比较老了，可以考虑用下面的

https://github.com/johnchakauya/wesng.git

https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS

https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc

https://github.com/rasta-mouse/Watson

https://github.com/GhostPack/Seatbelt

https://github.com/411Hall/JAWS


```


1， 系统内核溢出漏洞提权

```bash

#手工查找补丁情况
systeminfo
Wmic qfe get Caption,Description,HotFixID,InstalledOn

#MSF后渗透扫描
post/windows/gather/enum_patches

#Powershell扫描
Import-Module C:\Sherlock.ps1
Find-AllVulns

#Empire内置模块
usemodule privesc/powerup/allchecks
execute


```
2，系统配置错误提权


3， DLL 劫持提权


4， 令牌窃取


5，组策略首选项提权


6， 绕过UAC提权