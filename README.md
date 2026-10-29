### Day 3：PromptTemplate、结构化输出与 OutputParser
| 序号 | 任务 | 完成标准 |
|---|---|---|
| 1 | 复习 Day 2 代码 | `day2_messages.py`、`day2_lcel.py` 能正常运行 |
| 2 | 练习 ChatPromptTemplate | 能用 `from_messages` 和 `from_template` 创建 Prompt |
| 3 | 练习变量替换 | 能用 `{topic}`、`{question}` 等变量传入 |
| 4 | 练习 Pydantic 结构化输出 | 模型能返回稳定字段，而不是自由文本 |
| 5 | 练习 JsonOutputParser | 能解析模型返回的 JSON |
| 6 | 练习 PydanticOutputParser | 能解析成 Pydantic 对象 |
| 7 | 对比 Parser 差异 | 知道 `StrOutputParser` 与 `JsonOutputParser` 的区别 |
| 8 | 记录踩坑 | 至少记录 1 个 JSON 解析或 Prompt 问题 |

#### 对比三种 Parser
| Parser | 返回类型 | 适合场景 |
|---|---|---|
| `StrOutputParser` | 字符串 | 普通问答 |
| `JsonOutputParser` | dict / list | 需要 JSON，但不强制字段 |
| `PydanticOutputParser` | Pydantic 对象 | 需要严格字段校验 |

#### 推荐优先级：
| 场景 | 推荐方式 |
|---|---|
| 普通对话 | `StrOutputParser` |
| 需要 JSON | `JsonOutputParser` |
| 需要固定字段 | `model.with_structured_output(Pydantic)` |

#### 今天重点看的文档
| 文档 | 看什么 |
|---|---|
| LangChain PromptTemplate | `from_messages`、`from_template`、变量替换 |
| LangChain Structured Output | `with_structured_output`、Pydantic |
| LangChain OutputParser | `StrOutputParser`、`JsonOutputParser`、`PydanticOutputParser` |
| DeepSeek 模型页 | 确认 `deepseek-flash` 是否支持结构化输出 |

#### 今日验收标准
- uv run python day3_prompt.py 能运行
- uv run python day3_structured.py 能运行
- uv run python day3_json_parser.py 能运行
- 能解释 ChatPromptTemplate 的变量替换
- 能解释 with_structured_output 的作用
- 能区分 StrOutputParser、JsonOutputParser、PydanticOutputParser
- 至少记录 1 个踩坑点

```
DeepSeek 的思考模式不支持强制 tool_choice，而 with_structured_output 会强制指定工具，
所以这里关闭思考模式
```