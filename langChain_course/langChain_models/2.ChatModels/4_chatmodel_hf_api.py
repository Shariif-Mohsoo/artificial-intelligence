from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

from huggingface_hub import login

import os

# Load environment variables from .env file
load_dotenv()

# --- Step 1: Authenticate Hugging Face ---
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not hf_token:
    raise ValueError("❌ Missing HUGGINGFACEHUB_API_TOKEN in your .env file")

login(token=hf_token)

# --- Step 2: Define model ---
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    huggingfacehub_api_token=hf_token  # optional but good practice
)

# --- Step 3: Use Chat model ---
model = ChatHuggingFace(llm=llm)
res = model.invoke("What is the capital of Pakistan?")
print(res.content)
