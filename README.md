
# AI Hiring Assistant

## Description
TalentScout AI Hiring Assistant is an intelligent chatbot designed to streamline the initial stages of technical recruitment. It collects candidate details, dynamically generates technical questions based on their skills, and provides a context-aware conversational experience.

---

## Features
- Step-by-step collection of candidate information:
  - Full Name
  - Email
  - Phone Number
  - Years of Experience
  - Current Location
  - Desired Role
  - Tech Stack
- Dynamic generation of 3–5 technical questions tailored to the candidate’s declared tech stack.
- Context-aware responses and fallback handling for irrelevant inputs.
- Graceful conversation termination with exit keywords.
- Optional saving of candidate info and answers for review.

---

## Tech Stack
- **Frontend & UI:** Streamlit  
- **Backend & AI Engine:** Python, OpenRouter GPT/Grok models  
- **Data Handling:** Pandas for storing candidate info and answers  
- **Environment Management:** dotenv for API key management
- **API keys :** https://openrouter.ai/

---

## Use
- Automates initial screening for technical recruitment.  
- Helps recruiters generate relevant technical questions instantly.  
- Provides candidates a smooth and interactive experience during interviews.  

---

## Installation
```bash
# Clone repository
git clone https://github.com/ShantanuGame/Hiring-Assistant-AI.git
cd Hiring-Assistant-AI

# Install required packages
pip install -r requirements.txt

# Run locally
streamlit run app.py

```

## Note:- You will need to update the API key from OPENROUTER 
