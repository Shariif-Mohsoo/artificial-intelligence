from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=1.5
)

model = ChatHuggingFace(llm=llm)


messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]
res = model.invoke(messages)
messages.append(AIMessage(content=res.content))

print(messages)