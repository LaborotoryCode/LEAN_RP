import openai
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.evaluation import load_evaluator
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

openai_api_key = st.secrets['OPENAI_API_KEY']

llm = OpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo-instruct'
)

evaluator = load_evaluator("labeled_criteria", criteria="correctness", llm=llm)

# Kopi C Kosong
# Black coffee with evaporated milk and no sugar – think of it as a cafe au lait
# ref: https://thehoneycombers.com/singapore/order-kopi-singapore/



# test 1

def evaluate(question, student, teacher_data, marks, reason):
    correctness_test_1=f'''{student}'''

    reference=f'''{teacher_data}'''

    eval_result = evaluator.evaluate_strings(
        input=f"""{question}""",
        prediction=correctness_test_1,
        reference=reference,
    )

    test = eval_result["reasoning"]
    template = f"If the question is worth {marks} marks, based on your reasoning: {reason},how many marks would you award the solution?"
    prompt = PromptTemplate(template=template,input_variables=["marks","reason"])
    chain = LLMChain(llm=llm,prompt=prompt,verbose=False)



# print(f'Reasoning: {eval_result["reasoning"]}')
# print(chain.run(marks=3,reason=test))
