Title: Python的列表,元组,字典方法总结
Date: 2017-03-24 10:20
Modified: 2017-03-24 10:20
Category: Python
Tags: Python
Slug: C1
Authors: nJcx
Summary: Python的列表,元组,字典方法总结
####Python的列表,元组,字典方法总结
首先，Python的列表，元组，字典都是对象

- 1,创建一个ww = [1,2]列表

```python
ww.append   ww.extend   ww.insert   ww.remove   ww.sort     
ww.count    ww.index    ww.pop      ww.reverse  

```
- 2,创立一个we=()元组

```python
we.count  we.index  
```
- 3,创立一个字典 asd = {1:1,'b':2}
```python

asd.clear       asd.items       asd.pop         asd.viewitems
asd.copy        asd.iteritems   asd.popitem     asd.viewkeys
asd.fromkeys    asd.iterkeys    asd.setdefault  asd.viewvalues
asd.get         asd.itervalues  asd.update      
asd.has_key     asd.keys        asd.values    

```
- 4，创立一个集合 wr=set([1,2,3])

```python
wr.add                          wr.issubset
wr.clear                        wr.issuperset
wr.copy                         wr.pop
wr.difference                   wr.remove
wr.difference_update            wr.symmetric_difference
wr.discard                      wr.symmetric_difference_update
wr.intersection                 wr.union
wr.intersection_update          wr.update
wr.isdisjoint        

```
- 5,建立一个字符串 sts = 'asdadsff'

```python
sts.capitalize  sts.isalnum     sts.lstrip      sts.splitlines
sts.center      sts.isalpha     sts.partition   sts.startswith
sts.count       sts.isdigit     sts.replace     sts.strip
sts.decode      sts.islower     sts.rfind       sts.swapcase
sts.encode      sts.isspace     sts.rindex      sts.title
sts.endswith    sts.istitle     sts.rjust       sts.translate
sts.expandtabs  sts.isupper     sts.rpartition  sts.upper
sts.find        sts.join        sts.rsplit      sts.zfill
sts.format      sts.ljust       sts.rstrip      
sts.index       sts.lower       sts.split   

```





