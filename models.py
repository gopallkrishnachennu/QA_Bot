# models.py
from transformers import pipeline
import yaml
import streamlit as st

# Load configuration from the YAML file
with open('config.yaml') as f:
    config = yaml.safe_load(f)

model_options = config['models']

@st.cache_resource
def load_qa_pipeline(selected_model):
    """Load the QA pipeline based on the user's choice."""
    return pipeline('question-answering', model=model_options[selected_model])
