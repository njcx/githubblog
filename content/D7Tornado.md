Title: Tornado 学习笔记
Date: 2017-04-12 10:20
Modified: 2017-04-12 10:20
Category: Tornado
Tags: Tornado
Slug: D7
Authors: nJcx
Summary: tornado 学习笔记
####开始
Tornado全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架。作为Web框架，是一个轻量级的Web框架，其拥有异步非阻塞IO的处理方式。作为Web服务器，Tornado有较为出色的抗负载能力。得利于其非阻塞的方式和对 epoll 的运用，Tornado 每秒可以处理数以千计的连接，这意味着对于实时Web服务来说，Tornado 是一个理想的 Web 框架。无论做为一个HTTP Server 还是一个Web框架，Tornado都足够优秀。
####安装
Tornado 是纯Python实现的，完美支持PyPy，在Jit 加持下性能更是如虎添翼，我个人在做Web开发的时候，就很喜欢用PyPy，性能差异可以直接感觉到，推荐大家试一试。 目前Tornado的版本是4.5.1，我们可以配置国内源，把下面内容写到 ～/.pip/pip.conf 文件中，我的系统是ubuntu16.04，其他linux发行版类似
```bash
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```
安装方式：


```python
Python
>apt-get install python-pip -y && python -m pip install tornado

```
```python 
PyPy
> apt-get install wget pypy pypy-lib pypy-dev -y && wget https://bootstrap.pypa.io/get-pip.py && pypy get-pip.py && pypy -m pip install tornado

```

```bash
MySQL 数据库安装
>apt-get install mysql-server libmysqlclient-dev -y
>pypy -m pip install mysql-python
或者
>python -m pip install mysql-python
```
####模块
Tornado包含以下模块，和Django、Flask 不同，Tornado没有用二级目录作为模块的名字(Django、Flask喜欢把类和方法集中到__init__.py里面)，而是直接用Py文件作为模块

- Web框架

tornado.web - RequestHandler和Application类

tornado.template - 模板

tornado.routing - 路由

tornado.escape - 转义和字符串模块

tornado.locale - 国际化支持

tornado.websocket - 提供WebSocket支持

- HTTP服务器和客户端

tornado.httpserver - 非阻塞HTTP服务器

tornado.httpclient - 异步HTTP客户端

tornado.httputil - 处理HTTP头文件和URL

tornado.http1connection - HTTP/1.x客户端/服务器实现

- 异步

tornado.ioloop - 主事件循环

tornado.iostream - 非阻塞socket的包装

tornado.netutil - 网络工具集

tornado.tcpclient- IOStream 连接池（tcpclient）

tornado.tcpserver- 基于 IOStream的TCP服务器

- 并发

tornado.gen - 简化异步的模块

tornado.concurrent - 使用线程和futures

tornado.locks - 同步原语

tornado.queues - 队列

tornado.process - 多进程工具集

- 与其他服务集成

tornado.auth - 使用OpenID和OAuth进行第三方登录

tornado.wsgi - 与其他Python框架和服务器交互

tornado.platform.asyncio- asyncio和 Tornado的交互接口

tornado.platform.caresresolver - C-Ares的异步DNS解析器

tornado.platform.twisted - Twisted 和 Tornado的交互接口

- 工具集

tornado.autoreload - 自动加载代码

tornado.log - 日志处理

tornado.options - 命令行解析

tornado.stack_context - 异步回调的异常处理

tornado.testing - 单元测试支持

tornado.util - 实用工具集

####实践
简单的抛砖引玉，通过get传递参数并显示出来，pypy untitled2.py --port=8082,http://127.0.0.1:8082/?greeting=njcx

```python

from tornado.web import RequestHandler,Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define,options,parse_command_line

define("port",default=8081,help="run on the given port",type=int)

class Index(RequestHandler):
    def get(self):
        welcome = self.get_argument('greeting', 'Hello')
        self.write(welcome + ', friendly user!')
if __name__=="__main__":
    parse_command_line()
    app = Application(handlers=[(r"/",Index)])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.instance().start()
    
```