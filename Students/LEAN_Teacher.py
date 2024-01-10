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

st.set_page_config(page_title="Teacher", page_icon="👨‍🏫")

global teacher_data
global question

# i love lean!!!!!!

load_dotenv('/Users/Ayaan/LEAN/env.txt')
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo-instruct'
)

evaluator = load_evaluator("labeled_criteria", criteria="correctness", llm=llm)


def main():
    st.markdown("# Teacher")

    st.write("""For the teacher:
             Please upload the model answer to the question in the form of a .py file
             """)
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        teacher_data = stringio.read()
        st.write(teacher_data)
        #eval_result = evaluator.evaluate_strings(input=question,prediction=,reference=string_data)

    st.write("""
                Enter the problem that you gave your students to solve below:
             """)
    question = st.chat_input("Input the problem", key=uuid.uuid4())


#def placeholder(): #IGNORE THIS IF YOU SEE IT
    #assuming ayaan has the thing working and all the files are in strings
    #student_ans = query_students()
    #for ans in student_ans:
    #    eval_results = evaluator.evaluate_strings(input=question,prediction=ans,reference=string_data)
    #    

if __name__ == "__main__":
    main()


        








