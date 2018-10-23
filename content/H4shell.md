Title: shell编程快速入门
Date: 2018-06-03 13:20
Modified: 2018-06-03 13:20
Category: shell
Tags: shell
Slug: H4
Authors: nJcx
Summary: bash编程学习后，转化成教程，方便大家阅读

##### 介绍

Shell 是一个用C语言编写的程序，它是用户使用Linux的桥梁。Shell 既是一种命令语言，又是一种程序设计语言。通过编写shell脚本，来控制系统的运行。

#### 安装

一般不需要安装,通常位于以下目录：

```bash
Bourne Shell（/usr/bin/sh或/bin/sh）
Bourne Again Shell（/bin/bash）
```

#### 向世界打招呼

```bash 

# touch demo.sh && echo " echo 'hello its me'" >> demo.sh
 
# sh demo.sh 

# hello its me
```

