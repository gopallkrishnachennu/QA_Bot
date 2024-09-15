# ui.py
import streamlit as st
import yaml

# Load configuration from the YAML file
with open('config.yaml') as f:
    config = yaml.safe_load(f)

def set_page_config():
    """Set the page configuration."""
    page_config = config['page']
    st.set_page_config(page_title=page_config['title'], layout=page_config['layout'])

def sidebar_settings():
    """Configure the sidebar settings."""
    st.sidebar.title("App Settings")
    model_choice = st.sidebar.selectbox("Select a Pre-trained Model", list(config['models'].keys()))
    confidence_threshold = st.sidebar.slider(
        'Confidence Score Threshold',
        config['sidebar']['confidence_threshold']['min'],
        config['sidebar']['confidence_threshold']['max'],
        config['sidebar']['confidence_threshold']['default'],
        config['sidebar']['confidence_threshold']['step']
    )
    show_raw_outputs = st.sidebar.checkbox("Show Raw Model Outputs", value=False)
    return model_choice, confidence_threshold, show_raw_outputs

def main_ui():
    """Main UI components for the app."""
    st.title("Question Answering Bot")
    context = st.text_area("Enter the Context:", height=200, placeholder="Paste or write the context here...")
    questions = st.text_area("Enter your Questions (separate with new lines):", height=100, placeholder="Ask one or more questions...")
    return context, questions
