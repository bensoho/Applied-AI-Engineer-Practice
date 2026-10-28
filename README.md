### Day 2：ChatModel 调用、消息类型与 LCEL 基础
| 序号 | 任务 | 完成标准 |
|---|---|---|
| 1 | 进入 Day 1 项目目录 | 终端位于 `langchain-day1` |
| 2 | 激活 uv 环境 | `uv run python --version` 正常输出 |
| 3 | 复习 Day 1 三个脚本 | `day1_chat.py`、`day1_messages.py`、`day1_lcel.py` 都能运行 |
| 4 | 封装统一模型函数 | 新建 `model.py`，避免每个文件重复写配置 |
| 5 | 练习三种消息 | 能区分 SystemMessage、HumanMessage、AIMessage |
| 6 | 练习 LCEL 三种调用 | 能运行 `invoke`、`stream`、`batch` |
| 7 | 观察返回对象 | 能打印 `type(response)` 和 `response.content` |
| 8 | 记录踩坑 | 至少记录 1 个报错或理解点 |

#### 三种调用方式对比
| 调用方式 | 适合场景 | 返回值 |
|---|---|---|
| `invoke` | 单次问答、调试 | 一个完整结果 |
| `stream` | 对话界面、打字机效果 | 逐块返回文本 |
| `batch` | 批量生成、离线处理 | 结果列表 |


#### 今天重点看的文档
| 文档 | 看什么 |
|---|---|
| LangChain ChatModel 教程 | invoke、stream、batch、消息类型 |
| LangChain Messages 文档 | SystemMessage、HumanMessage、AIMessage |
| LangChain LCEL 文档 | `|` 管道、Runnable 接口 |
| DeepSeek 模型与价格页 | 确认 `deepseek-flash`、`deepseek-v4-pro` 当前状态 |

#### 今日验收标准
- uv run python day2_messages.py 能运行
- uv run python day2_lcel.py 能运行
- 能解释 invoke、stream、batch 的区别
- 能解释 SystemMessage、HumanMessage、AIMessage 的作用
- 能打印出 response.content
- 至少记录 1 个踩坑点