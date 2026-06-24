from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-large",
    dimensions=32,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

document = [
    "delhi is the capital of india",
    "kolkata is the capital of west bengal",
    "paris is the capital of france"
]

vector = embeddings.embed_documents(document)
print(str(vector))