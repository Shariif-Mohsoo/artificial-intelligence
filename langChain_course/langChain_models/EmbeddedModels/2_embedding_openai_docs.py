from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
documents = [
    "Islamabad is the capital of Pakistan",
    "Kolkata is the capital of West Bangal",
    "Paris is the capital of France"
]
result = embeddings.embed_documents(documents);
print(str(result))