Title: lua快速入门
Date: 2018-06-01 13:20
Modified: 2018-06-01 13:20
Category: lua
Tags: lua
Slug: H2
Authors: nJcx
Summary: lua学习后，转化成教程，方便大家阅读

##### 介绍

Lua 是一脚本语言，巴西人所开发。由标准C开发，方便嵌入应用程序中。几乎可以在所有操作系统和平台上都可以编译，运行。

#### 安装

```bash
$ brew install lua
# yum install lua -y
$ sudo apt-get -y install lua
```

包管理

```bash

$ brew install luarocks

```

常用包

```bash
luarocks install luasocket
luarocks install luasql-sqlite3
luarocks install lpeg
luarocks install lzlib
luarocks install luafilesystem
luarocks install luasec
luarocks install md5
luarocks install luacurl
luarocks install luasql-mysql 
luarocks install lua-cjson

```

#### hello world

老规矩

```lua
#!/usr/local/bin/lua

print("Hello World！")
```

#### 数据结构




