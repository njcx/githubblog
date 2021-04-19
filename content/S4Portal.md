Title: 企业安全建设之访客网络准入Portal认证Web开发
Date: 2018-08-15 20:20
Modified: 2018-08-15 20:20
Category: 安全
Tags: 企业安全建设
Slug: S4
Authors: nJcx
Summary: 企业安全建设之网络准入Portal认证Web开发 ~
Status: draft


#### 介绍

Portal认证通常也称为Web认证，

Portal认证特点：

	不需要安装客户端，直接使用Web页面认证，使用方便，减少客户端的维护工作量。
	
	便于运营，可以在Portal页面上开展业务拓展，如广告推送、责任公告、企业宣传等。
	
	技术成熟，被广泛应用于运营商、连锁快餐、酒店、学校等网络。
应用场景：

	访客接入
	
	低成本混合接入：Portal + MAC旁路。



![ac](../images/WechatIMG123.jpeg)



	1）用户访问任意网站，经过AC判断该用户未完成认证，发送HTTP 302请求到用户端，要求重定向到Portal Server的URL；

	2）用户收到重定向报文，再次请求portal server的URL；

	3）Portal Server推送统一的URL认证页面；
	
	4）用户填入用户名、密码，提交页面，向Portal Server发起连接请求；
	
	5）Portal Server向AC发起认证请求，请求中携带用户名和密码（已经加密）；
	
	6）而后AC进行RADIUS认证，发送Access-Request请求；
	
	7）AC接收Radius响应Access-Accept（Access-Reject等）消息；
	
	8）AC向Portal Server发送认证结果；
	
	9) Portal Server回应确认收到认证结果的报文。
	
	10）Portal Server推送认证结果给用户。
