Title: 汇编学习总结
Date: 2018-06-01 15:30
Modified: 2018-06-01 15:30
Category: 编程语言
Tags: 汇编
Slug: K6
Authors: nJcx
Summary: 汇编学习总结
Status: draft

#### 介绍

#### 安装
笔者电脑： Mac + VMware + winxp + masm

```bash
masm for windows版本

http://sqdownb.onlinedown.net/down/masm2015.rar

深度技术_Windows_XP_SP3_完美精简安装版小盘_v6

http://2783079.ch3.data.tv002.com/down/2db7a208418b86f8ef8a3e772f63abb3-226689024/%E6%B7%B1%E5%BA%A6%E6%8A%80%E6%9C%AF_Windows_XP_SP3_%E5%AE%8C%E7%BE%8E%E7%B2%BE%E7%AE%80%E5%AE%89%E8%A3%85%E7%89%88%E5%B0%8F%E7%9B%98_v6.iso?cts=f-D203A156A222A100F8690f&ctp=203A156A222A100&ctt=1544726207&limit=1&spd=0&ctk=e4817236abaaee01e01a4d35de4926c0&chk=2db7a208418b86f8ef8a3e772f63abb3-226689024&mtd=1
```

```bash
;计算2^12
assume cs:code
code segment
start:  mov ax,2
        mov cx,11
      p:add,ax,ax       
        loop p;p是标号
              
       mov ax,4c00H;masm默认数字是十进制
       int 21H
code ends
end start

;编程计算123*236，结果放在ax中
assume cs:code
code segment
start:mov ax,0
      mov cx,236
   an:add ax,123
     loop an
      mov ax,4c00H
      int 21H
code ends
end start
```