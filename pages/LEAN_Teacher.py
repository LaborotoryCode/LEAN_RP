from openai import OpenAI
import uuid
import streamlit as st
from io import StringIO
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.evaluation import load_evaluator
import warnings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
warnings.filterwarnings("ignore")

global title
global text

st.set_page_config(page_title="Teacher", page_icon="👨‍🏫")

# i love lean!!!!!!

openai_api_key = st.secrets["OPENAI_API_KEY"]

llm = OpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo-instruct'
)

evaluator = load_evaluator("labeled_criteria", criteria="correctness", llm=llm)




def main():

    title = "Teacher"
    text = """For the teacher:
             Please upload the model answer to the question in the form of a .py file
             """

    st.markdown("# Teacher")

    st.write("## Question")
    question_file = st.file_uploader("Input the question in the form of a text file")

    if question_file is not None:

        # To convert to a string based IO:
        stringio1 = StringIO(question_file.getvalue().decode("utf-8"))

        # To read file as string:
        question = stringio1.read()
        st.write(question)
    
    
    st.write("## Model Answer")
    answer_file = st.file_uploader("Input the model answer in the form of a .py file")

    if answer_file is not None:

        # To convert to a string based IO:
        stringio2 = StringIO(answer_file.getvalue().decode("utf-8"))

        # To read file as string:
        teacher_data = stringio2.read()
        st.write(teacher_data)

    with st.form("my_form"):
        st.write("Input the max marks for the question: ")
        max_marks = st.slider("Form slider")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", max_marks, "checkbox")
    
    

        # if 'teacher_data' not in st.session_state:
        #     st.session_state['teacher_data'] = teacher_data
        #eval_result = evaluator.evaluate_strings(input=question,prediction=,reference=string_data)

    st.title('Student:')

    student_files = st.file_uploader("Input the model answer in the form of a .py file", accept_multiple_files=True)


    for file in student_files:
        # To convert to a string based IO:
        stringio3 = StringIO(file.getvalue().decode("utf-8"))

        # To read file as string:
        student_data = stringio3.read()
        correctness_test_1=student_data
        reference=teacher_data
        
        eval_result = evaluator.evaluate_strings(
            input=question,
            prediction=correctness_test_1,
            reference=reference,
        )

        test = eval_result["reasoning"]
        template = "If the question is worth {marks} marks, based on your reasoning: {reason},how many marks would you award the solution?"
        prompt = PromptTemplate(template=template,input_variables=["marks","reason"])
        chain = LLMChain(llm=llm,prompt=prompt,verbose=False)


        st.write(f'Reasoning: {eval_result["reasoning"]}')
        st.write(chain.run(marks=3,reason=test))


    

if __name__ == "__main__":
    main()


        








