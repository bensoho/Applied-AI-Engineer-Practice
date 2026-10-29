from langchain_core.prompts import ChatPromptTemplate
from applied_ai_engineer_practice.model import get_model

model = get_model(temperature=0.7)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个 Python 老师，回答要简洁、准确。"),
        ("human", "请解释：{topic}"),
    ]
)

# from_messages 更适合区分 system、human、assistant 角色；from_template 更适合简单文本模板。
# prompt_1 = ChatPromptTemplate.from_template(
#     "请解释：{topic}"
# )

chain = prompt | model
result = chain.invoke({"topic": "什么是 Python 中的列表推导式？"})
print(result.content)

