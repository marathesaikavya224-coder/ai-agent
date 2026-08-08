
import os
import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="AUTONOMOUS AI CORE // CINEMATIC MATRIX",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultimate Cyberpunk Cinematic CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap');

    /* Global Dark Cinematic Theme */
    .stApp {
        background: radial-gradient(circle at center, #0a0f1d 0%, #020408 100%);
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
    }

    /* Hide standard header elements */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Custom Cinematic Title Banner */
    .cinematic-header {
        background: linear-gradient(90deg, rgba(0,255,204,0.1) 0%, rgba(0,119,255,0.2) 100%);
        border: 2px solid #00ffcc;
        box-shadow: 0 0 25px rgba(0,255,204,0.4);
        padding: 25px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 30px;
        backdrop-filter: blur(5px);
    }
    .cinematic-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 2.8rem;
        color: #ffffff;
        text-shadow: 0 0 15px #00ffcc, 0 0 30px #00ffcc;
        letter-spacing: 4px;
        margin: 0;
    }
    .cinematic-subtitle {
        font-family: 'Share Tech Mono', monospace;
        color: #8be9fd;
        font-size: 1.1rem;
        letter-spacing: 3px;
        margin-top: 10px;
        text-transform: uppercase;
    }

    /* Futuristic Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #050811;
        border-right: 1px solid rgba(0,255,204,0.2);
    }
    
    /* Glowing HUD Cards */
    .hud-card {
        background: rgba(11, 15, 25, 0.8);
        border: 1px solid #00ffcc;
        border-radius: 6px;
        padding: 15px;
        box-shadow: inset 0 0 15px rgba(0,255,204,0.1);
        margin-bottom: 15px;
    }

    /* Custom Input Box */
    .stChatInput input {
        background-color: #050811 !important;
        color: #00ffcc !important;
        border: 2px solid #00ffcc !important;
        font-family: 'Share Tech Mono', monospace !important;
        border-radius: 4px !important;
        box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;
    }

    /* Cinematic Chat Bubbles */
    .stChatMessage {
        background: rgba(16, 24, 39, 0.6) !important;
        border: 1px solid rgba(0,255,204,0.3);
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Cinematic Sidebar HUD
with st.sidebar:
    st.markdown("<h3 style='font-family: Orbitron; color: #00ffcc;'>SYSTEM STATUS</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class="hud-card">
            <p style="margin:0; font-size: 0.9rem; color: #8be9fd;">CONNECTED TARGET</p>
            <h4 style="margin:0; color: #ffffff; font-family: Orbitron;">CANDIDATE_001</h4>
            <p style="margin:5px 0 0 0; color: #00ffcc; font-weight: bold;">🟢 SYNCHRONIZED</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 LIVE GRID METRICS")
    st.metric(label="Evaluation Depth", value="1/8")
    st.metric(label="Core Temp", value="36.4°C")
    st.metric(label="Defense Status", value="ACTIVE")
    
    st.markdown("---")
    if st.button("🔄 HARD REBOOT MATRIX", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Cinematic Header Banner
st.markdown("""
    <div class="cinematic-header">
        <h1 class="cinematic-title">⚡ AUTONOMOUS AI CORE</h1>
        <div class="cinematic-subtitle">SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX</div>
    </div>
""", unsafe_allow_html=True)

# Initialize Groq client securely
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("⚠️ CRITICAL: Groq API Key missing. Configure in Streamlit Secrets.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # Manage chat history state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "INITIALIZED. Welcome, Candidate 001. Present your architectural decision or system breakdown for deep-tier evaluation."}
        ]

    # Render chat interface history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # High-tech user input prompt
    user_input = st.chat_input("Transmit your architectural decision / system breakdown...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("DECODING ARCHITECTURAL VULNERABILITIES..."):
                try:
                    response = client.chat.completions.create(
                        model="llama3-70b-8192",
                        messages=[
                            {"role": "system", "content": "You are an intense, high-tech cinematic AI technical interviewer evaluating architectural trade-offs, scaling, failure modes, and distributed systems in a high-stakes cyber environment."},
                            *st.session_state.messages
                        ]
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Transmission Interrupted: {e}")