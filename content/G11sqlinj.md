Title: SQL注入记录
Date: 2017-05-22 13:20
Modified: 2017-05-22 13:20
Category: 安全
Tags: SQLI
Slug: G11
Authors: nJcx
Summary: 记录一下学习SQL注入的心路
Status: draft
#### 原理

没有过滤敏感字符，绑定变量，导致攻击者可以通过sql灵活多变的语法，构造精心巧妙的语句，不择手段，达成目的，或者通过系统报错，返回对自己有用的信息。

#### 数字型注入

http://www.test.com/test.php?id=8

我们通过get 传入 id为8的参数，如果对id 没有过滤，那么id就可能传入任何参数，底层的对应的SQL如下

select * from table where id=8

先加个 '，看看是否正常，

```bash

http://www.test.com/test.php?id=8 and 1=1
select * from table where id=8 and 1=1


http://www.test.com/test.php?id=8 and 1=2
select * from table where id=8 and 1=2

```
看看加上 and 1=2 是否正常，如果出现异常，可能出现SQL注入漏洞

#### 字符型注入
http://www.test.com/test.php?user=njcx

select * from table where user='njcx'

字符型注入跟数字型注入的区别在字符型注入需要闭合,参数变了，"njcx' and 1=1--"

当然，也可以出现双闭合

```bash

http://www.test.com/test.php?user=njcx' and 1=1-- 
select * from table where user='njcx' and 1=1--'

http://www.test.com/test.php?user=njcx' and 1=2-- 
select * from table where user='njcx' and 1=2--'
```
看看加上 and 1=2 是否正常，如果出现异常，可能出现SQL注入漏洞，
#### 注入方式


#### 检测


#### 防范