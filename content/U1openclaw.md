Title: OpenClaw内部的安全策略拆解
Date: 2026-04-29 20:20
Modified: 2026-04-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: U01
Authors: nJcx
Summary: OpenClaw内部的安全策略拆解 ~


#### 介绍


OpenClaw 是一个开源、自托管的 AI Agent 平台，支持 40+ 通信渠道（包括 WhatsApp、Telegram、Discord、Slack、Signal、iMessage、LINE、飞书等）。其核心设计理念可以概括为一句话：所有消息渠道、AI 会话、工具调用都通过一个统一的本地 WebSocket 服务（Gateway）进行调度。

从代码规模来看，OpenClaw 是一个相当庞大的工程：拥有 2600+ TypeScript 文件、50+ 功能模块，估计代码行数超过 200,000 行。尽管如此庞大的规模，OpenClaw 并没有采用复杂的微服务架构，而是采用了 “插件化单体” 的架构风格——所有核心能力通过 pnpm-workspace.yaml 组织，在单一代码库中完成模块化。

在架构范式上，OpenClaw 采用以单个网关为中心的星型（hub-and-spoke）架构。Gateway 是一个常驻后台的 Node.js 进程，作为整个系统的单一控制平面（Single Control Plane），负责协调 LLM（“大脑”）、本地执行能力（“双手”）、持久化记忆以及外部消息渠道之间的通信。

![openclaw](../images/20260908_4e1654.png)



#### 架构

一条消息的完整旅程如下：

	消息入口 (Ingress)：用户通过任一渠道发送消息，该渠道的适配器将其标准化后传给网关。
	
	路由与分发 (Routing)：网关的路由器根据消息元数据，决定由哪个智能体处理。
	
	上下文组装 (Context Assembly)：编排器为此次请求组装上下文，包括系统指令、会话历史、相关记忆和可用工具列表等。
	
	LLM 推理 (Brain Inference)：将组装好的上下文发送给 “大脑” (LLM) 进行推理。LLM 可能直接生成回复，也可能要求调用工具。
	
	工具执行 (Hands Execution)：如需调用工具，“双手” 会执行相应操作：
	
	执行环境默认为 Docker 沙箱。
	
	高风险操作可能需要用户审批。
	
	结果返回与迭代 (Result Loop)：工具执行结果返回给编排器，再次送入 “大脑” 进行下一轮思考。此过程会循环，直到任务完成。
	
	消息出口 (Egress)：最终生成的回复由编排器通过路由器，经由原渠道返回给用户。



![openclaw](../images/20260908_683881.png)

```bash

git clone https://github.com/openclaw/openclaw.git


```


