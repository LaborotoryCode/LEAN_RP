import openai
import uuid
import streamlit as st
from io import StringIO
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.evaluation import load_evaluator
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Student", page_icon="👨‍🎓")

global string_data
global feedback

load_dotenv('../env.txt')
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo-instruct'
)

evaluator = load_evaluator("labeled_criteria", criteria="correctness", llm=llm)


def main():
    st.markdown("# Student")
    
    feedback = ""

    uploaded_files = st.file_uploader("Input a student's file", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        st.write("Filename:", uploaded_file.name)
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        teacher_data = stringio.read()
        st.write(teacher_data)
        st.write("\n")
        


if __name__ == "__main__":
    main()