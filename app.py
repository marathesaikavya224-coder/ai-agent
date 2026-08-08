import os
import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="AI Cohort Interview Agent - Cinematic Matrix", page_icon="⚡", layout="wide")

# Custom Cyberpunk / Cinematic CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #05050a;
        color: #00ffcc;
    }
    .sidebar .sidebar-content {
        background-color: #0b0f19;
    }
    h1, h2, h3 {
        color: #00ffcc !important;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px rgba(0,255,204,0.5);
    }
    .stTextInput input {
        background-color: #0b0f19;
        color: #00ffcc;
        border: 1px solid #00ffcc;
        box-shadow: 0 0 5px rgba(0,255,204,0.3);
    }
    .stButton button {
        background: linear-gradient(45deg, #00ffcc, #0077ff);
        color: #000;
        font-weight: bold;
        border: none;
        box-shadow: 0 0 10px rgba(0,255,204,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar layout for cinematic metrics
with st.sidebar:
    st.markdown("### CONNECTED TARGET")
    st.markdown("```CANDIDATE_001```")
    st.markdown("🟢 **SYNCHRONIZED**")
    st.markdown("---")
    st.markdown("### 📊 Live Grid Metrics")
    st.metric(label="Depth", value="1/8")
    st.metric(label="Status", value="ACTIVE")
    st.markdown("---")
    st.markdown("### 🛡️ DEFENSE MATRIX")
    st.progress(0.25)
    if st.button("🔄 HARD REBOOT MATRIX"):
        st.session_state.messages = []
        st.rerun()

# Main Cinematic Header
st.markdown("""
    <div style="text-align: center; padding: 10px; border-bottom: 2px solid #00ffcc; margin-bottom: 20px;">
        <h1 style="margin: 0; font-size: 2.5rem;">⚡ AUTONOMOUS AI CORE</h1>
        <p style="color: #8be9fd; letter-spacing: 2px; font-family: 'Courier New', monospace;">SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX</p>
    </div>
""", unsafe_allow_html=True)

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("⚠️ CRITICAL ERROR: Groq API Key not detected in environment or Streamlit secrets.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # Chat history state for conversation memory
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Interactive Chat Input
    user_input = st.chat_input("Transmit your architectural decision / system breakdown...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Decoding architecture trade-offs..."):
                try:
                    response = client.chat.completions.create(
                        model="llama3-70b-8192",
                        messages=[
                            {"role": "system", "content": "You are an intense, highly intelligent AI technical interviewer evaluating architectural trade-offs, system design, scaling, and failure modes in a high-stakes cyberpunk evaluation environment."},
                            *st.session_state.messages
                        ]
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Core Transmission Failed: {e}")