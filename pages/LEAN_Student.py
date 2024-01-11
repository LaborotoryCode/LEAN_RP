from openai import OpenAI
import uuid
import streamlit as st
from io import StringIO
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.evaluation import load_evaluator
import sys

import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Student", page_icon="👨‍🎓")

# if not st.session_state.teacher_data:
#     teacher_data = None
# else:
#     teacher_data = st.session_state.teacher_data
# if not st.session_state.question:
#     question = None
# else:
#     question = st.session_state.question

try:
    teacher_data = st.session_state.teacher_data
except:
    teacher_data = ""
try:
    question = st.session_state.question
except:
    question = ""

openai_api_key = st.secrets["OPENAI_API_KEY"]

llm = OpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo-instruct'
)

evaluator = load_evaluator("labeled_criteria", criteria="correctness", llm=llm)


def main():
    st.markdown("# Student")
    
    feedback = ""

    uploaded_files = st.file_uploader("Input a student's file", accept_multiple_files=True, key=uuid.uuid4())

    try:
        st.write(teacher_data)
    except:
        st.write("NO")
    # st.write(question)
    try:
        st.write(question)
    except:
        st.write("NIG")
    
    ans = main()
    solution_txt = teacher_data
    question_prompt = question
    
    print(solution_txt)
    print(question_prompt)

    


if __name__ == "__main__":
    main()