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

切片就是动态数组

```bash
var identifier []type
```

```bash
s :=[] int {1,2,3 } 

```

切片也可以通过make 创建，其中，len 是数组的长度并且也是切片的初始长度，cap 是切片容量
```bash

s :=make([]int,len,cap) 

```

切片使用的例子

```bash

package main

import "fmt"

func main() {
   /* 创建切片 */
   numbers := []int{0,1,2,3,4,5,6,7,8}   
   printSlice(numbers)

   /* 打印原始切片 */
   fmt.Println("numbers ==", numbers)

   /* 打印子切片从索引1(包含) 到索引4(不包含)*/
   fmt.Println("numbers[1:4] ==", numbers[1:4])

   /* 默认下限为 0*/
   fmt.Println("numbers[:3] ==", numbers[:3])

   /* 默认上限为 len(s)*/
   fmt.Println("numbers[4:] ==", numbers[4:])

   numbers1 := make([]int,0,5)
   printSlice(numbers1)

   /* 打印子切片从索引  0(包含) 到索引 2(不包含) */
   number2 := numbers[:2]
   printSlice(number2)

   /* 打印子切片从索引 2(包含) 到索引 5(不包含) */
   number3 := numbers[2:5]
   printSlice(number3)

}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}

```
执行以上代码输出结果为：

```bash
len=9 cap=9 slice=[0 1 2 3 4 5 6 7 8]
numbers == [0 1 2 3 4 5 6 7 8]
numbers[1:4] == [1 2 3]
numbers[:3] == [0 1 2]
numbers[4:] == [4 5 6 7 8]
len=0 cap=5 slice=[]
len=2 cap=9 slice=[0 1]
len=3 cap=7 slice=[2 3 4]

```

如果想增加切片的容量，我们必须创建一个新的更大的切片并把原分片的内容都拷贝过来。
下面的代码描述了从拷贝切片的 copy 方法和向切片追加新元素的 append 方法。

```bash

package main

import "fmt"

func main() {
   var numbers []int
   printSlice(numbers)

   /* 允许追加空切片 */
   numbers = append(numbers, 0)
   printSlice(numbers)

   /* 向切片添加一个元素 */
   numbers = append(numbers, 1)
   printSlice(numbers)

   /* 同时添加多个元素 */
   numbers = append(numbers, 2,3,4)
   printSlice(numbers)

   /* 创建切片 numbers1 是之前切片的两倍容量*/
   numbers1 := make([]int, len(numbers), (cap(numbers))*2)

   /* 拷贝 numbers 的内容到 numbers1 */
   copy(numbers1,numbers)
   printSlice(numbers1)   
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}

```

以上代码执行输出结果为：

```bash

len=0 cap=0 slice=[]
len=1 cap=1 slice=[0]
len=2 cap=2 slice=[0 1]
len=5 cap=6 slice=[0 1 2 3 4]
len=5 cap=12 slice=[0 1 2 3 4]

```

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

定义结构体

```bash
type struct_variable_type struct {
   member definition;
   member definition;
   ...
   member definition;
}

```

列子

```bash

type Books struct {
   title string
   author string
   subject string
   book_id int
}

```

如果要访问结构体成员，需要使用点号 . 操作符，格式为：

结构体.成员名

定义指向结构体的指针类似于其他指针变量，格式如下：

var struct_pointer *Books

以上定义的指针变量可以存储结构体变量的地址。查看结构体变量地址，可以将 & 符号放置于结构体变量前：

struct_pointer = &Book1;

使用结构体指针访问结构体成员，使用 "." 操作符：

struct_pointer.title;



- Channel 类型


```bash
ch := chan int // 定义一个chan
ch := make(chan int)  //定义一个chan
ch <- v    // 把 v 发送到通道 ch
v := <-ch  // 从 ch 接收数据
           // 并把值赋给 v
           
```

- 接口类型（interface）

```bash

/* 定义接口 */
type interface_name interface {
   method_name1 [return_type]
   method_name2 [return_type]
   method_name3 [return_type]
   ...
   method_namen [return_type]
}

/* 定义结构体 */
type struct_name struct {
   /* variables */
}

/* 实现接口方法 */
func (struct_name_variable struct_name) method_name1() [return_type] {
   /* 方法实现 */
}
...
func (struct_name_variable struct_name) method_namen() [return_type] {
   /* 方法实现*/
}

```

- Map 类型

```bash

/* 声明变量，默认 map 是 nil */
var map_variable map[key_data_type]value_data_type

/* 使用 make 函数 */
map_variable := make(map[key_data_type]value_data_type)

/ * map 初始化 * /
var map_variable = map[string]string{"key1": "value1","key2": "value2",}


```

