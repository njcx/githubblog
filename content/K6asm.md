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

https://weedser.ctfile.com/file/59675503

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

![asm](../images/asm.jpeg)