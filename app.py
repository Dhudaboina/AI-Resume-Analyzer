import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_similarity, missing_skills

st.title("AI Resume Analyzer & Job Matcher")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    resume_text = extract_text_from_pdf(uploaded_file)
    
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_desc)

    score = calculate_similarity(clean_resume, clean_job)
    missing = missing_skills(clean_resume, clean_job)

    st.subheader(f"Match Score: {score}%")

    st.subheader("Missing Skills:")
    for skill in missing:
        st.write(f"- {skill}")