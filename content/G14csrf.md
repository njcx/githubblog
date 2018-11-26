Title: CSRF记录
Date: 2017-05-26 13:20
Modified: 2017-05-26 13:20
Category: 安全
Tags: CSRF
Slug: G14
Authors: nJcx
Summary: 记录一下学习CSRF的心路

#### 介绍

CSRF（Cross-Site Request Forgery）是指跨站请求伪造，通常缩写为CSRF。

#### 原理

![csrf](../images/csrf.jpg)


#### 检测


#### 预防

- 通过 referer、token（这里的token可以放到cookie，也可以放到参数里面）或者验证码二次确认来检测用户提交。
- 敏感操作最好都使用post操作 。
- 避免全站通用的cookie，严格设置cookie的域。