- 类型转换

```bash

Go 语言类型转换基本格式如下：
	type_name(expression)
	type_name 为类型，expression 为表达式。

```

- range

range 关键字用于 for 循环中迭代数组(array)、切片(slice)、通道(channel)或集合(map)的元素。在数组和切片中它返回元素的索引和索引对应的值，在map 中返回 key 和 value。

```bash

package main
import "fmt"
func main() {
    //这是我们使用range去求一个slice的和。使用数组跟这个很类似
    nums := []int{2, 3, 4}
    sum := 0
    for _, num := range nums {
        sum += num
    }
    fmt.Println("sum:", sum)
    //在数组上使用range将传入index和值两个变量。上面那个例子我们不需要使用该元素的序号，所以我们使用空白符"_"省略了。有时侯我们确实需要知道它的索引。
    for i, num := range nums {
        if num == 3 {
            fmt.Println("index:", i)
        }
    }
    //range也可以用在map的键值对上。
    kvs := map[string]string{"a": "apple", "b": "banana"}
    for k, v := range kvs {
        fmt.Printf("%s -> %s\n", k, v)
    }
    //range也可以用来枚举Unicode字符串。第一个参数是字符的索引，第二个是字符（Unicode的值）本身。
    for i, c := range "go" {
        fmt.Println(i, c)
    }
}

```



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

continue 语句

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

函数定义 

```bash

func function_name( [parameter list] ) [return_types] {
   函数体
}


```

以下实例为 max() 函数的代码，该函数传入两个整型参数 num1 和 num2，并返回这两个参数的最大值：

```bash
/* 函数返回两个数的最大值 */
func max(num1, num2 int) int {
   /* 声明局部变量 */
   var result int

   if (num1 > num2) {
      result = num1
   } else {
      result = num2
   }
   return result 
}

```

向函数传递数组

```bash
形参设定数组大小：

void myFunction(param [10]int)
{
}

形参未设定数组大小：

void myFunction(param []int)
{
}
```

列子

```bash

func main() {
    var array = []int{1, 2, 3, 4, 5}
    /* 未定义长度的数组只能传给不限制数组长度的函数 */
    setArray(array)
    /* 定义了长度的数组只能传给限制了相同数组长度的函数 */
    var array2 = [5]int{1, 2, 3, 4, 5}
    setArray2(array2)
}

func setArray(params []int) {
    fmt.Println("params array length of setArray is : ", len(params))
}

func setArray2(params [5]int) {
    fmt.Println("params array length of setArray2 is : ", len(params))
}

```

函数可以作为值

```bash
package main

import (
   "fmt"
   "math"
)

func main(){
   /* 声明函数变量 */
   getSquareRoot := func(x float64) float64 {
      return math.Sqrt(x)
   }

   /* 使用函数 */
   fmt.Println(getSquareRoot(9))

}

```

闭包

```bash

package main

import "fmt"

func getSequence() func() int {
   i:=0
   return func() int {
      i+=1
     return i  
   }
}

func main(){
   /* nextNumber 为一个函数，函数 i 为 0 */
   nextNumber := getSequence()  

   /* 调用 nextNumber 函数，i 变量自增 1 并返回 */
   fmt.Println(nextNumber())
   fmt.Println(nextNumber())
   fmt.Println(nextNumber())
   
   /* 创建新的函数 nextNumber1，并查看结果 */
   nextNumber1 := getSequence()  
   fmt.Println(nextNumber1())
   fmt.Println(nextNumber1())
}
```

```bash


package main

import "fmt"
func main() {
    add_func := add(1,2)
    fmt.Println(add_func())
    fmt.Println(add_func())
    fmt.Println(add_func())
}

// 闭包使用方法
func add(x1, x2 int) func()(int,int)  {
    i := 0
    return func() (int,int){
        i++
        return i,x1+x2
    }
}

```

```bash

package main
import "fmt"
func main() {
    add_func := add(1,2)
    fmt.Println(add_func(1,1))
    fmt.Println(add_func(0,0))
    fmt.Println(add_func(2,2))
} 
// 闭包使用方法
func add(x1, x2 int) func(x3 int,x4 int)(int,int,int)  {
    i := 0
    return func(x3 int,x4 int) (int,int,int){ 
       i++
       return i,x1+x2,x3+x4
    }
}

```

#### 接口

