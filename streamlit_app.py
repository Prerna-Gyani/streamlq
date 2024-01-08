import streamlit as st
import os
from constants import APIKEY
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ['OPENAI_API_KEY'] = "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"

# App Framework
st.title("🧠 Rudimentary Second Brain")
prompt = st.text_input('Plug in your prompt here.')

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.markdown("# Welcome!")


if prompt:
    loader = DirectoryLoader("Resources", glob='*')
    index = VectorstoreIndexCreator().from_loaders([loader])
    st.markdown("## Results: ")
    st.write(index.query(prompt))
    #st.write(index.query(prompt, llm=ChatOpenAI()))
