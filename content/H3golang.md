Title: golang快速入门
Date: 2018-06-02 13:20
Modified: 2018-06-02 13:20
Category: golang
Tags: golang
Slug: H3
Authors: nJcx
Summary: golang学习后，转化成教程，方便大家阅读

##### 介绍

Go语言是谷歌与09年开源的一门编译型编程语言，其专门针对多处理器系统应用程序的编程进行了优化，支持并行进程，自动垃圾回收。Docker就是go语言所编写。


#### 安装
mac 电脑安装

```bash
brew install go
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


```go
package main 

import "fmt"

func main() {
    fmt.Println("Hello world!")
}
```
####  数据结构


- 布尔型

```go
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

```go

var a = 1

var b int = 2

c :=3

```

- 字符串类型

```go
    var b string = "demo"
    c :=  "godemo"
```
- 数组类型

```go

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


```go
var b *int

b = &a

var b *int = &a

b := &a

```

```go

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

