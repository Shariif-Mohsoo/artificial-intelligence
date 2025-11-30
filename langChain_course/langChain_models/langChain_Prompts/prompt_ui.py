# from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI() 

st.header("Research Tool")
# user_input = st.text_input("Enter your prompt")

paper_input = st.selectbox("Select Research Paper Name",[
    "A",
    "B","D","E","F"
])
style_input = st.selectbox("Select Explanation Style",[
    "A",
    "B","D","E","F"
])
length_input = st.selectbox("Select Explanation Length",[
    "Short",
    "Medium",
    "Long"
])

#template
template = load_prompt("template.json")



if st.button("Summarize"):
    chain = template | model
    res = chain.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
    })
    # prompt = template.invoke({
    # "paper_input":paper_input,
    # "style_input":style_input,
    # "length_input":length_input
    # })
    # res = model.invoke(prompt)
    # st.write("Some random text")
    st.write(res.content)


# streamlit run prompt_ui.py