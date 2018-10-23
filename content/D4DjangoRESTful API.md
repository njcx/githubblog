Title: 利用Django实现RESTful API
Date: 2017-04-09 10:20
Modified: 2017-04-09 10:20
Category: Django
Tags: Django
Slug: D4
Authors: nJcx
Summary: 利用Django实现RESTful API,实践记录如下
Status: draft

####介绍
首先,什么是RESTful? 阮一峰大大写了两篇博文介绍的比较详尽

[理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful)

[RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)

####django 之 RESTful

浏览器向http服务器发出请求,服务器返回一个html,然后浏览器渲染这个html,然后，大家就能看到网页了，而RESTful是返回json、xml、yaml、csv等序列化文件，作为resource的载体，供前端或者app解析。django实现RESTful，一般使用djangorestframework模块

```python 

pip install djangorestframework

```

然后在settings.py中添加 rest_framework

```python

INSTALLED_APPS = (
    ...
    'rest_framework',
)


```
到这，djangorestframework 就装上的了。


