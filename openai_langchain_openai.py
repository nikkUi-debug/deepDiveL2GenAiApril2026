from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

response = llm.invoke("capital of US")

print(response)