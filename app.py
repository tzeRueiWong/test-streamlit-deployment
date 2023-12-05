

import streamlit as st
from streamlit_option_menu import option_menu





st.title('some random title')
prompt = st.text_input('Plug in your prompt')

with st.sidebar:
    selected  = option_menu(
        menu_title = "Main Menu",
        options = ["Home","Projects","Contact"]
    )


