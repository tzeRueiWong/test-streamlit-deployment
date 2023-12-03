import os 


import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



st.title('some random title')
prompt = st.text_input('Plug in your prompt')

