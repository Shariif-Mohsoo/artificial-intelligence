# from langchain_huggingface import HuggingFaceEmbeddings #incase of local

# from dotenv import load_dotenv

# load_dotenv()

# embedding = HuggingFaceEmbeddings(model_name="google/embeddinggemma-300m")

# text = "Islamabad is the capital of Pakistan"

# res = embedding.embed_query(text)

# print(res)

#incase of api key
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

embeddings = HuggingFaceEndpointEmbeddings(
    model="google/embeddinggemma-300m",
    huggingfacehub_api_token=hf_token
)

text = "Pakistan is a beautiful country."
print(embeddings.embed_query(text))
