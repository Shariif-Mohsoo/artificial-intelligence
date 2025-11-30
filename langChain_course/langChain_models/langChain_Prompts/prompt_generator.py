from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="You entered your paper input:{paper_input} with style:{style_input} and length:{length_input}",
    input=["paper_input","style_input","length_input"],
    validate_template=True
)

template.save("template.json")