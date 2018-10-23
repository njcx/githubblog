Title:Python 的 *args和 **kwargs
Date: 2017-04-18 12:20
Modified: 2017-04-18 12:20
Category: Python
Tags: Python
Slug: F8
Authors: nJcx
Summary: Python 的 *args和 **kwargs
####介绍
首先，我们并不是一定要写成\*args 和 \*\*kwargs，关键是前面的\* 和 \*\*,换句话说，我们也可以\*var 和　\*\*var,这个只是大家约定熟成的方式,我们也可以换成其他的，既然，大家这样写，那么也推荐大家这样写。
####开始
\*args	和 \*\*kwargs主要用于函数定义。你可以将不定数量的参数传递给一个函数。这里的不定的意思是:预先并不知道,函数使用者会传递多少个参数给你,所以在这个场景下使用这两个关键字。\*args是用来发送一个非键值对的可变数量的参数列表给一个函数.这里有个例子帮你理解这个概念:

```python 

In [6]: def demo(args_f,*args_v):
        print args_f
        for x in args_v:
                print x
   ...:         

In [7]: demo('a','b','c','d')
a
b
c
d
```

\*\*kwargs允许你将不定长度的键值对,作为参数传递给一个函数。如果你想要在一个函数里处理带名字的参数,	你应该使用\*\*kwargs。这里有个例子帮你理解这个概念:
```python

In [1]: def demo(**args_v):
   ...:         for k,v in args_v.items():
   ...:                 print k,v
   ...: 

In [2]: demo(name='njcx')
name njcx

```
我们也可以把一个已经存在的list,tuple和dict构造成\*args 和 \*\*kwargs传进函数里面，这里有个例子：

```python 
In [17]: %paste

def demo(*args_f,**args_v):
    for x in args_f:
        print x        
    for k,v in args_v.items():
        print k+'='+v

list1 = [1,2,3]

dict = {'a':'A','b':'B','c':'C'}

demo(*list1,**dict)

## -- End pasted text --
1
2
3
a=A
c=C
b=B

In [18]: 
```
那么函数里同时使用所有三种参数,顺序怎么样的呢？我们可以这样写 def demo(fargs,\*args,\*\*kwargs):

前面我们明确指定了，\*args	和 \*\*kwargs做为函数的参数，如果，我们没有指定\*args	和 \*\*kwargs，我们定义的函数是这样的def demo(fargs,fargs1,fargs2):　我们怎么用\*args	和 \*\*kwargs把参数传到函数里面？

```python
In [18]: %paste
list1 = [1,2,3]

dict = {'arg2':'A','arg1':'B','arg3':'C'}

def demo(arg1,arg2,arg3):
       print "arg1:", arg1
       print "arg2:", arg2
       print "arg3:", arg3
  
demo(*list1)
demo(**dict)

## -- End pasted text --
arg1: 1
arg2: 2
arg3: 3
arg1: B
arg2: A
arg3: C

In [19]: 
```

注意：我们构造的字典是参数是一一对应的。