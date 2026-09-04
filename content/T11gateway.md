Title: 大模型网关里面的智能路由拆解
Date: 2026-04-22 20:20
Modified: 2026-04-22 20:20
Category: 安全
Tags: 企业安全建设
Slug: T11
Authors: nJcx
Summary: 大模型网关里面的智能路由拆解 ~



#### 介绍


大模型网关的智能路由（Intelligent Routing）是近年来随着大模型应用爆发而兴起的一项关键技术。它的核心目标是：在多个可用的模型（或模型服务）之间，根据请求的特征、实时状态和业务目标，自动选择最合适的模型来处理请求。你在很多 IDE 里看到的 “Auto” 选项，就是智能路由的一种典型应用——它让用户无需手动选择模型，系统会自动判断当前任务（比如写代码、解释代码、聊天）适合用哪个模型，从而在效果、速度和成本之间取得平衡。


##### 一、智能路由要解决什么问题？

假设你有一个大模型网关，后面接入了多个模型：

Kimi-k3：能力强，但贵、慢

DeepSeek-v4-flash：便宜、快，但复杂任务可能不够好

Claude 4.5 Sonnet：代码能力强，价格中等

本地小模型（如 Qwen 3.5 9B）：几乎免费、极快，但只能处理简单任务

用户的请求是多样的：有的只是问“今天天气怎么样”，有的是“帮我重构这段 500 行的 Python 代码”。如果所有请求都发给最贵的模型，成本会爆炸；如果都发给小模型，复杂任务质量很差。

智能路由的目标就是动态决策：把每个请求送到“性价比”最高的模型上，同时满足用户对质量和延迟的期望。



##### 二、智能路由的常见策略

智能路由可以从简单到复杂，大致分为以下几类：

| 算法类型 | 原理 | 优势 | 局限 |
|---------|------|------|------|
| 基于规则 | 正则匹配、关键词、前缀树 | 毫秒级响应 | 只能处理固定格式 |
| 基于 Embedding | 将请求和模型描述转为向量，计算余弦相似度 | 能理解同义表达 | 长尾意图覆盖不足 |
| 基于 LLM | 用大模型分析输入，输出路由标签 | 灵活度高，能处理模糊输入 | 延迟高（秒级），有幻觉风险 |
| 基于 ML 分类器、BERT模型 | 训练轻量分类模型（逻辑回归、小参数LLM等） | 兼顾准确率与低延迟 | 依赖标注数据 |





##### 三、智能路由系统的典型架构

一个完整的智能路由系统通常包含以下组件：

```bash

用户请求 → [请求分析器] → [特征提取] → [路由策略] → [模型调用] → [响应]
                ↑                              ↓
                └────────── 反馈日志 ←──────────┘
                
```

请求分析器：解析请求内容，提取结构化信息（任务类型、语言、长度、敏感词等）

特征提取：将请求转换为路由策略可用的特征向量（如嵌入、关键词、元数据）

路由策略：核心决策模块，根据特征和当前系统状态选择模型

模型调用：实际向选定模型发送请求并获取响应

反馈日志：记录每次请求的决策、结果质量（如用户反馈、自动评估指标）、延迟、成本等

离线/在线学习：利用反馈数据更新路由策略（如重新训练分类器、更新MAB参数）


成熟的路由系统不只看"任务难不难"，还会综合考虑：

成本优化：根据实时 Token 单价选择最低成本模型，或在预算约束下平衡成本与质量

性能与可用性：基于实时延迟、吞吐量、错误率动态选路；支持主备切换、故障自动降级

难度感知：区分简单提示与复杂推理任务，仅对高难度任务调用前沿模型

复合策略：结合历史 Trace 数据与质量反馈，通过强化学习实现自适应调优




##### 基于 Embedding 的分类器实践


基于 Embedding 的分类器实践核心流程为：构建标注样本库 → 向量化存储 → 实时请求 Embedding → 余弦相似度计算 → 阈值判定 → 模型分发。 其本质是将路由问题转化为“语义最近邻搜索”问题，通过比较用户请求与预置样本的向量距离来自动选择模型。

```bash

用户请求 (model="auto")
    ↓
① Embedding 模型将请求文本 → 转为向量 (如 1536 维)
    ↓
② 与样本库中预标注的向量做余弦相似度计算
    ↓
③ 取 TopK 最相似样本，看它们属于哪个标签
    ↓
④ 最高相似度 ≥ 阈值 → 采纳样本标签；否则 → 退回走规则兜底
    ↓
⑤ 根据标签选择对应模型组，转发请求


```


第一步：构建样本库（离线阶段）
这是整个系统的“弹药库”。你需要为每个路由类别准备若干代表性样本。

```bash

# 样本库结构示意
sample_library = {
    "simple": [
        "你好",
        "今天天气怎么样",
        "帮我翻译这句话",
        "这段代码什么意思",
        "写一个 Hello World",
        # ... 每个类别 5~20 条即可
    ],
    "complex": [
        "帮我设计一个微服务架构方案",
        "分析这段代码的性能瓶颈并给出优化建议",
        "重构这个模块，要求支持插件化扩展",
        "帮我写一个完整的用户认证系统",
        # ...
    ],
    "code_generation": [
        "用 Python 实现一个 LRU 缓存",
        "写一个 React 组件，支持拖拽排序",
        # ...
    ]
}

```

关键参数：

每个类别 5~20 条样本即可冷启动，覆盖主要口语变体

