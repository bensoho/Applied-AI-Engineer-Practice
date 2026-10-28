from applied_ai_engineer_practice.model import get_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage



model = get_model()

messages = [
    SystemMessage(content="你是一个 Python 学习助手，回答要简洁、准确。"),
    HumanMessage(content="LangChain 的 ChatModel 是什么？"), 
]
response = model.invoke(messages)
print("响应类型:", type(response))
print("内容:", response.content)


"""
响应类型: <class 'langchain_core.messages.ai.AIMessage'>
内容: # LangChain 的 ChatModel

**ChatModel 是 LangChain 对“对话式大模型”的抽象接口**，实现基类是 `BaseChatModel`。它把模型调用统一成：**输入一组消息 → 输出一条 AI 消息**。

## 核心特征

**输入**：`List[BaseMessage]`，常用消息类型：
- `SystemMessage`：系统提示、角色设定
- `HumanMessage`：用户输入
- `AIMessage`：模型回复（可带 `tool_calls`）
- `ToolMessage`：工具执行结果

**输出**：一个 `AIMessage`（含 `content`、`response_metadata`、`tool_calls` 等）

## 和 LLM 的区别

| | LLM（旧接口） | ChatModel |
|---|---|---|
| 输入 | 纯字符串 | 消息列表 |
| 输出 | 字符串 | AIMessage |
| 场景 | 补全类模型 | 对话、工具调用、多轮 |

现在主流模型（OpenAI、Anthropic、Gemini、通义等）都走 ChatModel 接口。

## 常用实现

`ChatOpenAI`、`ChatAnthropic`、`ChatGoogleGenerativeAI`、`ChatOllama`、`ChatTongyi` ……

## 统一方法

所有 ChatModel 共享同一套调用方式，便于替换供应商：

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage("你是简洁的助手"),
    HumanMessage("什么是 LangChain？"),
]

resp = model.invoke(messages)      # 同步
# resp 是 AIMessage，resp.content 是文本

model.stream(messages)             # 流式
model.batch([messages, messages])  # 批量
await model.ainvoke(messages)      # 异步
```

## 两个重要能力

```python
# 1. 绑定工具，让模型可以发起函数调用
model_with_tools = model.bind_tools([my_tool])

# 2. 结构化输出，直接得到 Pydantic 对象
structured = model.with_structured_output(MySchema)
```

## 一句话总结

ChatModel 是 LangChain 里“**消息进、消息出**”的对话模型统一接口，屏蔽了不同厂商 API 的差异，并内置流式、批量、工具调用、结构化输出等能力，是构建 Agent / RAG / Chain 的基础组件。
"""