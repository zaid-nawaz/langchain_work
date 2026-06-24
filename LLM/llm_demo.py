from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenRouter(
    model="openai/gpt-3.5-turbo-instruct",
    temperature=0.7,
)

response = llm.invoke("what is the capital of india")
print(response)

