Title: XSS记录
Date: 2017-05-21 13:20
Modified: 2017-05-21 13:20
Category: 安全
Tags: XSS
Slug: G10
Authors: nJcx
Summary: 记录一下XSS的学习心路
Status: draft
#### 原因

xss出现的原因就是过于相信用户提交的数据，导致可以插入一些可执行脚本。

#### 分类

- 反射型
当我们把脚本作为参数，发给服务端的时候，服务端把脚本作为HTTP响应的一部分再次发送回来了，由浏览器解析脚本，产生攻击效应。

```php

<?php
$user = = $_GET['user'];
echo $user;
?>

```
当输入 

```javascipt

?user=<script>alert(1)</script>

```
js脚本被渲染到前端了，由浏览器弹窗了


- 存储型

存储型xss就是把脚本作为参数，未过滤插入了数据库中，当用户访问了相关的网页，后台再次把脚本渲染到前端，由浏览器执行了对应脚本，属于高危漏洞

- Dom型

Dom型的xss，不需要与server 连接，因为dom 发生在客户端,通过JavaScript改变前端内容,从客户端获取Dom中的数据并在本地运行，
