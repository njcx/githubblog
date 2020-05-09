Title: 使用Flink和Syslog、Flume做大规模主机日志审计
Date: 2018-07-28 20:20
Modified: 2018-07-28 20:20
Category: 安全
Tags: flink
Slug: O1
Authors: nJcx
Summary: 使用flink和syslog、flume做大规模主机日志审计~

#### 安装

使用Docker 快速搭建一个flink 集群环境

```bash

version: "2.1"
services:
  jobmanager:
    image: flink:1.10.0-scala_2.12
    expose:
      - "6123"
    ports:
      - "8081:8081"
    command: jobmanager
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager
  taskmanager:
    image: flink:1.10.0-scala_2.12
    expose:
      - "6121"
      - "6122"
    depends_on:
      - jobmanager
    command: taskmanager
    links:
      - "jobmanager:jobmanager"
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager

```

```go

```