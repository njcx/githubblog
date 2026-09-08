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


#### 架构详解



如果把 OpenClaw 比作一个高度自动化的智能工厂，那么它的各个组件就是这条流水线上的核心工位。OpenClaw 采用了“控制平面与数据平面分离”的现代架构思想，但其独特之处在于，整个控制平面（Gateway）和数据平面（工具执行）被有机地整合在了一个常驻进程中，通过精妙的模块化设计实现了高内聚、低耦合。


######  网关（Gateway）—— 系统的控制平面

Gateway 是 OpenClaw 最核心的组件，没有之一。它是一个常驻后台的守护进程，监听在 `ws://127.0.0.1:18789`，承担着“系统单一控制平面（Single Control Plane）”的角色。

核心职责与能力：

- 双协议接入层：Gateway 同时暴露 WebSocket（JSON-RPC）和 HTTP（OpenAI 兼容 API）两种接口。WebSocket 用于 CLI/TUI/WebChat 等交互式客户端，提供低延迟的双向通信；HTTP API 则用于外部服务的标准化调用。
- 连接生命周期管理：管理所有客户端（CLI、App、WebChat）的 WebSocket 连接，处理心跳保活、断线重连和会话恢复。
- 配置热重载与校验：启动时读取根目录下的 `openclaw.json`（JSON5 格式），通过 Zod 模式（Schema）进行严格的类型校验。支持在运行时监听配置文件变更，实现热重载（Hot Reload），无需重启进程即可应用新配置。
- 渠道管家：负责初始化、启动和监控所有配置的消息渠道适配器（如 Telegram、WhatsApp）。
- 定时任务调度器：内置 Cron 调度引擎，用于执行周期性的“心跳（Heartbeat）”任务，允许 Agent 在没有用户主动输入的情况下，按计划主动发起思考和行动（如每日总结或定时监控）。

生命周期启动流程：

-  1. 加载配置：解析 `openclaw.json` 并进行 Zod 校验。
-  2. 初始化认证：检查 API Key 或本地信任机制。
-  3. 启动 HTTP/WS 服务：绑定端口，升级 WebSocket 协议。
-  4. 连接渠道：并发初始化所有启用的渠道适配器（如登录 Telegram、连接 Discord）。
-  5. 启动 Cron 调度器：注册定时任务。
-  6. 注册工具与技能：扫描 `tools/` 和 `skills/` 目录，构建可执行能力清单。
-  7. 启动记忆服务：初始化向量数据库（本地）和记忆检索器。

###### 通道适配器（Channel Adapters）—— 异构消息的“万能翻译官”

通道适配器是 OpenClaw 实现“40+ 渠道接入”的基石。每个适配器都是一个独立的协议转换模块。

标准化抽象：
所有适配器都继承自同一个基类（`BaseChannel`），必须实现两个核心方法：`onMessage`（接收）和 `sendMessage`（发送）。这使得 Gateway 可以无视底层协议差异，将所有传入消息统一转化为标准的 `InternalMessage` 对象（包含 `senderId`、`content`、`channelType`、`replyTo` 等字段）。

认证与连接的多样性：

- Bot Token 模式（Telegram、Discord）：直接使用平台颁发的机器人令牌建立长连接（Long-Polling 或 Webhook）。
- 扫码配对模式（WhatsApp、Signal）：利用 `baileys` 或 `signal-node` 等库，通过扫码或配对码建立端到端加密会话，模拟多设备登录。
- OAuth 模式（Slack、Google Chat）：遵循标准 OAuth 2.0 流程获取用户凭证。

关键机制——降级与容错：
当某个渠道连接因网络问题断开时，适配器会启动指数退避（Exponential Backoff）重连策略。如果长时间无法恢复，Gateway 会记录错误日志并尝试使用备用渠道（如 Telegram）向管理员发送告警。

###### 消息路由器（Router）—— 智能分发决策引擎

消息路由器是 Gateway 内部的核心决策组件之一。它不处理业务逻辑，只回答一个问题：“这条消息该交给谁？”

路由策略层级（优先级从高到低）：

1. 精确匹配路由：基于配置文件的规则（如 `routeBy: userId`），为特定用户或群组 ID 固定分配一个专属 Agent 实例。
2. 内容意图路由：通过简单的关键词匹配或调用本地小模型（Embedding）进行意图分类，将消息分流给擅长特定领域的 Agent（如“代码助手”或“文案助手”）。
3. 默认路由：如果以上规则均未命中，消息将被分配给默认的 `main` Agent。

这种设计使得 OpenClaw 在单一进程下，依然能模拟出“多 Agent 团队协作”的效果。

######  会话管理器（Session Manager）—— 上下文隔离与队列控制

会话（Session）是 OpenClaw 中最基本的隔离单元。每个对话独立维护一个 Session，包含了完整的 `messageHistory`（消息历史）、`systemPrompt`（系统提示词）和 `metadata`（元数据如时区、用户名）。

“车道式队列（Lane Queue）”机制：
这是 OpenClaw 处理并发请求的精妙设计。它遵循“显式并行，默认串行”的原则：

