Title: django、flask 0day合集
Date: 2017-06-6 15:20
Modified: 2017-06-6 15:20
Category: 安全
Tags: django、flask 0day
Slug: L7
Authors: nJcx
Summary: django、flask 0day合集


- Django任意代码执行漏洞 
 	- django < 1.6
 	- http://blog.nsfocus.net/django-code-execution-vulnerability/

- Django的两个url跳转漏洞分析:CVE-2017-7233&7234
	- django 
	- https://mp.weixin.qq.com/s?__biz=MzI4MzI4MDg1NA==&mid=2247483817&idx=1&sn=5a1fd58b65edf4b88d2f455a486b97bd

- Django is_safe_url() URL跳转过滤函数Bypass（CVE-2017-7233）
	- 	django
	-  https://mp.weixin.qq.com/s?__biz=MzI4MzI4MDg1NA==&sn=5a1fd58b65edf4b88d2f455a486b97bd


- Django-UEditor 1.9.143 任意文件上传漏洞
	- Django-UEditor 1.9.143
	- https://github.com/zhangfisher/DjangoUeditor/issues/47
	
- django-epiceditor（CVE-2017-6591） XSS
	- django==1.10.6 django-epiceditor==0.2.3
	- http://morningchen.com/2017/03/09/Cross-site-scripting-vulnerability-in-django-epiceditor/

- Django CSRF Bypass (CVE-2016-7401)
	- Django 1.9.x < 1.9.10
	- Django 1.8.x < 1.8.15
	- https://www.seebug.org/vuldb/ssvid-92447

- django CMS 3.3.0 - (Editor Snippet) 存储型 XSS
 - https://www.exploit-db.com/exploits/40129/
	
- django logout 函数 dos拒绝服务攻击（CVE: 2015-5963）
	- Fix: Update/1.8.4/1.7.10/1.4.22/Add @login_required()
	- http://blog.knownsec.com/2015/08/django-logout-function-denial-of-service/

- django 的目录遍历漏洞(任意文件读取)
	- django
	- http://www.lijiejie.com/python-django-directory-traversal/

- flask  Werkzeug 调试模式 命令执行
	- https://www.seebug.org/vuldb/ssvid-89266
	
- flask 的jinjia2 服务端模板注入（SSTI）
	- https://blog.csdn.net/lansatiankongxxc/article/details/78764726
	- https://www.freebuf.com/articles/web/88768.html





