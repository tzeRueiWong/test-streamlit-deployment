import os 
from apikey import apikey

import streamlit as st
from streamlit_option_menu import option_menu




os.environ['OPENAI_API_KEY'] = apikey 

st.title('sample youtube title')
prompt = st.text_input('Plug in your prompt')

with st.sidebar:
    selected  = option_menu(
        menu_title = "Main Menu",
        options = ["Home","Projects","Contact"]
    )


