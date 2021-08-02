Title: 个人简历-刘少华-安全开发
Date: 2018-02-15 10:20
Modified: 2018-02-15 10:20
Category: sec
Tags: sec
Slug: sec_resume1
Authors: nJcx
Summary:简历
Status: draft


---
# 联系方式

- 手机：18855999143 
- Email：njcx86@gmail.com 
- 微信号: cxwin512
- 微信公众号： 西部老枪

---

# 个人信息

 - 刘少华/男/1994 
 - 本科/黄山学院计算机系 
 - 工作年限：4年
 - [技术博客](https://www.njcx.bid )：https://www.njcx.bid 
 - [Github](http://github.com/njcx)：http://github.com/njcx 
 - [FreeBUF专栏](https://www.freebuf.com/column/1481)： https://www.freebuf.com/column/1481
 - [安全客](https://www.anquanke.com/member/154147)：https://www.anquanke.com/member/154147
 - Freebuf核心作者/安全客认证作者
 - 职位：高级安全开发工程师


---

## 自我简介
熟悉甲方的安全建设流程，熟悉大型互联网架构，日常工作主要负责安全工具维护、安全工具开发、应急响应等，有WAF、NIDS、HIDS、SOC开发经验，日常关注安全事件、威胁情报，业余偶尔挖挖SRC，对网络安全充满热爱，熟悉项目开发流程和团队协同工作，有很好的团队合作意识，对新技术比较感兴趣，兴趣面和技术面比较广泛，希望能在日后通过继续学习更进一步

---

## 技术能力
- 熟悉主流WEB安全技术，如SQL注入、XSS、CSRF、文件包含、命令执行、文件上传等，以及简单的漏洞修补建议
- 熟悉常用安全渗透测试工具的使用，比如Burp Suite、AWVS、SQLMAP、Nmap、MSF、CS等
- 熟悉常用安全开发组件的使用，比如Kafak、ELK、Zeek(bro)、Suricata等
- 熟悉常见的Linux发行版本，了解shell编程,熟悉常见服务搭建与故障排除，能以Linux为开发环境正常工作
- 熟悉Linux分布式生产环境部署，熟悉Web分布式生产环境，熟悉大型的互联网公司架构
- 熟悉TCP/IP、HTTP协议
- 熟悉Linux环境常用工具使用，比如Docker、k8S的使用等
- 可以用常用的编程语言编程，比如，Python、JAVA、Golang、Bash、Lua、JavaScript


---

## 工作经历

#### 上海微盟（6000人）（ 2019年3月 ~ 至今 ）


###### 自研WAF一期
- 简介：主要是利用Openresty技术栈开发而成，编程语言Lua，APi使用Python Flask开发而成，使用Redis+MySQL存放规则，项目超过2万行代码，90多个接口，涉及传统的规则引擎，对GET、POST、Header里面的字段、URL检测，文件上传后缀检测，IP黑白名单，URL域名泛域名拦截，CC流控等
- 主要工作
	+ 担任主要开发、管理、运维工作，Lua和Python API 均为本人一人所开发，WAF作为微盟的业务网关，几乎所有HTTP请求都过WAF，WAF作为一个安全工具，也是一个运维工具，后面写成文章做了分享，见下文

	
###### 自研WAF二期（偏风控）
- 简介： WAF虽然可以解决部分传统安全，但对，业务安全这一块心有余力不足，由WAF dump出来全量的流量打入kafka，进行反欺诈风控分析，分析用户行为，联动威胁情报得出决策，并调用WAF进行拦截封禁，用到了 Flink做流式处理，ClickHouce 做周期统计，ES做持久化

- 主要工作
	+ 担任部分开发、管理、运维工作，提供了威胁情报支持（刚开始自研收集的威胁情报，后购入腾讯的商业威胁情报），以及IP定位标签支持，以及部分风控策略的编写，WAF侧的支持


###### HIDS自研项目
- 简介： HIDS分成了3个环境，Linux、Windows、K8S环境，Linux环境是使用 Cgroups + etcd + kafka + netlink-connector 开发而成的Linux HIDS的架构，agent 部分使用go 开发而成， 会把采集的数据写入到kafka里面，由后端的规则引擎（Go开发而成，和NIDS共用）消费，配置部分以及agent存活使用etcd，Windows使用了Sysmon、K8S环境使用了Falco，后面写成文章做了分享，见下文

- 主要工作
	+  本项目由本人一人开发而成，我在此项目负责了规则引擎的开发、架构的设计、规则添加、自定义组件的开发，主要精力在Linux环境的HIDS开发，比如，反弹shell的检测、提权的检测、Webshell的检测（正则），系统信息的收集，恶意的网络连接（过威胁情报）等	

###### NIDS自研项目
- 简介：NIDS是自研的，主要镜像核心交换流量,采用PacketBeat、Zeek工具解析流量，通过kafka做传输管道，然后进行后续规则引擎分析(Go开发),分析的维度包括:主机的异常连接行为、异常流量等，使用ELK做持久化，告警通过发邮件通知

- 主要工作
	+ 本项目由本人一人开发而成，我在此项目负责了规则引擎的开发、架构的设计、规则添加、自定义组件的开发，比如挖矿检测、扫描器检测、漏洞利用请求等，项目使用了pf-ring 加速dpi，与威胁情报联动，目前运行状态良好
	


#### 上海点融网（4500人）（2017年7月 ~ 2019年3月）

###### 代码依赖异常审计项目
- 简介：目前很多代码项目没有对依赖的包进行检查，导致很多依赖的包存在cve和exp，存在巨大的风险，危及到上线的项目的安全，所以，安全部门建立该项目，进行项目包依赖检查，该项目把大量风险扼杀在摇篮之中
- 主要工作
	+ 担任主要开发、管理、运维工作，项目与自动集成工具联动，从kafka中获取项目发布信息，拉取repo，使用DependencyCheck 检测对应repo，然后把检测报告放到nginx下面，并把对应的url 通过email发送出来，供对应的人员参考查阅，并修复升级相关的依赖包，主要编程语言是Python，主要使用DependencyCheck模块，生成html格式的异常检测报告



###### 安全SOC平台的开发和维护
- 简介： SOC平台主要是采集WAF、NIDS、HIDS的告警记录，并进行一个告警跟踪，实现闭环
- 主要工作
	+ 该项目是Django开发而成，担任主要开发、管理、运维工作，主要还在于WAF、NIDS、HIDS、蜜罐，SOC主要作用是展示以及漏洞跟踪
	

###### 企业内部蜜罐的平台的建设
- 简介：由于我们的NIDS是通过镜像交换机流量建设而成，无法检测网段间的内部异常，一旦来内网段间内部攻击，就无法通过NIDS检测到，所以我们在各个生产环境的网段部署了蜜罐的agent，我们采用了开源的蜜罐做了简单二次开发，部署网段超过100个，蜜罐工作期间检测到大量的异常
- 主要工作
	+ 项目是基于开源的蜜罐做了简单二次开发而成，我在此项目负责了主要的开发工作，包括，前端和后端、以及一些组件，项目采用了Docker容器化部署，大量的agent节点分布在各个网段，在安全异常事件收集过程中，起到了较好的作用
	
###### NIDS的自研项目
- 简介：公司内部的NIDS是自主研发的，主要镜像核心交换流量,采用PacketBeat、Bro工具解析流量，通过kafka做传输管道，然后进行后续规则引擎分析,分析的维度包括:主机的异常连接行为、异常流量等

- 主要工作
	+ 我在此项目负责了规则添加、规则编写、自定义组件的开发，添加了比如防爬虫规则、挖矿检测、扫描器检测等，在目前力严重依赖前置WAF的前提下,需要有一定的入侵感知能力,给内部环境一定的安全感知能力,可以做到及时感知及时处理
	
###### HIDS 的自研项目
- 简介：公司内部的HIDS是自主研发的，主要通过加载LKM模块的方式进入Ring0层，通过修改寄存器CR0中保护控制位中的WP位来达到可修改Linux原本syscall地址的方式来Hook主要操作,主要支持安全基线、系统完整性检测、反弹shell、webshell检测等
- 主要工作
	+ 我在此项目负责了HIDS的规则添加，比如，日志删除检测、bash history删除检测、异常下载检测，以及安全基线规则添加等，HIDS和NIDS联动，可以提高异常的关联度，方便异常发生的溯源
	

###### 点融网Guest Wifi NAC网络接入认证平台开发和维护
- 简介：该平台主要用于访客网络接入认证，主要使用了Portal认证通常也称为Web认证，用到了Radius和MySQL，交换机为思科交换机
- 主要工作
	+ 项目是基于Flask开发而成，项目采用了Docker容器化部署，稳定性良好，使用者众多
	


###### 点融网安全应急响应中心平台SRC开发
- 简介：点融网安全应急响应中心平台是一个对外提供服务的项目，主要是收录白帽子提交的漏洞，以及提供漏洞审核、奖品发放的项目
- 主要工作
	+ 项目是基于Django开发而成，我在此项目负责了主要的开发工作，包括，前端和后端，项目采用了Docker容器化部署，项目在对外漏洞收集过程中起到重要的作用，服务白帽子超过1000人

###### 等级保护与ISO27001安全合规审计平台项目
简介：等级保护与iso27001安全合规审计平台是为安全部门提供一个直观显示并能轻松管理的公司安全合规审计平台,用于执行安全检查，风险评估等需求

- 主要工作
	+ 项目是基于Django开发而成，我在此项目负责了主要的开发工作，包括，前端和后端，前端采用了H+框架，项目采用了Docker容器化部署，该平台系统主要服务于安全合规审计人员使用


###### Github 代码泄露扫描项目

简介：Github 代码泄露扫描项目是一个爬虫项目，会按预定时间频率爬取Github，匹配相关的关键字，检测是否有公司的相关的代码以及敏感信息泄露

- 主要工作
	+ 我在此项目负责了主要的开发工作和维护工作，该项目包含两个子项目：代理获取模块和爬虫模块，主要开发语言是Python，该项目上线以后，查找到大量的源代码泄露和敏感信息泄露

---

## 开源项目

- [BlackIPS](https://github.com/njcx/BlackIPS)：https://github.com/njcx/BlackIPS

	开源威胁情报，包含3个组件，2个查询API，1个前端，400万+恶意IP，Go +Redis开发的威胁情报查询API性能良好。

- [RuleCat](https://github.com/njcx/RuleCat)：https://github.com/njcx/RuleCat

	GO开发而成，用于NIDS HIDS 分析的规则引擎，使用WorkerPool 高性能检测，使用yml作为规则，支持正则、子串、等于，支持多字段 "和" "或" 检测， 支持频率检测, 支持自定义函数检测,自定义函数可以满足几乎所有数据类型的检测

- [flink_sec](https://github.com/njcx/flink_sec)：https://github.com/njcx/flink_sec

	使用Flink Java 开发的规则引擎，使用json作为规则，支持正则、子串、等于，支持多字段 "和" "或" 检测
    

- [pyspark_nids](https://github.com/njcx/pyspark_nids)：https://github.com/njcx/pyspark_nids 

    使用PySpark 开发的规则引擎，使用Py字典作为规则，支持正则、子串、等于，支持多字段 "和" "或" 检测

- [iprestful](https://github.com/njcx/iprestful)：https://github.com/njcx/iprestful

	用于IP地址查询，使用Spring Boot 开发而成，性能良好，配合风控使用，有idc出口标记
	
- [py3finger](https://github.com/njcx/py3finger)：https://github.com/njcx/py3finger

	Py3Finger是一个HTTP指纹识别类库,用于HTTP资产识别、扫描器等

- [nginx_dump](https://github.com/njcx/nginx_dump)：https://github.com/njcx/nginx_dump

	Lua开发而成，该工具用于把Openresty(Nginx+Lua) 请求参数和响应 dump出来，用于旁路HTTP流量分析、风控、资产识别、API数据泄露分析等等
	
- [packetbeat](https://github.com/njcx/packetbeat)：https://github.com/njcx/packetbeat

 	魔改的Packetbeat，支持icmp data字段解码，用于检测icmp隧道，添加了ssh协议，支持ssh 部分字段解析，用于检测扫描
 	
- [Artemis_HIDS](https://github.com/njcx/Artemis_HIDS)：https://github.com/njcx/Artemis_HIDS

    使用 Cgroups + etcd + kafka + netlink-connector 开发而成的hids的架构，agent 部分使用go 开发而成， 会把采集的数据写入到kafka里面，由后端的规则引擎（go开发而成）消费，配置部分以及agent存活使用etcd。


- [pocsuite_poc_collect](https://github.com/njcx/pocsuite_poc_collect)：https://github.com/njcx/pocsuite_poc_collect
 
  自己写的一些Poc和收集的一些POC
  
- [peppa_gitscan](https://github.com/njcx/peppa_gitscan.git):  https://github.com/njcx/peppa_gitscan.git 
 
   Github 扫描器
- [gocmd](https://github.com/njcx/gocmd)：https://github.com/njcx/gocmd

	一个 HTTP隧道的 C&C ，可以用 CDN 隐藏， 免杀，流量加密，用于学习，研究使用

- [gomoon](https://github.com/njcx/gomoon)：https://github.com/njcx/gomoon

	一个WebShell管理工具，支持JSP、PHP，免杀，过WAF，过NIDS，用于学习，研究使用

- [Linux Basics for Hackers](https://github.com/OpenCyberTranslationProject/TP1):  https://github.com/OpenCyberTranslationProject/TP1 
 
 参与翻译的书，Linux Basics for Hackers，第5、6、7章节
 
---

## 技术文章
- [NIDS(suricata)中的ICMP隐蔽隧道检测](https://www.freebuf.com/articles/es/243486.html)
- [NIDS（suricata）中的DNS隐蔽隧道检测](https://www.freebuf.com/articles/network/244094.html)
- [甲方自研分布式WAF落地全程实录](https://www.freebuf.com/articles/es/245977.html)
- [C2的一些隐藏策略与防丢失](https://www.freebuf.com/articles/system/245567.html)
- [Etcd在HIDS-Agent配置管理和健康监测上的应用](https://www.freebuf.com/articles/system/266118.html)
- [Linux的Cgroups在HIDS-Agent资源限制上的应用](https://www.freebuf.com/articles/system/265733.html)
- [HIDS-Agent开发之抓取DNS请求和异常分析](https://www.anquanke.com/post/id/235715)
- [HIDS-Agent开发之检测反弹shell](https://www.anquanke.com/post/id/235717)
- [使用Sysmon和Winlogbeat打造Windows平台的HIDS](https://www.anquanke.com/post/id/236222)
- [Linux HIDS开发之eBPF的应用](https://www.anquanke.com/post/id/239870)
- [DDoS介绍与防御](https://www.anquanke.com/post/id/247595)
- [使用Falco做K8S环境的HIDS](https://www.njcx.bid/posts/S12.html)
- [K8S安全建设经验试分享](https://www.njcx.bid/posts/S9.html)

---

## 技能列表

以下均为我用过或正在使用的编程语言、工具或者库：

- 编程语言：C/Python/JAVA/Golang/Bash/Lua/JavaScript
- Web框架：Django/Flask/Gin/SpringBoot
- 数据库相关：MySQL/Redis/Mongodb/Etcd
- 常用组件： ELK/Kafka/OpenResty/Flink/Spark
- 常用工具： Burp Suite/AWVS/Nessus/Zeek(Bro)/Suricata/Wireshark

---

## 致谢
感谢您花时间阅读我的简历，期待能有机会和您共事。
