Title: MongoDB学习笔记(A)
Date: 2017-04-03 10:20
Modified: 2017-04-03 10:20
Category: 数据库
Tags: MongoDB
Slug: C5
Authors: nJcx
Summary: 记录一下自己学到的东西

####介绍
Mongodb的3大元素:数据库(db),集合(collection),文档(document),"数据库"还是对应关系数据库中的"数据库",其中"集合"就是对应关系数据库中的"表"，"文档"对应"记录"。

| RDBMS	| MongoDB |
| --------   | -----:   | :----: |
| Database	| Database |
|Table	| Collection |
| Tuple/Row	| Document|
|column	| Field |
| Table Join	| Embedded Documents | 
| Primary Key	| Primary Key (Default key _id provided by mongodb itself)|

数据库服务器和客户端

| mysql | oracle | mongodb |
| --------   | -----:   | :----: |
| Mysqld | Oracle	| mongod |
| mysql | sqlplus	| mongo |

####安装

```bash

centos/rhce : yum install mongodb-server -y

debian/ubuntu : apt-get install mongodb-server -y

```
####使用
- 创建数据库

```bash

> use njcx
switched to db njcx
> db
njcx
> 

```
- 查看数据库

```bash
> show dbs

```

- 删除数据库

```bash
> use njcx
switched to db njcx
> db
njcx
> db.dropDatabase()

```
- 创建集合(插入自动创建)

```bash

> db.njcx.insert({"name":"njcx"})

```

- 创建集合(db.createCollection(name, options))

name 指定集合名称,opt 指定有关内存大小和索引选项(可选)

capped	         Boolean  （可选）如果为true，则启用封顶集合。封顶集合是固定大小的集合，会自动覆盖最早的条目，当它达到其最大大小。如果指定true，则需要也指定尺寸参数。

autoIndexID 	Boolean	（可选）如果为true，自动创建索引_id字段的默认值是false。

size	        number	（可选）指定最大大小字节封顶集合。如果封顶如果是 true，那么你还需要指定这个字段。

max  	        number	（可选）指定封顶集合允许在文件的最大数量。


```bash

> db.createCollection("tudou", { capped : true, autoIndexID : true, size : 6142800, max : 10000 } )

```

- 删除集合

```bash

> db.njcx.drop()

```







