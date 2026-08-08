import os
import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="AI Cohort Interview Agent", page_icon="⚡", layout="wide")

# Custom UI styling for the cyber security theme
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput input { background-color: #161b22; color: #ffffff; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

# Sidebar layout matching your cyber theme
with st.sidebar:
    st.markdown("### CONNECTED TARGET")
    st.markdown("```CANDIDATE_001```")
    st.markdown("🟢 **SYNCHRONIZED**")
    st.markdown("---")
    st.markdown("### 📊 Live Grid Metrics")
    st.metric(label="Depth", value="0/8")
    st.metric(label="Status", value="ACTIVE")
    st.markdown("---")
    if st.button("🔄 HARD REBOOT MATRIX"):
        st.rerun()

# Main Header
st.markdown("## ⚡ AUTONOMOUS AI CORE")
st.markdown("### SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX")
st.markdown("---")

# Initialize Groq client using Streamlit secrets or environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("⚠️ Groq API Key not found! Please add your GROQ_API_KEY to Streamlit Cloud Secrets.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # Chat interface input box
    user_input = st.text_input("Transmit your architectural decision / system breakdown...")

    if user_input:
        with st.spinner("Analyzing architecture..."):
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192", 
                    messages=[
                        {"role": "system", "content": "You are an aggressive and rigorous AI technical interviewer evaluating architecture trade-offs."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response.choices[0].message.content
                st.markdown("### 🧠 Core Response:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error connecting to AI Core: {e}")