Title: Python Web项目搭建实战-Django篇
Date: 2017-04-15 10:20
Modified: 2017-04-15 10:20
Category: Django
Tags: Django
Slug: D10
Authors: nJcx
Summary: Python Web项目搭建过程记录
- 安装

环境：Ubuntu server 16.04 amd64

我用的是PyPy替代了CPython,在纯Python项目上还没有遇到幺蛾子，性能提升看得见。先把nginx和supervisor装上，这里用supervisor监控进程的状态以及开机启动下文用到的uwsgi

```bash
> sudo apt-get install nginx pypy pypy-lib pypy-dev supervisor
```
我们可以配置pip国内源，把下面内容写到 ～/.pip/pip.conf 文件中,这样就可以用豆瓣的pip源加速了

```bash
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```
下面我们为PyPy 安装pip和virtualenv、uwsgi
```python 
> sudo apt-get install libpcre3 libpcre3-dev -y
> wget https://bootstrap.pypa.io/get-pip.py && pypy get-pip.py && pypy -m pip install virtualenv uwsgi

```

```bash
MySQL 数据库安装(好像在本文用不到，先安装再说)
>apt-get install mysql-server libmysqlclient-dev -y
>pypy -m pip install mysql-python
```
我们先创建一个PyPy的虚拟环境,就叫env

```bash
> pypy -m virtualenv env
> source env/bin/activate
> pip install django tornado flask mysql-python

```
下面，我们就要要配置这些nginx、supervisor、uwsgi,我们通过supervisor来管理uwsgi，

先简单的建一个django的项目,叫blog，再创建一个blogapp

```bash
> django-admin startproject blog
> cd blog && django-admin startapp blogapp
```

通过django内置的wsgi服务器测试，是正常的

```bash
> pypy manage.py runserver 0.0.0.0:8080
```

下面我们把django和uwsgi桥接在一起,写一个桥接django_uwsgi.py 文件，放在blog目录里面

```python
import os
import sys
import django
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
django.setup()
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

```
下面我们再写一个uwsgi的配置文件（还没有优化),就叫django.xml，也放到blog文件夹里面
```xml
<uwsgi>
    <socket>127.0.0.1:8521</socket>
    <chdir>/root/.pip/blog</chdir>
    <pythonpath>/root/.pip/env/site-packages</pythonpath>
    <module>django_uwsgi</module>
    <daemonize>uwsgi.log</daemonize>
</uwsgi>
```
nginx 的配置文件，不过没有做静态文件处理，django的后台显示不正常
```bash

server {
    listen   80; ## listen for ipv4; this line is default and implied
    #listen   [::]:80 default ipv6only=on; ## listen for ipv6

    #server_name blog;

    access_log /var/log/nginx/blog-access.log ;
    error_log /var/log/nginx/blog-error.log ;

    location / {
            uwsgi_pass 127.0.0.1:8521;
            include uwsgi_params;
    }

}
```
然后，给我们自己开发的应用程序编写一个配置文件，让supervisor来管理它。每个进程的配置文件都可以单独分拆，放在/etc/supervisor/conf.d/目录下，以.conf作为扩展名,就叫django_app.conf
```bash

[program:app]
command=uwsgi -x django.xml
directory=/root/.pip/blog
user=root

```
其中，进程app定义在[program:app]中，command是命令，directory是进程的当前目录，user是进程运行的用户身份。

重启supervisor，让配置文件生效，然后运行命令supervisorctl启动进程：
```bash

supervisorctl start app
```
停止进程：
```bash

supervisorctl stop app

```

这样，系统重启的时候，uwsgi 也会自动启动，省的我们手动启动它了，我是用的root用户配置的，生产环境不推荐这样做，全文基本搭建完了，运行也是正常的，后期，再深入一点，优化一下性能。