```bash
Go 语言提供了另外一种数据类型即接口，它把所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就是实现了这个接口。

实例
/* 定义接口 */
type interface_name interface {
   method_name1 [return_type]
   method_name2 [return_type]
   method_name3 [return_type]
   ...
   method_namen [return_type]
}

/* 定义结构体 */
type struct_name struct {
   /* variables */
}

/* 实现接口方法 */
func (struct_name_variable struct_name) method_name1() [return_type] {
   /* 方法实现 */
}
...
func (struct_name_variable struct_name) method_namen() [return_type] {
   /* 方法实现*/
}

```
例子

```bash
package main

import (
    "fmt"
)

type cat interface {
    ()
}

type NokiaPhone struct {
}

func (nokiaPhone NokiaPhone) call() {
    fmt.Println("I am Nokia, I can call you!")
}

type IPhone struct {
}

func (iPhone IPhone) call() {
    fmt.Println("I am iPhone, I can call you!")
}

func main() {
    var phone Phone

    phone = new(NokiaPhone)
    phone.call()

    phone = new(IPhone)
    phone.call()

}

```

#### 面向对象
面向对象的方法

```bash

package main

import (
   "fmt"  
)

/* 定义结构体 */
type Circle struct {
  radius float64
}

func main() {
  var c1 Circle
  c1.radius = 10.00
  fmt.Println("圆的面积 = ", c1.getArea())
}

//该 method 属于 Circle 类型对象中的方法
func (c Circle) getArea() float64 {
  //c.radius 即为 Circle 类型对象中的属性
  return 3.14 * c.radius * c.radius
}

```

#### GO IO

#### GO异常处理

#### GO 并发

#### 标准库

