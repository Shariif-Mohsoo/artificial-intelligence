from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="Claude-3-5-sonnet-202041022",temperature=1.2);

res = model.invoke("What is the capital of Pakistan?")

print(res.content);
