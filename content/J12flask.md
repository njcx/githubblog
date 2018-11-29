Title: Flask 学习记录
Date: 2017-04-16 11:20
Modified: 2017-04-16 11:20
Category: Flask
Tags: Flask
Slug: J12
Authors: nJcx
Summary: Flask 学习记录
Status: draft

#### 介绍
Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用Werkzeug ，模板引擎则使用 Jinja2 。Flask使用 BSD 授权。Flask也被称为“microframework” ，因为它使用简单的核心，用 extension 增加其他功能。Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术。最新版本为1.0.2

#### 安装

把下面字样保存成requirements.txt

```bash
Flask==1.0.2
Flask-Login==0.4.1
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
Flask-Migrate==2.3.0
Flask-Mail==0.9.1
```
这样就可以在虚拟环境里面安装了

```bash
# pip install virtualenv
# python -m virtualenv flaskenv
# source  flaskenv/bin/activate
# pip install -r requirements.txt
```

#### 使用

老规矩，Hello World!

```python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
```

#### 搭建上线



