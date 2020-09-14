Title: Docker环境安全实践
Date: 2018-07-16 02:20
Modified: 2018-07-16 02:20
Category: 安全
Tags: Docker
Slug: R9 
Authors: nJcx
Summary: Docker环境安全实践~


#### 介绍

Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口,更重要的是容器性能开销极低。Docker 是一个用于开发，交付和运行应用程序的开放平台。Docker 能够将应用程序与基础架构分开，从而可以快速交付软件。借助 Docker，可以与管理应用程序相同的方式来管理基础架构。通过利用 Docker 的方法来快速交付，测试和部署代码，可以大大减少编写代码和在生产环境中运行代码之间的延迟。在 Linux 中，实现容器的边界，主要有两种技术 Cgroups 和 Namespace. Cgroups 用于对运行的容器进行资源的限制，Namespace 则会将容器隔离起来，实现边界。

