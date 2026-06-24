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

vector = embeddings.embed_query("Delhi is the capital of India")
print(str(vector))