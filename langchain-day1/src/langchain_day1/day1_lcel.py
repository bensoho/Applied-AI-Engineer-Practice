import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="deepseek-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个 Python 学习助手。"),
        ("human", "{question}"),
    ]
)

chain = prompt | model

result = chain.invoke({"question": "Python 的 f-string 怎么用？"})
print(result.content)