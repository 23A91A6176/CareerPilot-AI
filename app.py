import streamlit as st
from PyPDF2 import PdfReader
import re

# Page Config
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 CareerPilot AI")
st.subheader("AI Career Guidance & Resume Analyzer")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Your Resume PDF",
    type=["pdf"]
)

# Extract Resume Text
def extract_resume_text(pdf_file):
    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text

# Skill Keywords
skills = [
    "python",
    "java",
    "c",
    "machine learning",
    "deep learning",
    "sql",
    "html",
    "css",
    "javascript",
    "power bi",
    "tableau",
    "ai",
    "data science"
]

# Analyze Resume
def analyze_resume(text):

    text_lower = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text_lower:
            found_skills.append(skill)

    ats_score = len(found_skills) * 10

    if ats_score > 100:
        ats_score = 100

    missing_skills = []

    recommended = [
        "React",
        "Streamlit",
        "LangChain",
        "Generative AI",
        "Docker",
        "Cloud"
    ]

    for item in recommended:
        if item.lower() not in text_lower:
            missing_skills.append(item)

    return ats_score, found_skills, missing_skills

# Main App
if uploaded_file:

    st.success("Resume Uploaded Successfully!")

    resume_text = extract_resume_text(uploaded_file)

    with st.expander("View Resume Text"):
        st.write(resume_text)

    if st.button("Analyze Resume"):

        ats_score, found_skills, missing_skills = analyze_resume(resume_text)

        st.write("## 📊 ATS Score")
        st.progress(ats_score / 100)
        st.write(f"### {ats_score}/100")

        st.write("## ✅ Detected Skills")

        for skill in found_skills:
            st.success(skill)

        st.write("## ❌ Missing Recommended Skills")

        for skill in missing_skills:
            st.warning(skill)

        st.write("## 🎯 Career Recommendations")

        st.info("""
        - Learn Generative AI
        - Build Full Stack AI Projects
        - Practice DSA
        - Improve GitHub Profile
        - Deploy Projects Online
        """)

        st.write("## 💡 Suggested AIML Projects")

        st.success("""
        1. AI Interview Coach
        2. AI PDF Chatbot
        3. AI Study Assistant
        4. Face Recognition System
        5. AI Resume Analyzer
        """)

        st.write("## 🎤 Interview Questions")

        st.warning("""
        1. Explain your machine learning projects.
        2. Difference between AI and ML?
        3. What is overfitting?
        4. Explain supervised learning.
        5. Tell me about yourself.
        """)