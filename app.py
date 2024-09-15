# app.py
import streamlit as st
from models import load_qa_pipeline
from ui import set_page_config, sidebar_settings, main_ui
from utils.feedback import feedback_section
import time
import numpy as np
import yaml

# Set up the page configuration
set_page_config()

# Sidebar settings
model_choice, confidence_threshold, show_raw_outputs = sidebar_settings()

# Load the model pipeline
qa_pipeline = load_qa_pipeline(model_choice)

# Main UI
context, questions = main_ui()

# Load configuration from the YAML file
with open('config.yaml') as f:
    config = yaml.safe_load(f)

if st.button("Get Answers") and context and questions:
    question_list = questions.split('\n')

    st.subheader("Results:")
    for idx, question in enumerate(question_list):
        if question.strip():
            st.write(f"**Question {idx + 1}:** {question}")
            try:
                start_time = time.time()
                result = qa_pipeline(question=question.strip(), context=context)
                elapsed_time = time.time() - start_time

                answer = np.atleast_1d(result['answer'])[0]
                score = np.atleast_1d(result['score'])[0]

                if score >= confidence_threshold:
                    st.write(f"**Answer**: {answer}")
                    st.write(f"**Confidence Score**: {score:.4f}")
                else:
                    st.warning(f"The answer for this question does not meet the confidence threshold ({confidence_threshold:.2f}).")

                if show_raw_outputs:
                    st.write(f"**Raw Output**: {result}")
                
                st.write(f"Time Taken: {elapsed_time:.4f} seconds")
            except Exception as e:
                st.error(f"An error occurred for Question {idx + 1}: {str(e)}")
        else:
            st.warning(f"Question {idx + 1} is empty. Please provide a valid question.")
else:
    st.write("Please provide both a context and at least one question to get an answer.")

feedback_section()

st.write(f"Developed by **{config['developer']}**")