样本要覆盖不同表达方式（正式/口语/简短/详细），而非堆砌相似句

样本质量 > 数量，一条坏样本可能污染整个类别的匹配


第二步：向量化存储（离线阶段）
用 Embedding 模型将所有样本转为向量，存入向量数据库（或直接用内存中的 NumPy 数组）。

```bash

import numpy as np
from openai import OpenAI

client = OpenAI()

class EmbeddingRouter:
    def __init__(self, embedding_model="text-embedding-3-small"):
        self.embedding_model = embedding_model
        self.samples = {}       # {label: [text, ...]}
        self.sample_vectors = {} # {label: np.array}
    
    def build_index(self, sample_library: dict):
        """离线构建向量索引"""
        for label, texts in sample_library.items():
            # 批量调用 Embedding API
            response = client.embeddings.create(
                model=self.embedding_model,
                input=texts
            )
            vectors = np.array([item.embedding for item in response.data])
            self.samples[label] = texts
            self.sample_vectors[label] = vectors
        
        print(f"索引构建完成: {len(self.samples)} 个类别, "
              f"共 {sum(len(v) for v in self.samples.values())} 条样本")

```



第三步：实时路由决策（在线阶段）

请求进来后，实时 Embedding → 计算相似度 → 决策。

```bash

def cosine_similarity(a, b):
    """计算两个向量的余弦相似度"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def route(self, user_query: str, threshold=0.72, top_k=5):
    """
    核心路由逻辑
    - threshold: 相似度阈值，超过才采纳样本匹配结果
    - top_k: 取最相似的 K 个样本参与投票
    """
    # 1. 将用户请求向量化
    response = client.embeddings.create(
        model=self.embedding_model,
        input=[user_query]
    )
    query_vector = np.array(response.data[0].embedding)
    
    # 2. 与所有样本计算相似度，找 TopK
    all_scores = []  # [(score, label), ...]
    
    for label, vectors in self.sample_vectors.items():
        for vec in vectors:
            score = cosine_similarity(query_vector, vec)
            all_scores.append((score, label))
    
    # 按相似度降序排列，取 TopK
    all_scores.sort(key=lambda x: x[0], reverse=True)
    top_k_scores = all_scores[:top_k]
    
    # 3. 阈值判定
    best_score, best_label = top_k_scores[0]
    
    if best_score >= threshold:
        # 命中样本库，采用多数投票
        label_votes = {}
        for score, label in top_k_scores:
            if score >= threshold:
                label_votes[label] = label_votes.get(label, 0) + 1
        
        final_label = max(label_votes, key=label_votes.get)
        return final_label, best_score, "sample_match"
    else:
        # 未命中，走规则兜底
        return self._fallback_rules(user_query), best_score, "rule_fallback"

```



第四步：规则兜底（当 Embedding 不确定时）

当所有样本相似度都低于阈值时，用轻量规则兜底，避免"强行匹配"导致误路由。


```bash

def _fallback_rules(self, query: str) -> str:
    """规则兜底：基于长度、关键词等浅层特征"""
    
    # 规则1: 超长输入大概率是复杂任务
    if len(query) > 500:
        return "complex"
    
    # 规则2: 包含特定关键词
    complex_keywords = ["架构", "重构", "优化", "性能", "设计模式", "微服务"]
    if any(kw in query for kw in complex_keywords):
        return "complex"
    
    # 规则3: 包含代码块
    if "```" in query or "def " in query or "function " in query:
        return "code_generation"
    
    # 默认走简单模型
    return "simple"


```

关键参数调优指南


| 参数 | 作用 | 调优建议 |
|------|------|----------|
| threshold（阈值） | 相似度超过此值才采纳样本匹配 | 通常 0.70~0.80；太高会导致大量走兜底，太低会误匹配 |
| top_k | 参与投票的最相似样本数 | 通常 3~5；太小容易单样本误判，太大引入噪声 |
| Embedding 模型选择 | 决定语义理解能力 | 轻量场景用 `text-embedding-3-small`（1536维）；中文场景可用 `Qwen3-Embedding-0.6B` 等 |
| 样本数量 | 每类样本的覆盖度 | 冷启动 5~10 条，生产环境建议 20~50 条，覆盖主要变体 |



生产环境要注意的坑

	Embedding 延迟：每次路由都要调一次 Embedding API，通常 50~200ms。如果对延迟敏感，可以用本地 ONNX 模型（如 OpenSquilla 的做法，用本地 ONNX embedder 完全在设备端完成分类）
	
	样本漂移：用户使用模式会随时间变化，需要定期回标并更新样本库
	
	缓存亲和：同一对话中频繁切换模型会导致 prompt 缓存失效，路由决策要考虑缓存切换成本
	
	阈值不是万能的：边界模糊的请求（如"代码审查"既涉及编码也涉及安全）容易在类别间摇摆，建议设置信度阈值，低于阈值的走默认安全模型

##### 基于BERT模型 的分类器实践  







##### 六、总结
智能路由的本质是在多个模型之间做权衡决策，它结合了传统软件工程中的负载均衡、成本优化和机器学习中的预测与在线学习。从简单的规则到复杂的强化学习，你可以根据实际需求选择合适的复杂度。对于学习而言，建议从规则和启发式评分入手，理解基本框架后，再尝试引入 ML 或 MAB 来提升自适应性。IDE 中的 “Auto” 选项正是智能路由的一个轻量级应用，它的背后通常也是基于任务类型和成本/延迟的简单判断，但深入下去就是一套完整的系统工程。


