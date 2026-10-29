import json
from langchain_core.prompts import ChatPromptTemplate
from applied_ai_engineer_practice.model import get_model
from langchain_core.output_parsers import JsonOutputParser


model = get_model(temperature=0.3)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个 JSON 助手。只输出合法 JSON，不要输出其他文字。"),
        ("human", "请介绍 {topic}，返回字段：name、definition、example。"),
    ]
)

parser = JsonOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic": "Python字典"})
print("名称：", result["name"])
print("定义：", result["definition"])
print("示例：", result["example"])
