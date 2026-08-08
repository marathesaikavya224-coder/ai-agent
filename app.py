import os
import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="AI Cohort Interview Agent", page_icon="⚡", layout="wide")

# Custom UI styling to match your theme
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

st.markdown("## ⚡ AUTONOMOUS AI CORE")
st.markdown("### SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX")

# Initialize Groq client using Streamlit secrets or environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("Groq API Key not found! Please set the GROQ_API_KEY environment variable or Streamlit secret.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # Chat interface
    user_input = st.text_input("Transmit your architectural decision / system breakdown...")

    if user_input:
        with st.spinner("Analyzing architecture..."):
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",  # Or your preferred Groq model
                    messages=[
                        {"role": "system", "content": "You are an AI technical interviewer evaluating architecture trade-offs."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response.choices[0].message.content
                st.write(answer)
            except Exception as e:
                st.error(f"Error connecting to AI Core: {e}")