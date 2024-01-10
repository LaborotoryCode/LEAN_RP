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

load_dotenv('/Users/Ayaan/LEAN/env.txt')
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo-instruct'
)

evaluator = load_evaluator("labeled_criteria", criteria="correctness", llm=llm)


def main():
    st.markdown("# Student")
    st.sidebar.header("Student")
    number_of_students = st.chat_input("Number of Students", key=uuid.uuid4())
    if number_of_students is not None:
        number_of_students = int(number_of_students)
        ans = []
        for _ in range(number_of_students):
            input_file = st.file_uploader("Upload Student's Answer", key=uuid.uuid4())
            if input_file is not None:
                # To read file as bytes:
                bytes_data = input_file.getvalue()

                # To convert to a string based IO:
                stringio = StringIO(input_file.getvalue().decode("utf-8"))

                # To read file as string:
                string_data = stringio.read()
                st.write(string_data)
            print(string_data)
            ans.append(string_data)
        return ans

if __name__ == "__main__":
    main()