- 每个 Session 拥有一个独立的消息队列（Lane）。
- 同一个 Lane 中的消息严格串行（FIFO）处理。这确保了多轮对话的因果一致性，防止 LLM 因乱序而产生幻觉。
- 不同 Lane 之间的消息完全并行处理，充分利用 Node.js 的异步 I/O 能力，一个用户的长时间推理不会阻塞其他用户的消息接收。

######  大脑（Brain）—— LLM 推理与提示工程中枢

Brain 模块是 OpenClaw 的“智慧核心”，负责封装与所有大语言模型的交互细节。

核心能力：

- 多提供商抽象（Provider Abstraction）：通过统一的 `LLMClient` 接口，屏蔽了 OpenAI、Anthropic、Google、Azure 以及本地 Ollama 等不同 API 的差异。切换模型只需在配置文件中修改 `provider` 和 `modelName` 字段。
- 层级模型路由（Tiered Routing）：支持配置“主模型”和“备用模型”。当主模型因限流或超时失败时，Brain 自动降级到备用模型（如从 Claude-3.5-Sonnet 降级到 GPT-4o-mini），保证服务高可用。
- 动态 Prompt 组装：每次请求时，Brain 会动态构建 Prompt 上下文。其结构通常为：
    1. 系统层：基础人格设定、安全边界、当前时间/时区。
    2. 工具层：将当前可用的 `Skills` 和 `Tools` 序列化为符合模型 Function Calling 规范的 JSON Schema。
    3. 记忆层：调用 Memory 模块检索出的相关长期记忆片段。
    4. 会话层：最近的 N 轮对话历史。
    5. 用户层：当前用户的原始输入。

######  双手（Hands）—— 安全的工具执行沙箱

Hands 模块负责执行 Brain 发出的工具调用指令（如 `run_shell`、`write_file`、`browser_click`）。它不仅是执行引擎，更是安全的守门人。

执行隔离策略：

- 默认沙箱（Sandbox）：绝大多数工具调用被默认路由到 Docker 容器中执行。Gateway 会动态挂载必要的卷，并设置 CPU/内存限制，防止恶意或错误的 Shell 命令损坏宿主机。
- 本地直连（Local Fallback）：对于某些需要访问宿主机特定资源（如 USB 设备、本地音频）的任务，可配置白名单跳过沙箱，但会触发更严格的审批流程。

执行审批（Exec Approval）机制：
这是 OpenClaw 安全体系中最关键的一环。对于高风险操作（如 `rm -rf`、修改系统文件、发送邮件），Hands 不会立即执行，而是：

1. 挂起该工具调用。
2. 通过渠道（如 Telegram）向管理员发送一条带有“批准/拒绝”按钮的交互式消息。
3. 等待管理员审批通过后，才继续执行并将结果返回给 Brain。

######  记忆系统（Memory）—— 长期记忆与知识库

OpenClaw 的记忆系统超越了简单的对话历史缓存，它是一个轻量级的本地“长期记忆”服务。

存储与检索架构：

- 本地 Markdown 存储：记忆片段以人类可读的 Markdown 格式存储在 `memory/` 目录下，方便用户随时查看和手动编辑。
- 混合检索（Hybrid Search）：检索时，Memory 模块同时执行关键词（BM25）和向量（Embedding）搜索，并将两者的结果进行加权融合（RRF 算法），确保既能精确匹配术语，又能理解语义相关性。
- “梦想（Dreaming）”机制：这是一个独特的后台进程。在系统空闲时，Memory 模块会自动回顾近期的对话摘要，进行压缩和归纳，形成更高层级的“蓝图记忆”，模拟人脑在睡眠中整理记忆的过程。

######  技能系统（Skills）—— 声明式能力扩展

与传统的需要编写代码的插件系统不同，OpenClaw 的 Skills 是声明式（Declarative）的。

定义方式：
一个 Skill 由 `YAML` 配置和 `Markdown` 说明组成。例如：

```yaml
# weather.skill.md
---
name: "weather-query"
description: "查询指定城市的实时天气"
parameters:
  city:
    type: string
    required: true
    description: "城市英文名称"
---
执行步骤：
1. 调用 `curl https://api.weatherapi.com/v1/current.json?key=xxx&q={{city}}`
2. 提取温度与天气状况，格式化输出

```


######  执行审批管理器（Exec Approval Manager）—— 纵深防御体系

这是内嵌在 Gateway 中的一个安全微服务，与 Hands 紧密配合，负责执行策略决策点（PDP）。

安全防护矩阵：

- SSRF 防护：拦截工具向内部敏感 IP（如 127.0.0.1、169.254.169.254）发起的请求。
	
- 文件系统围栏：限制工具只能读写 workspace/ 目录下的文件，禁止访问 /etc/passwd 等系统敏感路径。
	
- 时序安全（Timing Attack）防护：在审批流程中引入随机延迟，防止攻击者通过响应时间推断系统状态。



#### 一条消息的生命周期

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




#### 安全部分的介入点