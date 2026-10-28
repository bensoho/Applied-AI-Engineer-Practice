import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_model(model: str = "deepseek-flash", temperature: float = 0.7):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("BASE_URL"),
        temperature=temperature,
    )