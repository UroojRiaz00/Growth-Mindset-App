# import streamlit as st

# import streamlit as st

# st.set_page_config(page_title="My App", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# st.sidebar.empty()

# st.write("Hello world")



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import numpy as np


# Set page title and layout
st.set_page_config(page_title="Growth Mindset App", page_icon="🚀", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Viewer", "Sentiment Analysis"])

# Home Page
if page == "Home":
    st.title("Welcome to the Growth Mindset App! 🧠")
    st.write("This app helps you explore data and analyze text sentiment interactively using Streamlit.")
    
       # New Feature: Editable To-Do List
    st.subheader("📝 To-Do List")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    
    new_task = st.text_input("Add a new task:")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append(new_task)
    
    if st.session_state.tasks:
        st.write("### Your Tasks:")
        for i, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                updated_task = st.text_input(f"Edit Task {i+1}", task, key=f"task_{i}")
                if updated_task != task:
                    st.session_state.tasks[i] = updated_task
            with col2:
                if st.button("❌", key=f"delete_{i}"):
                    st.session_state.tasks.pop(i)
                    st.rerun()
                    # st.experimental_rerun()
# Data Viewer Page
elif page == "Data Viewer":
    st.title("📊 Data Viewer")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

# Sentiment Analysis Page
elif page == "Sentiment Analysis":
    st.title("💬 Sentiment Analysis")
    user_input = st.text_area("Enter text for sentiment analysis")
    
    if st.button("Analyze Sentiment"):
        if user_input:
            analysis = TextBlob(user_input)
            sentiment = analysis.sentiment.polarity
            
            if sentiment > 0:
                st.success("Positive 😊")
            elif sentiment < 0:
                st.error("Negative 😞")
            else:
                st.warning("Neutral 😐")
        else:
            st.warning("Please enter some text.")


