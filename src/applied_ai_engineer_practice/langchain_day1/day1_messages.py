import os

from dotenv import load_dotenv
from langchain.messages import HumanMessage, HumanMessage
from langchain.messages import SystemMessage
from langchain_openai import ChatOpenAI


load_dotenv()

model = ChatOpenAI(
    model="deepseek-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

messages = [
    SystemMessage(content="你是一个简洁的 AI 助手，回答不超过 60 字。"),
    HumanMessage(content="LangChain 是什么?"), 
]
response = model.invoke(messages)
print(response.content)