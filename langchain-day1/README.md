
### Day 1：认识 LangChain 生态，跑通第一个 DeepSeek 调用
| 序号 | 任务 | 完成标准 |
|---|---|---|
| 1 | 确认 uv 可用 | 终端执行 `uv --version` 有输出 |
| 2 | 初始化 uv 项目 | 项目目录下生成 `pyproject.toml` |
| 3 | 添加依赖 | 执行 `uv add` 后依赖写入 `pyproject.toml` |
| 4 | 申请 DeepSeek API Key | 在 DeepSeek 平台创建 Key 并保存 |
| 5 | 配置环境变量 | `.env` 中写入 `DEEPSEEK_API_KEY`，`load_dotenv()` 能读取 |
| 6 | 跑通最小 ChatModel 调用 | 能打印 DeepSeek 返回内容 |
| 7 | 理解三种消息 | 知道 SystemMessage、HumanMessage、AIMessage 的区别 |
| 8 | 写一个最小问答脚本 | 输入问题，模型能回答 |
| 9 | 记录踩坑 | 记下报错、模型名、Key 配置方式 |

```bash
mkdir langchain-day1
cd langchain-day1
uv init
uv add langchain langchain-openai python-dotenv
```

#### 今天重点看的文档
| 文档 | 看什么 |
|---|---|
| LangChain 快速开始 | 安装、ChatModel、最小调用 |
| LangChain 概念指南 | Prompt、LCEL、消息类型 |
| LangGraph 概览 | 知道它负责状态编排即可 |
| LangSmith 概览 | 知道它负责追踪和评测即可 |
| uv 文档 | 熟悉 `uv init`、`uv add`、`uv run` |
| DeepSeek 平台文档 | 申请 API Key、查看可用模型 |

