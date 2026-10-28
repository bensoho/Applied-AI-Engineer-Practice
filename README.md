### Day 1：认识 LangChain 生态，跑通第一个 LLM 调用
| 序号 | 任务 | 完成标准 |
|---|---|---|
| 1 | 确认 uv 可用 | 终端执行 `uv --version` 有输出 |
| 2 | 初始化 uv 项目 | 项目目录下生成 `pyproject.toml` |
| 3 | 添加依赖 | 执行 `uv add` 后依赖写入 `pyproject.toml` |
| 4 | 配置 API Key | 创建 `.env` 文件，`load_dotenv()` 能读取 |
| 5 | 跑通最小 ChatModel 调用 | 能打印模型返回内容 |
| 6 | 理解三种消息 | 知道 SystemMessage、HumanMessage、AIMessage 的区别 |
| 7 | 写一个最小问答脚本 | 输入问题，模型能回答 |
| 8 | 记录踩坑 | 记下报错、版本、Key 配置方式 |

#### 环境准备
```bash
mkdir langchain-day1
cd langchain-day1
uv init
uv add langchain langchain-openai python-dotenv
```