### Applied AI Engineer Learning Plan
#### 第1个月：LangChain 基础与 LCEL
| 天数 | 任务 | 重点 |
|---|---|---|
| Day 1 | 了解 LangChain 生态 | 分清 LangChain / LangGraph / LangSmith 的分工 |
| Day 2 | 搭建 Python 环境 | 装好 Python、虚拟环境、langchain、langchain-openai |
| Day 3 | 跑通 ChatModel 调用 | 用 `init_chat_model` 或 `ChatOpenAI` 完成最小调用 |
| Day 4 | 理解消息类型 | 练习 SystemMessage、HumanMessage、AIMessage、ToolMessage |
| Day 5 | 学习 PromptTemplate | 用 `ChatPromptTemplate` 做变量替换 |
| Day 6 | 结构化输出 | 用 Pydantic/TypedDict 让模型返回稳定 JSON |
| Day 7 | 学习 OutputParser | 对比 StrOutputParser、JsonOutputParser、PydanticOutputParser |
| Day 8 | 理解 LCEL | 掌握 `prompt | model | parser` 管道写法 |
| Day 9 | Runnable 接口 | 练习 invoke、stream、batch |
| Day 10 | RunnablePassthrough | 理解如何在链中传递额外字段 |
| Day 11 | 多模型切换 | 尝试 OpenAI、Ollama 或其他模型接入 |
| Day 12 | 错误重试 | 给模型调用增加超时、重试、fallback |
| Day 13 | 封装工具函数 | 用 `@tool` 封装 2-3 个本地函数 |
| Day 14 | 工具调用机制 | 理解 bind_tools、tool_calls、工具回填 |
| Day 15 | 小项目复盘 | 做一个“带工具调用的 LCEL 链” |

#### 第2个月：Agent、RAG 与记忆
| 天数 | 任务 | 重点 |
|---|---|---|
| Day 16 | 理解新版 Agent | 知道 `create_agent` 已基于 LangGraph |
| Day 17 | 跑通 create_agent | 用官方示例跑通第一个 Agent |
| Day 18 | 接入自定义工具 | 让 Agent 调用你写的搜索、计算、查询工具 |
| Day 19 | 多轮对话历史 | 把 messages 传入 Agent，观察工具调用过程 |
| Day 20 | LangGraph Checkpointer | 用 MemorySaver 实现会话持久化 |
| Day 21 | Agent 错误处理 | 处理工具失败、空结果、重复调用 |
| Day 22 | RAG 基础 | 学习文档加载、分块、Embedding、向量库 |
| Day 23 | 构建 Retriever | 实现“问题 → 检索 → 增强 Prompt → 回答” |
| Day 24 | RAG 调优 | 调整 chunk_size、top_k、检索策略 |
| Day 25 | 引用原文 | 让 RAG 回答时标注来源片段 |
| Day 26 | Agent + RAG | 把检索器封装成工具接入 Agent |
| Day 27 | 记忆机制对比 | 理解旧 Memory 已不推荐，改用 LangGraph Checkpointer |
| Day 28 | 阶段项目 | 做一个“知识库问答 Agent” |
| Day 29 | 阶段复盘 | 整理 Prompt、工具、RAG、记忆的调用链 |

#### 第3个月：LangGraph 状态编排
| 天数 | 任务 | 重点 |
|---|---|---|
| Day 30 | LangGraph 概览 | 理解 StateGraph、Node、Edge |
| Day 31 | 定义 State | 用 TypedDict/Pydantic 定义状态结构 |
| Day 32 | 编写 Node | 每个节点只做一件事，接收 State，返回更新 |
| Day 33 | 普通边 | 用 `add_edge` 串联固定流程 |
| Day 34 | 条件边 | 用 `add_conditional_edges` 做分支路由 |
| Day 35 | 循环控制 | 实现“不合格就重试”的循环，并设置最大步数 |
| Day 36 | 编译与运行 | 理解 `compile()`、invoke、stream |
| Day 37 | 消息追加 | 掌握 `add_messages` 和 Reducer |
| Day 38 | 持久化状态 | 用 checkpointer 保存线程状态 |
| Day 39 | 人工介入 | 尝试 Human-in-the-loop 暂停与恢复 |
| Day 40 | 路由模式 | 实现“意图识别 → 分支处理 → 汇总回答” |
| Day 41 | 并行模式 | 尝试多节点并行执行后汇总结果 |
| Day 42 | 评估器模式 | 实现“生成 → 评估 → 优化”循环 |
| Day 43 | 多 Agent 雏形 | 尝试编排器 + Worker 模式 |
| Day 44 | LangGraph 项目 | 做一个多步工作流 Agent |

#### 第4个月：LangSmith、工程化与最终项目
| 天数 | 任务 | 重点 |
|---|---|---|
| Day 45 | 开通 LangSmith | 注册账号、获取 API Key |
| Day 46 | 启用自动追踪 | 配置环境变量，让 LangChain/LangGraph 自动上报 |
| Day 47 | 查看 Trace | 分析每一步输入输出、耗时、Token |
| Day 48 | 调试失败链路 | 用 Trace 定位工具报错、检索失败、Prompt 问题 |
| Day 49 | 创建数据集 | 在 LangSmith 中准备固定测试问题集 |
| Day 50 | 编写评估器 | 尝试 LLM-as-Judge 或代码评估器 |
| Day 51 | 运行评估实验 | 对比不同 Prompt 或模型版本 |
| Day 52 | 监控成本 | 记录 Token 消耗、延迟、错误率 |
| Day 53 | 安全与权限 | 给工具加权限控制，防止越权调用 |
| Day 54 | Prompt 注入防护 | 设计输入校验和系统提示词边界 |
| Day 55 | 缓存与限流 | 为高频问题增加缓存，控制并发 |
| Day 56 | FastAPI 接口 | 把 Agent 暴露成 API |
| Day 57 | 流式输出 | 支持 SSE 或 stream 流式返回 |
| Day 58 | 最终项目选题 | 选一个可演示项目，例如知识库助手、研究助手、工单助手 |
| Day 59 | 画架构图 | 明确 State、Node、Edge、工具、RAG、LangSmith 的关系 |
| Day 60 | 完成主链路 | 跑通端到端流程 |
| Day 61 | 接入评测 | 用 LangSmith 跑一轮回归测试 |
| Day 62 | 优化失败案例 | 根据 Trace 修复最差回答 |
| Day 63 | 写 README | 记录环境、启动方式、架构图、演示视频 |
| Day 64 | 整理踩坑清单 | 记录版本、报错、Prompt、工具失败、RAG 不准 |
| Day 65 | 最终复盘 | 输出学习总结、项目亮点、下一步计划 |



