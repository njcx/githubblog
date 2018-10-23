Title: Python 字符串方法详解
Date: 2017-04-25 10:40
Modified: 2017-04-25 10:40
Category: Python
Tags: Python
Slug: E4
Authors: nJcx
Summary: Python 字符串方法详解
####开始

```python
str.capitalize  str.isalnum     str.lstrip      str.splitlines
str.center      str.isalpha     str.partition   str.startswith
str.count       str.isdigit     str.replace     str.strip
str.decode      str.islower     str.rfind       str.swapcase
str.encode      str.isspace     str.rindex      str.title
str.endswith    str.istitle     str.rjust       str.translate
str.expandtabs  str.isupper     str.rpartition  str.upper
str.find        str.join        str.rsplit      str.zfill
str.format      str.ljust       str.rstrip      
str.index       str.lower       str.split       
```
以Python2.7.12为主，Python字符串有上述方法，一共38个方法。

####介绍

- capitalize   返回第一个字母大写开头的字符串
- isalpha  如果是字母，返回一个Ture；否则返回为 False
- isalnum  如果是字母或数字，返回一个Ture；否则返回为 False
- isdigit  如果是数字（0-9），返回一个Ture；否则返回为 False
- islower  如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
- isspace  如果 string 中只包含空格，则返回 True，否则返回 False.
- istitle  如果 string 是标题化的(见 title())则返回 True，否则返回 False
- isupper  如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
- center
- count
- decode 
- endswith  endswith(obj, beg=0, end=len(string)) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
- expandtabs
- find     find(str, beg=0, end=len(string)),方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
- format  
- index
- join
- ljust
- lower
- lstrip
- partition
- replace
- rfind 
- rindex
- rjust
- rpartition
- rsplit 
- rstrip
- split 
- splitlines
- startswith
- strip
- swapcase
- title
- translate
- upper
- zfill