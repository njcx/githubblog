Title: Flask-RESTful 探秘
Date: 2017-04-16 10:20
Modified: 2017-04-16 10:20
Category: Flask
Tags: Flask
Slug: D11
Authors: nJcx
Summary: Flask-RESTful 探秘
Status: draft

####介绍
首先,什么是RESTful? 阮一峰大大写了两篇博文介绍的比较详尽

[理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful)

[RESTful API 设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)

url里面不要给出动词，动词都是通过HTTP动词搞定（截取阮一峰大大的博客）

- GET /zoos：列出所有动物园
- POST /zoos：新建一个动物园
- GET /zoos/ID：获取某个指定动物园的信息
- PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
- PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
- DELETE /zoos/ID：删除某个动物园
- GET /zoos/ID/animals：列出某个指定动物园的所有动物
- DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物

####Flask 之 RESTful

浏览器向http服务器发出请求,服务器返回一个html,然后浏览器渲染这个html,然后，大家就能看到网页了，而RESTful是返回json、xml、yaml、csv等序列化文件，作为resource的载体，供前端或者app解析。Flask实现RESTful，可以使用Flask-RESTful 插件，感觉这个插件比djangorestframework模块轻多了。


```python

from flask import Flask, jsonify
app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': u'Django book',
        'description': u'a book about django',
    }
]

@app.route('/api/v1.0/', methods=['GET'])
def get_book():
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run(debug=True)
    
```
这里我们直接把任务列表存储在内存中
我们通过
```bash
> curl -i http://127.0.0.1:5000/api/v1.0/

```
就可以看到

```bash
njcx@debian:~$ curl -i http://127.0.0.1:5000/api/v1.0/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 123
Server: Werkzeug/0.12.2 Python/2.7.9
Date: Sun, 11 Jun 2017 11:32:20 GMT

{
  "books": [
    {
      "description": "a book about django", 
      "id": 1, 
      "title": "Django book"
    }
  ]
}
```

