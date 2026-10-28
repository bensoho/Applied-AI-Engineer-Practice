from applied_ai_engineer_practice.model import get_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = get_model()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个简洁的 AI 助手，回答不超过 80 字。"),
        ("human", "{question}"),
    ]
)

parser = StrOutputParser()
chain = prompt | model | parser

# 1. invoke: 单次调用
print("单次调用结果:")
result = chain.invoke({"question": "什么是LCEL?"})
print(result)

# 2. stream: 流式调用
print("流式调用结果:")
for chunk in chain.stream({"question": "用一句话介绍 LangGraph。"}):
    print(chunk, end="", flush=True)
print()

# 3. batch: 批量调用
print("批量调用结果:")
inputs = [
    {"question": "什么是 ChatModel？"},
    {"question": "什么是 PromptTemplate？"},
    {"question": "什么是 OutputParser？"},
]
results = chain.batch(inputs)
for result in results:
    print(result)