```bash

archive	    	
     tar	    	tar包实现了tar格式压缩文件的存取.
     zip	    	zip包提供了zip档案文件的读写服务.
bufio	    	bufio 包实现了带缓存的I/O操作.
builtin	    	builtin 包为Go的预声明标识符提供了文档.
bytes	    	bytes包实现了操作[]byte的常用函数.
compress	    	
     bzip2	    	bzip2包实现bzip2的解压缩.
     flate	    	flate包实现了deflate压缩数据格式，参见RFC 1951.
     gzip	    	gzip包实现了gzip格式压缩文件的读写，参见RFC 1952.
     lzw	    	lzw包实现了Lempel-Ziv-Welch数据压缩格式，这是一种T. A. Welch在“A Technique for High-Performance Data Compression”一文（Computer, 17(6) (June 1984), pp 8-19）提出的一种压缩格式.
     zlib	    	zlib包实现了对zlib格式压缩数据的读写，参见RFC 1950.
container	    	
     heap	    	heap包提供了对任意类型（实现了heap.Interface接口）的堆操作.
     list	    	list包实现了双向链表.
     ring	    	ring实现了环形链表的操作.
context	    	Package context defines the Context type, which carries deadlines, cancelation signals, and other request-scoped values across API boundaries and between processes.
crypto	    	crypto包搜集了常用的密码（算法）常量.
     aes	    	aes包实现了AES加密算法，参见U.S. Federal Information Processing Standards Publication 197.
     cipher	    	cipher包实现了多个标准的用于包装底层块加密算法的加密算法实现.
     des	    	des包实现了DES标准和TDEA算法，参见U.S. Federal Information Processing Standards Publication 46-3.
     dsa	    	dsa包实现FIPS 186-3定义的数字签名算法（Digital Signature Algorithm），即DSA算法.
     ecdsa	    	ecdsa包实现了椭圆曲线数字签名算法，参见FIPS 186-3.
     elliptic	    	elliptic包实现了几条覆盖素数有限域的标准椭圆曲线.
     hmac	    	hmac包实现了U.S. Federal Information Processing Standards Publication 198规定的HMAC（加密哈希信息认证码）.
     md5	    	md5包实现了MD5哈希算法，参见RFC 1321.
     rand	    	rand包实现了用于加解密的更安全的随机数生成器.
     rc4	    	rc4包实现了RC4加密算法，参见Bruce Schneier's Applied Cryptography.
     rsa	    	rsa包实现了PKCS#1规定的RSA加密算法.
     sha1	    	sha1包实现了SHA1哈希算法，参见RFC 3174.
     sha256	    	sha256包实现了SHA224和SHA256哈希算法，参见FIPS 180-4.
     sha512	    	sha512包实现了SHA384和SHA512哈希算法，参见FIPS 180-2.
     subtle	    	Package subtle implements functions that are often useful in cryptographic code but require careful thought to use correctly.
     tls	    	tls包实现了TLS 1.2，细节参见RFC 5246.
     x509	    	x509包解析X.509编码的证书和密钥.
          pkix	    	pkix包提供了共享的、低层次的结构体，用于ASN.1解析和X.509证书、CRL、OCSP的序列化.
database	    	
     sql	    	sql 包提供了通用的SQL（或类SQL）数据库接口.
          driver	    	driver包定义了应被数据库驱动实现的接口，这些接口会被sql包使用.
debug	    	
     dwarf	    	Package dwarf provides access to DWARF debugging information loaded from executable files, as defined in the DWARF 2.0 Standard at http://dwarfstd.org/doc/dwarf-2.0.0.pdf
     elf	    	Package elf implements access to ELF object files.
     gosym	    	Package gosym implements access to the Go symbol and line number tables embedded in Go binaries generated by the gc compilers.
     macho	    	Package macho implements access to Mach-O object files.
     pe	    	Package pe implements access to PE (Microsoft Windows Portable Executable) files.
     plan9obj	    	Package plan9obj implements access to Plan 9 a.out object files.
encoding	    	encoding包定义了供其它包使用的可以将数据在字节水平和文本表示之间转换的接口.
     ascii85	    	ascii85 包是对 ascii85 的数据编码的实现.
     asn1	    	asn1包实现了DER编码的ASN.1数据结构的解析，参见ITU-T Rec X.690.
     base32	    	base32包实现了RFC 4648规定的base32编码.
     base64	    	base64实现了RFC 4648规定的base64编码.
     binary	    	binary包实现了简单的数字与字节序列的转换以及变长值的编解码.
     csv	    	csv读写逗号分隔值（csv）的文件.
     gob	    	gob包管理gob流——在编码器（发送器）和解码器（接受器）之间交换的binary值.
     hex	    	hex包实现了16进制字符表示的编解码.
     json	    	json包实现了json对象的编解码，参见RFC 4627.
     pem	    	pem包实现了PEM数据编码（源自保密增强邮件协议）.
     xml	    	Package xml implements a simple XML 1.0 parser that understands XML name spaces.
errors	    	error 包实现了用于错误处理的函数.
expvar	    	expvar包提供了公共变量的标准接口，如服务的操作计数器.
flag	    	flag 包实现命令行标签解析.
fmt	    	fmt 包实现了格式化I/O函数，类似于C的 printf 和 scanf.
go	    	
     ast	    	Package ast declares the types used to represent syntax trees for Go packages.
     build	    	Package build gathers information about Go packages.
     constant	    	Package constant implements Values representing untyped Go constants and their corresponding operations.
     doc	    	Package doc extracts source code documentation from a Go AST.
     format	    	Package format implements standard formatting of Go source.
     importer	    	Package importer provides access to export data importers.
     parser	    	Package parser implements a parser for Go source files.
     printer	    	Package printer implements printing of AST nodes.
     scanner	    	Package scanner implements a scanner for Go source text.
     token	    	Package token defines constants representing the lexical tokens of the Go programming language and basic operations on tokens (printing, predicates).
     types	    	Package types declares the data types and implements the algorithms for type-checking of Go packages.
hash	    	hash包提供hash函数的接口.
     adler32	    	adler32包实现了Adler-32校验和算法，参见RFC 1950.
     crc32	    	crc32包实现了32位循环冗余校验（CRC-32）的校验和算法.
     crc64	    	Package crc64 implements the 64-bit cyclic redundancy check, or CRC-64, checksum.
     fnv	    	fnv包实现了FNV-1和FNV-1a（非加密hash函数）.
html	    	html包提供了用于转义和解转义HTML文本的函数.
     template	    	template包（html/template）实现了数据驱动的模板，用于生成可对抗代码注入的安全HTML输出.
image	    	image实现了基本的2D图片库.
     color	    	color 包实现了基本的颜色库。
          palette	    	palette包提供了标准的调色板.
     draw	    	draw 包提供组装图片的方法.
     gif	    	gif 包实现了GIF图片的解码.
     jpeg	    	jpeg包实现了jpeg格式图像的编解码.
     png	    	png 包实现了PNG图像的编码和解码.
index	    	
     suffixarray	    	suffixarrayb包通过使用内存中的后缀树实现了对数级时间消耗的子字符串搜索.
io	    	io 包为I/O原语提供了基础的接口.
     ioutil	    	ioutil 实现了一些I/O的工具函数。
log	    	log包实现了简单的日志服务.
     syslog	    	syslog包提供一个简单的系统日志服务的接口.
math	    	math 包提供了基本常数和数学函数。
     big	    	big 包实现了（大数的）高精度运算.
     cmplx	    	cmplx 包为复数提供了基本的常量和数学函数.
     rand	    	rand 包实现了伪随机数生成器.
mime	    	mime实现了MIME的部分规定.
     multipart	    	multipart实现了MIME的multipart解析，参见RFC 2046.
     quotedprintable	    	Package quotedprintable implements quoted-printable encoding as specified by RFC 2045.
net	    	net包提供了可移植的网络I/O接口，包括TCP/IP、UDP、域名解析和Unix域socket.
     http	    	http包提供了HTTP客户端和服务端的实现.
          cgi	    	cgi 包实现了RFC3875协议描述的CGI（公共网关接口）.
          cookiejar	    	cookiejar包实现了保管在内存中的符合RFC 6265标准的http.CookieJar接口.
          fcgi	    	fcgi 包实现了FastCGI协议.
          httptest	    	httptest 包提供HTTP测试的单元工具.
          httptrace	    	Package httptrace provides mechanisms to trace the events within HTTP client requests.
          httputil	    	httputil包提供了HTTP公用函数，是对net/http包的更常见函数的补充.
          pprof	    	pprof 包通过提供HTTP服务返回runtime的统计数据，这个数据是以pprof可视化工具规定的返回格式返回的.
     mail	    	mail 包实现了解析邮件消息的功能.
     rpc	    	rpc 包提供了一个方法来通过网络或者其他的I/O连接进入对象的外部方法.
          jsonrpc	    	jsonrpc 包使用了rpc的包实现了一个JSON-RPC的客户端解码器和服务端的解码器.
     smtp	    	smtp包实现了简单邮件传输协议（SMTP），参见RFC 5321.
     textproto	    	textproto实现了对基于文本的请求/回复协议的一般性支持，包括HTTP、NNTP和SMTP.
     url	    	url包解析URL并实现了查询的逸码，参见RFC 3986.
os	    	os包提供了操作系统函数的不依赖平台的接口.
     exec	    	exec包执行外部命令.
     signal	    	signal包实现了对输入信号的访问.
     user	    	user包允许通过名称或ID查询用户帐户.
path	    	path实现了对斜杠分隔的路径的实用操作函数.
     filepath	    	filepath包实现了兼容各操作系统的文件路径的实用操作函数.
plugin	    	Package plugin implements loading and symbol resolution of Go plugins.
reflect	    	reflect包实现了运行时反射，允许程序操作任意类型的对象.
regexp	    	regexp包实现了正则表达式搜索.
     syntax	    	Package syntax parses regular expressions into parse trees and compiles parse trees into programs.
runtime	    	TODO(osc): 需更新 runtime 包含与Go的运行时系统进行交互的操作，例如用于控制Go程的函数.
     cgo	    	cgo 包含有 cgo 工具生成的代码的运行时支持.
     debug	    	debug 包含有程序在运行时调试其自身的功能.
     pprof	    	pprof 包按照可视化工具 pprof 所要求的格式写出运行时分析数据.
     race	    	race 包实现了数据竞争检测逻辑.
     trace	    	Go execution tracer.
sort	    	sort 包为切片及用户定义的集合的排序操作提供了原语.
strconv	    	strconv包实现了基本数据类型和其字符串表示的相互转换.
strings	    	strings包实现了用于操作字符的简单函数.
sync	    	sync 包提供了互斥锁这类的基本的同步原语.
     atomic	    	atomic 包提供了底层的原子性内存原语，这对于同步算法的实现很有用.
syscall	    	Package syscall contains an interface to the low-level operating system primitives.
testing	    	Package testing provides support for automated testing of Go packages.
     iotest	    	Package iotest implements Readers and Writers useful mainly for testing.
     quick	    	Package quick implements utility functions to help with black box testing.
text	    	
     scanner	    	scanner包提供对utf-8文本的token扫描服务.
     tabwriter	    	tabwriter包实现了写入过滤器（tabwriter.Writer），可以将输入的缩进修正为正确的对齐文本.
     template	    	template包实现了数据驱动的用于生成文本输出的模板.
          parse	    	Package parse builds parse trees for templates as defined by text/template and html/template.
time	    	time包提供了时间的显示和测量用的函数.
unicode	    	unicode 包提供了一些测试Unicode码点属性的数据和函数.
     utf16	    	utf16 包实现了对UTF-16序列的编码和解码。
     utf8	    	utf8 包实现了支持UTF-8文本编码的函数和常量.
unsafe


```



