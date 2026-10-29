from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from applied_ai_engineer_practice.model import get_model

# DeepSeek 的思考模式不支持强制 tool_choice，而 with_structured_output 会强制指定工具，
# 所以这里关闭思考模式
model = get_model(temperature=0.3, extra_body={"thinking": {"type": "disabled"}})

class PythonConcept(BaseModel):
    name: str = Field(description="概念名称")
    definition: str = Field(description="简短定义")
    example: str = Field(description="一个示例代码")
    difficulty: str = Field(description="难度：入门/进阶/高级")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个 Python 老师，请严格按照 JSON 格式输出，不要输出多余解释。"),
        ("human", "介绍这个 Python 概念：{topic}"),
    ]
)

chain = prompt | model.with_structured_output(
    PythonConcept,
    method="function_calling",
)
result = chain.invoke({"topic": "Python字典"})
print("名称：", result.name)
print("定义：", result.definition)
print("示例：", result.example)
print("难度：", result.difficulty)