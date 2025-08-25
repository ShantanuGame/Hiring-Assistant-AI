# app.py
import streamlit as st
import pandas as pd
from prompts import info_prompt, question_prompt, context_prompt
from llm import query_llm

# -------------------------------
# Streamlit Page Configuration
# -------------------------------
st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")
st.title("TalentScout Hiring Assistant")
st.write("Hello! Welcome to TalentScout. I will assist you with the initial screening. Type 'exit' anytime to quit.")

EXIT_KEYWORDS = ["exit", "quit", "bye"]

# -------------------------------
# Step 0: Optional Chat Input (Fallback)
# -------------------------------
user_input = st.text_input("Type your message here (optional)")
if user_input:
    if user_input.lower() in EXIT_KEYWORDS:
        st.write("Thank you for your time! We will review your responses and contact you soon.")
    else:
        context = context_prompt
        if 'candidate_info' in st.session_state:
            candidate = st.session_state['candidate_info']
            context += f"\nCandidate info: {candidate}"
        if 'answers' in st.session_state:
            context += f"\nPrevious answers: {st.session_state['answers']}"
        fallback_prompt = f"{context}\nCandidate typed: {user_input}\nRespond politely and stay on topic."
        bot_response = query_llm(fallback_prompt)
        st.write(bot_response)

# -------------------------------
# Step 1: Candidate Info Collection
# -------------------------------
st.header("Step 1: Enter Candidate Information")
with st.form(key="candidate_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50)
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (comma separated, e.g., Python, Django)")

    submit_info = st.form_submit_button("Submit Info")

if submit_info:
    candidate_info = {
        "name": name,
        "email": email,
        "phone": phone,
        "experience": experience,
        "position": position,
        "location": location,
        "tech_stack": tech_stack
    }
    st.session_state['candidate_info'] = candidate_info
    st.success("Candidate information saved! Proceeding to generate technical questions...")

# -------------------------------
# Step 2: Generate Technical Questions
# -------------------------------
if 'candidate_info' in st.session_state:
    candidate = st.session_state['candidate_info']
    st.header("Step 2: Technical Questions")
    
    # Generate prompt for LLM
    prompt = question_prompt(candidate['tech_stack'], candidate['experience'])
    
    # Query LLM for questions
    questions_text = query_llm(prompt)
    
    # Split questions into list
    questions = [q.strip() for q in questions_text.split("\n") if q.strip()]
    st.session_state['questions'] = questions
    
    # Display questions and collect answers
    st.subheader("Answer the following questions:")
    answers = {}
    for i, q in enumerate(questions, start=1):
        ans = st.text_area(f"Q{i}: {q}", key=f"ans_{i}")
        answers[q] = ans
    
    if st.button("Submit Answers"):
        st.session_state['answers'] = answers
        st.success("Answers saved! Thank you for participating.")
        
        # Optional: Save candidate info + answers to CSV
        df_info = pd.DataFrame([candidate])
        df_answers = pd.DataFrame([answers])
        df_info.to_csv("candidate_data.csv", mode='a', index=False, header=False)
        df_answers.to_csv("candidate_answers.csv", mode='a', index=False, header=False)