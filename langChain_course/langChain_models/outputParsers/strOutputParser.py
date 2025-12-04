from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it",task="text-generation")

model = ChatHuggingFace(llm = llm)

#1st prompt -> detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)

#2nd prompt -> summary
template2 = PromptTemplate(
    template="write a 5 line summary on following text. \n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
res = model.invoke(prompt1)

prompt2 = template2.invoke({'text':res.content})
print(model.invoke(prompt2)) 