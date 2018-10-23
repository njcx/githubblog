Title: Python下Scrapy爬虫框架简单入门（A）
Date: 2017-03-23 10:20
Modified: 2017-03-23 10:20
Category: Python
Tags: Python
Slug: B12
Authors: nJcx
Summary: 介绍一下Python下的Scarpy的简单使用，记录一下学习过程
Status: draft

####本篇记录一下Scrapy的简单使用（一）
首先，我们先安装Python，因为Scrapy是运行在Python环境下的，然后通过pip install scrapy 安装scrapy框架，如果存在Python多版本情况，也可以通过 python -m pip install scrapy（python 2.x）和python3 -m pip install scrapy。然后通过scrapy startproject xxx 创建项目。目录结构如下
```bash
├── scrapy.cfg
└── spy
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py

2 directories, 7 files

```


