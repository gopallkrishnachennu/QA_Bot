# utils/feedback.py
import streamlit as st

def feedback_section():
    """Sidebar feedback section for user input."""
    st.sidebar.title("Feedback")
    feedback = st.sidebar.text_area("Your Feedback:", height=100, placeholder="Leave your feedback here...")
    if st.sidebar.button("Submit Feedback"):
        if feedback:
            st.sidebar.write("Thank you for your feedback!")
        else:
            st.sidebar.write("Please enter some feedback before submitting.")
