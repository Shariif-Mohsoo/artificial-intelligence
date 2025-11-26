# #older
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# res = model.invoke("What is the capital of Pakistan?")
# print(res.content) 

# # present
# from langchain.chat_models import ChatGoogle
# from dotenv import load_dotenv
# import os

# load_dotenv()  # Load environment variables from .env

# # Make sure you have GOOGLE_API_KEY in your .env file
# api_key = os.getenv("GOOGLE_API_KEY")

# # Initialize the Google chat model
# chat = ChatGoogle(api_key=api_key, model="gemini-1.5-pro")

# # Ask a question
# response = chat.predict("What is the capital of Pakistan?")

# # Print the answer
# print(response)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
#gemini-2.5-pro
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=api_key)
response = model.invoke("What is the capital of Pakistan?")
print(response.content)
