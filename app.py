import streamlit as st
import joblib
import pandas as pd
from datetime import datetime


model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")
courses = joblib.load('courses.pkl')

st.set_page_config(page_title="Alcademy - Course Recommendation", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .stButton button {
        background-color: #0099ff;
        color: white;
        font-weight: bold;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #111;
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Alcademy")
st.subheader("Your Personal Udemy Course Recommender")

topic = st.text_input("Enter a topic to find relevant courses (e.g., python, design, guitar)", "")

if st.button("🔍 Recommend Courses"):
    if topic:
        filtered = courses[courses['course_title'].str.lower().str.contains(topic.lower(), na=False)]
        if not filtered.empty:
            st.success(f"Found {len(filtered)} course(s) related to '{topic}':")
            for _, row in filtered.iterrows():
                st.markdown(f"""
                <div style="background-color: #1e1e1e; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
                    <h4 style="color:#00c6ff;">{row['course_title']}</h4>
                    <ul>
                        <li><strong>Subject:</strong> {row['subject']}</li>
                        <li><strong>Price:</strong> {row['price']}</li>
                        <li><strong>Lectures:</strong> {row['num_lectures']}</li>
                        <li><strong>Level:</strong> {row['level']}</li>
                        <li><strong>Duration:</strong> {row['content_duration']}</li>
                    </ul>
                    <a href="{row['url']}" target="_blank" style="color:#00ff99;">🔗 View Course</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No matching courses found. Try a different topic.")
    else:
        st.error("Please enter a topic.")

st.markdown("""
<div class="footer">
    <p>Made with ❤️ by <strong>Faisal Khan</strong> | 
    <a href="https://khanfaisal.netlify.app" target="_blank">Portfolio</a> |
    <a href="https://linkedin.com/in/khanfaisal79960" target="_blank">LinkedIn</a> |
    <a href="https://medium.com/@khanfaisal79960" target="_blank">Medium</a> |
    <a href="https://instagram.com/mr._perfect_1004" target="_blank">Instagram</a> |
    <a href="https://github.com/khanfaisal79960" target="_blank">GitHub</a></p>
</div>
""", unsafe_allow_html=True)
