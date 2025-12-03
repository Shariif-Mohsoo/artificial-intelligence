from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

# --- Step 2: Define model ---
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
)

# --- Step 3: Use Chat model ---
model = ChatHuggingFace(llm=llm)
#memory/chat_history
chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]
while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    res = model.invoke(user_input)
    chat_history.append(AIMessage(content = res.content))
    print("AI:",res.content)
print(chat_history)