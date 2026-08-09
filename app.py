import os
import streamlit as st
from openai import OpenAI
import time

# Page configuration
st.set_page_config(
    page_title="⚡ AI COHORT INTERVIEW AGENT // NEXUS MATRIX",
    page_icon="🔮",
    layout="wide"
)

# Ultra-Enhanced Cinematic Cyberpunk CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@300;400;700&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 20%, #0d1124 0%, #05070c 70%, #010204 100%);
        color: #f1f5f9;
        font-family: 'JetBrains Mono', monospace;
    }

    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Advanced Glowing Hero Banner */
    .hero-banner {
        position: relative;
        background: linear-gradient(135deg, rgba(13,17,36,0.9), rgba(5,7,12,0.95)), 
                    url('https://images.unsplash.com/photo-1639762681485-074b7f938ba0?q=80&w=1600&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border: 2px solid rgba(0, 255, 204, 0.5);
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.2), inset 0 0 30px rgba(0, 119, 255, 0.15);
        padding: 30px 20px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: clamp(1.5rem, 2.5vw, 2.2rem);
        color: #ffffff;
        text-shadow: 0 0 20px #00ffcc, 0 0 40px #0077ff;
        letter-spacing: 3px;
        margin: 0;
    }

    .hero-subtitle {
        font-family: 'JetBrains Mono', monospace;
        color: #38bdf8;
        font-size: clamp(0.65rem, 1.1vw, 0.85rem);
        font-weight: 700;
        letter-spacing: 2px;
        margin-top: 10px;
        text-transform: uppercase;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }

    .metric-card {
        background: rgba(13, 17, 36, 0.75);
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 10px;
        padding: 12px 15px;
        text-align: center;
        box-shadow: inset 0 0 15px rgba(0, 255, 204, 0.05);
    }
    .metric-label {
        font-size: 0.7rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin: 0;
    }
    .metric-value {
        font-family: 'Orbitron', sans-serif;
        font-size: 1rem;
        color: #00ffcc;
        font-weight: 700;
        margin: 4px 0 0 0;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.4);
    }

    /* Pulsing Live Radar Dot */
    .radar-dot {
        height: 8px;
        width: 8px;
        background-color: #10b981;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 10px #10b981;
        animation: pulseRadar 1.5s infinite;
    }
    @keyframes pulseRadar {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }

    /* Custom Input Box */
    .stChatInput input {
        background-color: #070a14 !important;
        color: #00ffcc !important;
        border: 2px solid rgba(0, 255, 204, 0.6) !important;
        font-family: 'JetBrains Mono', monospace !important;
        border-radius: 10px !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.15) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main Cinematic Hero Banner
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">⚡ AUTONOMOUS AI CORE ⚡</h1>
        <div class="hero-subtitle">🔮 SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX 🛡️</div>
    </div>
""", unsafe_allow_html=True)

# Dashboard Telemetry Row (Visible directly on top, no sidebar needed!)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="metric-card">
            <p class="metric-label">🎯 Active Target</p>
            <p class="metric-value">CANDIDATE_001</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <p class="metric-label">⚡ System Load</p>
            <p class="metric-value">12.4%</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <p class="metric-label">🔥 Core Temp</p>
            <p class="metric-value">37.2°C</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="metric-card">
            <p class="metric-label">🛡️ Matrix Status</p>
            <p class="metric-value" style="font-size: 0.85rem;"><span class="radar-dot"></span> SYNCHRONIZED</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Initialize Groq client securely
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("🚨 CRITICAL ALERT: Groq API Key missing! Please configure it in Streamlit Cloud Secrets.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "🤖 **SYSTEM INITIALIZED.** Welcome, Candidate 001. Transmit your architectural breakdown, scaling logic, or system trade-offs for high-tier evaluation. Let's begin! ⚡"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("💬 Transmit your architectural decision / system breakdown...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("🔍 *[DECODING ARCHITECTURAL VULNERABILITIES & SCALING TRADE-OFFS...]*")
            time.sleep(0.4)
            
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are an elite, high-tech cybernetic AI technical interviewer evaluating architectural trade-offs, scaling bottlenecks, and system design failures. Maintain an immersive, professional, yet sharp tone. Use clear headings, emojis, and bullet points to structure your feedback."},
                        *st.session_state.messages
                    ]
                )
                answer = response.choices[0].message.content
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                message_placeholder.error(f"❌ Transmission Interrupted: {e}")