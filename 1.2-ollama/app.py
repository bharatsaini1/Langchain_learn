import os
from dotenv import load_dotenv

from langchain_ollama.llms import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# Prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework

st.title("Langchain Demo With Google Model")

input_text = st.text_input("What question you have in mind!")

## Ollama Llama2 model

llm = OllamaLLM(model="llama3")
output_praser = StrOutputParser()

chain = prompt|llm|output_praser

if input_text:
    st.write(chain.invoke({"question":input_text}))
