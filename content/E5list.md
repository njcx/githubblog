Title: Python list方法详解
Date: 2017-04-26 12:50
Modified: 2017-04-26 12:50
Category: Python
Tags: Python
Slug: E5
Authors: nJcx
Summary: Python list方法详解

####开始

```python
list.append   list.extend   list.insert   list.remove   list.sort     
list.count    list.index    list.pop      list.reverse  
```

####介绍

- list.append(obj) 在列表末尾添加新的对象

- list.count(obj) 统计某个元素在列表中出现的次数

- list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

- list.index(obj) 从列表中找出某个值第一个匹配项的索引位置

- list.insert(index, obj) 将对象插入列表

- list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

- list.remove(obj) 移除列表中某个值的第一个匹配项

- list.reverse()反向列表中元素

- list.sort([func]) 对原列表进行排序