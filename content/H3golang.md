Title: golang快速入门
Date: 2018-06-02 13:20
Modified: 2018-06-02 13:20
Category: 编程语言
Tags: golang
Slug: H3
Authors: nJcx
Summary: golang学习后，转化成教程，方便大家阅读


##### 介绍

Go语言是谷歌与09年开源的一门编译型编程语言，其专门针对多处理器系统应用程序的编程进行了优化，支持并行进程，自动垃圾回收。Docker就是go语言所编写。


#### 安装
mac 电脑安装

```bash
brew install golang
```
ubuntu

```bash
sudo apt-get install golang -y

```
CentOS 

```bash
yum install golang -y

```

#### 向世界打招呼


```bash
package main 

import "fmt"

func main() {
    fmt.Println("Hello world!")
}
```

####注释

```bash

// 单行注释

/*
 我是多行注释
 我是多行注释
 我是多行注释
 我是多行注释
 我是多行注释
 */
```
 
####  数据结构


- 布尔型

```bash
    var b bool = true
    c := false
```
- 数字类型
整型 int 和浮点型 float32、float64，Go 语言支持整型和浮点型数字，支持复数，位运算采用补码。
 	- uint8
	无符号 8 位整型 (0 到 255)
	- uint16
  无符号 16 位整型 (0 到 65535)
	- uint32
无符号 32 位整型 (0 到 4294967295)
	- uint64
无符号 64 位整型 (0 到 18446744073709551615)
	- int8
有符号 8 位整型 (-128 到 127)
	- int16
有符号 16 位整型 (-32768 到 32767)
	- int32
有符号 32 位整型 (-2147483648 到 2147483647)
	- int64
有符号 64 位整型 (-9223372036854775808 到 9223372036854775807)
	- float32
IEEE-754 32位浮点型数
	- float64
IEEE-754 64位浮点型数
	- complex64
32 位实数和虚数
	- complex128
64 位实数和虚数
	- byte
类似 uint8
	- rune
类似 int32
	- uint
32 或 64 位
	- int
与 uint 一样大小
	- uintptr
无符号整型，用于存放一个指针

变量

```bash

var a = 1

var b int = 2

c :=3

```

常量

```bash

const identifier [type] = value

显式类型定义： const b string = "abc"
隐式类型定义： const b = "abc"

多个类型定义： const c_name1, c_name2 = value1, value2
```

- 字符串类型

```bash
    var b string = "demo"
    c :=  "godemo"
```
- 数组类型

```bash

//第一种
var arr [2]int
    arr[0]=1
    arr[1]=2

//第二种

var arr = [2]int{1,2}
arr := [2]int{1,2}

//第三种

var arr = [...]int{1,2}
arr := [...]int{1,2}

//第四种
{索引1:元素1,索引2:元素2,...}
var arr = [...]int{1:1,0:2}
arr := [...]int{1:1,0:2}

```

- 切片类型


- 指针类型（Pointer）

指针类型就是一个变量，里面存的是另一个变量的地址


```bash
var b *int

b = &a

var b *int = &a

b := &a

```

```bash

package main 

import "fmt"

func main(){

	var a int = 1
	
	var b *int =&a

	fmt.Println(*b)
}

```
- 结构体类型(struct)

- Channel 类型

- 函数类型

- 接口类型（interface）

- Map 类型


#### 运算符
算术运算符

``` bash

+	相加	
-	相减	
*	相乘	
/	相除	
%	求余	
++	自增	
--	自减	

```

关系运算符

```bash
==	检查两个值是否相等，如果相等返回 True 否则返回 False。
!=	检查两个值是否不相等，如果不相等返回 True 否则返回 False。
>	检查左边值是否大于右边值，如果是返回 True 否则返回 False。
>=	检查左边值是否大于等于右边值，如果是返回 True 否则返回 False。
<=	检查左边值是否小于等于右边值，如果是返回 True 否则返回 False。
```

逻辑运算符

```bash

&&	逻辑 AND 运算符。 如果两边的操作数都是 True，则条件 True，否则为 False。
||	逻辑 OR 运算符。 如果两边的操作数有一个 True，则条件 True，否则为 False。
!	逻辑 NOT 运算符。 如果条件为 True，则逻辑 NOT 条件 False，否则为 True。

```

赋值运算符

```bash

=	简单的赋值运算符，将一个表达式的值赋给一个左值
+=	相加后再赋值	C += A 等于 C = C + A
-=	相减后再赋值	C -= A 等于 C = C - A
*=	相乘后再赋值	C *= A 等于 C = C * A
/=	相除后再赋值	C /= A 等于 C = C / A
%=	求余后再赋值   C %= A 等于 C = C % A

```


指针相关运算符

```bash

&	返回变量存储地址	&a; 将给出变量的实际地址。
*	指针变量。	*a; 是一个指针变量

```


#### 控制语句

- 条件语句

```bash

if 布尔表达式 {
   /* 在布尔表达式为 true 时执行 */
}

if 布尔表达式 {
   /* 在布尔表达式为 true 时执行 */
} else {
  /* 在布尔表达式为 false 时执行 */
}

if 布尔表达式 1 {
   /* 在布尔表达式 1 为 true 时执行 */
   if 布尔表达式 2 {
      /* 在布尔表达式 2 为 true 时执行 */
   }
}



```

for 循环

```bash

Go语言的For循环有3中形式，只有其中的一种使用分号。

和 C 语言的 for 一样：

for init; condition; post { }
和 C 的 while 一样：

for condition { }
和 C 的 for(;;) 一样：

for { }
init： 一般为赋值表达式，给控制变量赋初值；
condition： 关系表达式或逻辑表达式，循环控制条件；
post： 一般为赋值表达式，给控制变量增量或减量。

```

for 循环的 range 格式可以对 slice、map、数组、字符串等进行迭代循环。格式如下：

```bash

for key, value := range oldMap {
    newMap[key] = value
}


```

for 例子

```bash

package main

import "fmt"

func main() {

   var b int = 15
   var a int

   numbers := [6]int{1, 2, 3, 5} 

   /* for 循环 */
   for a := 0; a < 10; a++ {
      fmt.Printf("a 的值为: %d\n", a)
   }

   for a < b {
      a++
      fmt.Printf("a 的值为: %d\n", a)
   }

   for i,x:= range numbers {
      fmt.Printf("第 %d 位 x 的值 = %d\n", i,x)
   }   
}
```
for 无限循环

```bash
package main

import "fmt"

func main() {
    for true  {
        fmt.Printf("这是无限循环。\n");
    }
}

```

break 语句

```bash

package main

import "fmt"

func main() {
   /* 定义局部变量 */
   var a int = 10

   /* for 循环 */
   for a < 20 {
      fmt.Printf("a 的值为 : %d\n", a);
      a++;
      if a > 15 {
         /* 使用 break 语句跳出循环 */
         break;
      }
   }
}

```

```bash


import "fmt"

func main() {
   /* 定义局部变量 */
   var a int = 10

   /* for 循环 */
   for a < 20 {
      if a == 15 {
         /* 跳过此次循环 */
         a = a + 1;
         continue;
      }
      fmt.Printf("a 的值为 : %d\n", a);
      a++;     
   }  
}

```

#### 函数

#### GO IO

#### GO异常处理

#### GO 并发

#### 标准库



