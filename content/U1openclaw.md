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
