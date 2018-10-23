Title: Django的模板内置标签详解
Date: 2017-04-18 12:20
Modified: 2017-04-18 12:20
Category: Django
Tags: Django
Slug: F6
Authors: nJcx
Summary: Django的模板内置过滤器详解
Status: draft
####介绍

django模板过滤器看起来是这样的：{{ name|lower }}，这将在变量 {{ name }} 被过滤器 lower 过滤后再显示它的值，该过滤器将文本转换成小写。使用管道符号 (|)来应用过滤器，过滤器能够被“串联”，一个过滤器的输出将被应用到下一个，{{ text|escape|linebreaks }} 就像这样。一些过滤器带有参数。过滤器的参数看起来像是这样： {{ bio|truncatewords:30 }}，这将显示 bio 变量的前30个词。过滤器参数包含空格的话，必须被引号包起来，例如，使用逗号和空格去连接一个列表中的元素，需要使用 {{ list|join:", " }}。Django提供了大约六十个内置的模版过滤器。

####开始