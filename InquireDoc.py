import streamlit as st
import os
from dotenv import load_dotenv  # type: ignore
import warnings
import google.generativeai as genai
import pandas as pd
from io import StringIO

# # You can access the value at any point with:
# st.session_state.name

st.header("_What can I :blue[help] with :red[?]_  :sunglasses:",anchor=None,help=None, divider=False)
# st.text_input("Your name", key="name")
uploaded_file = st.file_uploader("Choose a file")
print(uploaded_file)
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    #To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    # string_data = bytes_data.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)

# load_dotenv()
# genai.configure(api_key=os.environ["API_KEY"])
# model = genai.GenerativeModel('gemini-1.5-flash')
# # Upload the file and print a confirmation
# sample_file = genai.upload_file(path="gemini.pdf",display_name="Gemini 1.5 PDF")