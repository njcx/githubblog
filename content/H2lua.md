Title: lua快速入门
Date: 2018-06-01 13:20
Modified: 2018-06-01 13:20
Category: lua
Tags: lua
Slug: H2
Authors: nJcx
Summary: lua学习后，转化成教程，方便大家阅读
Status: draft
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

两个减号是单行注释:

-- 单行注释

--[[多行注释

多行注释--]]
 
 
#### 数据结构

- nil  表示一个无效值， 在条件表达式中相当于false
- boolean	包含两个值：false和true
- number	表示双精度类型的实浮点数
- string	字符串由一对双引号或单引号来表示 (通过'..'连接字符串，通过# 取得字符串长度)
- table	table是一个"关联数组"（associative arrays），数组的索引可以是数字或者是字符串。在 Lua 里，table构造表达式是{}，用来创建一个空表


```lua

> print(#"www.njcx.bid")
12
> 
```

#### 变量,循环,流程控制

- 变量

Lua 变量有三种类型：全局变量、局部变量、表中的域。
Lua 中的变量全是全局变量，那怕是语句块或是函数里，除非用 local 显式声明为局部变量。局部变量的作用域为从声明位置开始到所在语句块结束。变量的默认值均为 nil。

```lua
a = 5               -- 全局变量
local b = 5         -- 局部变量

function joke()
    c = 5           -- 全局变量
    local d = 6     -- 局部变量
end
joke()
print(c,d)          --> 5 nil

```

- 循环

while

```lua
a=10
while( a < 20 )
do
   print("a 的值为:", a)
   a = a+1
end

while( true )
do
   print("循环将永远执行下去")
end
```

for  

```lua
for var=exp1,exp2,exp3 do  
    <执行体>  
end  
var 从 exp1 变化到 exp2，每次变化以 exp3 为步长递增 var，并执行一次 "执行体"。exp3 是可选的，如果不指定，默认为1。

for i=1,f(x) do
    print(i)
end
 
for i=10,1,-1 do
    print(i)
end

```

```lua

days={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}  
for i,v in ipairs(days) do 
	print(v) 
end  

```
这里提一下pairs能够遍历表中全部的key，而ipairs则不能返回nil,遇到nil则退出。


- repeat

```lua
--[ 变量定义 --]
a = 10
--[ 执行循环 --]
repeat
   print("a的值为:", a)
   a = a + 1
until( a > 15 )

```