Title: Centos6.9 编译安装 Python2.7.13
Date: 2017-04-17 10:20
Modified: 2017-04-17 10:20
Category: Python
Tags: Python
Slug: D12
Authors: nJcx
Summary: Centos6.9 编译安装 Python2.7.13

centos6.9自带的Python版本是2.6.6,版本太老了，目前Python的2.x版本最新是Python2.7.13，最好的方法是下载Python2.7.13的源码自己编译。先搞定centos的编译环境搭建以及相关依赖的处理：

```bash

1: yum install gcc gcc-c++ gcc-g77 flex bison autoconf automake bzip2-devel zlib-devel ncurses-devel libjpeg-devel libpng-devel libtiff-devel freetype-devel pam-devel openssl-devel libxml2-devel gettext-devel pcre-devel

2：可以直接yum groupinstall "Development tools"

```

然后下载Python2.7.13的源码自己编译：


```bash

> wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz && tar zxvf Python-2.7.13.tgz && cd Python-2.7.13

> ./configure && make && make install

```

很多教程说，编译安装Python会导致yum不能用，但是我没有遇到，所以就不用处理那个问题了。下面我们把pip安装上去，

```bash

wget wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py

```
这样，就行了

