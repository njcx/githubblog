Title: LLM安全围栏之个人隐私信息PII检测
Date: 2026-03-29 20:20
Modified: 2026-03-29 20:20
Category: 安全
Tags: 企业安全建设
Slug: T9
Authors: nJcx
Summary: LLM安全围栏之个人隐私信息PII检测 ~


  随着全球AI战略的深入推进，大语言模型（LLM）在提升生产力的同时，也引入了新的安全风险。根据OWASP发布的LLM应用十大安全威胁，提示词注入（Prompt Injection）和敏感信息泄露位列榜首，已成为企业级AI应用面临的最严峻挑战。大模型（LLM）本质上是概率生成系统，天然存在以下风险，LLM安全网关的核心目标是拦截有害输入、保障系统合规可控：


| 问题类型 | 具体表现 |
|---|---|
| **有害内容生成** | 暴力、色情、歧视、自伤等内容 |
| **提示词注入（Prompt Injection）** | 恶意指令混入上下文劫持模型行为 |
| **数据外泄（企业场景）** | 用户将内部敏感数据发送给外部模型 |


  因为输入的提示词是自然语言，传统方案（关键词黑名单、正则表达式、决策树）在 LLM 时代面临结构性失效， 目前业界普遍使用NLP 模型去检测异常提示词，比如微调BERT模型，规则引擎没有消失，而是退化为最后一道硬性兜底（如法规关键词、证件号码正则），小模型承担高频、高速的语义分类，大模型偶尔介入高风险的复杂歧义场景。三者分工协作，才能在安全性、性能、成本之间取得平衡。


   目前提示词注入检测和 意图检测是使用BERT模型检测，这个已经在前文写过了，  个人身份信息检测用的Presidio + spaCy ， 这两者通常出现在 NLP 文本处理流水线中，代表两种不同的文本理解范式，在LLM安全网关、意图识别、NER（命名实体识别）等任务里经常被对比选型。BERT模型 基于 Transformer 双向编码器的深度语义理解模型，核心是上下文感知的稠密向量表示， 典型使用场景就是文本分类（有害/无害、情感、意图）。 spaCy 模型是基于规则 + 统计机器学习的工业级 NLP 流水线工具，核心是符号化、结构化的语言处理， 目的快速提取关键词、实体（人名、地名、机构名）。



Presidio 是微软开源的一套 PII（个人隐私信息）检测与匿名化框架，专为企业级数据隐私保护设计。Presidio 由两个核心模块组成：Analyzer（检测 PII）和 Anonymizer（对检测结果执行匿名化操作）。二者解耦，可以独立使用。

![AnalyzerEngine](../images/AnalyzerEngine.png)

一， Analyzer Engine — PII 识别核心
 
 - 1. NLP 引擎
 
Presidio 本身不做 NLP，而是通过适配层对接主流框架：
 
- spaCy（默认）：轻量、快，适合生产环境
- Stanza：斯坦福 NLP，精度更高
- Hugging Face Transformers：支持 BERT/RoBERTa 等预训练模型做 NER
 
NLP 引擎负责分词、词性标注、命名实体识别（NER），为下游识别器提供语言学特征。
 
  - 2. 三类识别器
 
| 识别器类型 | 原理 | 典型用途 |
|---|---|---|
| Pattern Recognizer | 正则 + Checksum 校验 | 手机号、信用卡、身份证、邮箱 |
| NER Recognizer | 基于 NLP 模型的命名实体 | 人名、组织、地址、日期 |
| ML/Custom Recognizer | 自定义规则或微调分类器 | 行业特定 PII（病历号、合同编号） |
 
每个识别器返回一个 `RecognizerResult`，包含：
 
- `entity_type`：PII 类型（如 `PHONE_NUMBER`、`EMAIL_ADDRESS`）
- `score`：置信度 0~1
- `start / end`：在原文中的字符偏移量
 
 3. 内置 PII 类型（50+）
 
常见的有：`PERSON`、`EMAIL_ADDRESS`、`PHONE_NUMBER`、`CREDIT_CARD`、`IBAN_CODE`、`IP_ADDRESS`、`LOCATION`、`DATE_TIME`、`NRP`（国籍/宗教/政治观点）等，并支持多国本地化（中、美、英、德、法等）。
 
 
 二、Anonymizer Engine — 脱敏操作
 
检测到 PII 后，Anonymizer 支持五种操作符：
 
| 操作符 | 说明 |
|---|---|
| Replace | 将 PII 替换为类型占位符，如 `<PHONE_NUMBER>` |
| Redact | 直接删除 |
| Hash | MD5 / SHA256 / SHA512 单向哈希 |
| Encrypt / Decrypt | AES 128 CBC 可逆加密（用于需要还原的场景） |
| Custom| 传入自定义函数，灵活处理 |
 

 






![guard](../images/e0fd9ad6c548543c4107e8b70c671d06.png)
