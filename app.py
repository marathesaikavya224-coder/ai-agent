import os
import streamlit as st
from openai import OpenAI
import time

# Page configuration
st.set_page_config(
    page_title="⚡ AI COHORT INTERVIEW AGENT // NEXUS MATRIX",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
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
        padding: 35px 20px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: clamp(1.6rem, 2.8vw, 2.4rem);
        color: #ffffff;
        text-shadow: 0 0 20px #00ffcc, 0 0 40px #0077ff;
        letter-spacing: 3px;
        margin: 0;
    }

    .hero-subtitle {
        font-family: 'JetBrains Mono', monospace;
        color: #38bdf8;
        font-size: clamp(0.7rem, 1.2vw, 0.9rem);
        font-weight: 700;
        letter-spacing: 2px;
        margin-top: 12px;
        text-transform: uppercase;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }

    /* Sidebar HUD Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #070a14 0%, #020408 100%);
        border-right: 1px solid rgba(0, 255, 204, 0.2);
    }

    .sidebar-hud {
        background: rgba(13, 17, 36, 0.8);
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 12px;
        padding: 14px;
        box-shadow: inset 0 0 15px rgba(0, 255, 204, 0.05);
        margin-bottom: 15px;
    }

    .metric-card {
        background: rgba(13, 17, 36, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 10px;
        padding: 12px 15px;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
    }
    .metric-label {
        font-size: 0.75rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin: 0;
    }
    .metric-value {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.1rem;
        color: #00ffcc;
        font-weight: 700;
        margin: 4px 0 0 0;
        text-shadow: 0 0 8px rgba(0, 255, 204, 0.4);
    }

    /* Pulsing Live Radar Dot */
    .radar-dot {
        height: 10px;
        width: 10px;
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

    /* Cinematic Action Button */
    .stButton button {
        background: linear-gradient(135deg, #00ffcc 0%, #0077ff 100%);
        color: #05070c;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        box-shadow: 0 0 30px #00ffcc;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# Cinematic Sidebar HUD Panel
with st.sidebar:
    st.markdown("<h2 style='font-family: Orbitron; color: #00ffcc; text-align: center; font-size: 1.2rem;'>🛡️ COMMAND HUD 🛡️</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="sidebar-hud">
            <p style="margin:0; font-size: 0.75rem; color: #94a3b8;">🎯 ACTIVE TARGET</p>
            <h3 style="margin:4px 0; color: #ffffff; font-family: Orbitron; font-size: 0.95rem;">CANDIDATE_001</h3>
            <p style="margin:6px 0 0 0; color: #10b981; font-weight: 600; font-size: 0.75rem;"><span class="radar-dot"></span> STATUS: SYNCHRONIZED</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 0.85rem; color: #38bdf8; font-weight: 600; margin-bottom: 8px;'>📊 LIVE TELEMETRY</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="metric-card">
            <p class="metric-label">⚡ System Load</p>
            <p class="metric-value">12.4% <span style="font-size:0.7rem; color:#10b981;">(-1.1%)</span></p>
        </div>
        <div class="metric-card">
            <p class="metric-label">🔥 Core Temp</p>
            <p class="metric-value">37.2°C <span style="font-size:0.7rem; color:#f59e0b;">(+0.3°C)</span></p>
        </div>
        <div class="metric-card">
            <p class="metric-label">🛡️ Defense Matrix</p>
            <p class="metric-value" style="font-size: 0.9rem;">ACTIVE // TIER-1</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("🔄 HARD REBOOT MATRIX", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Cinematic Hero Banner
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">⚡ AUTONOMOUS AI CORE ⚡</h1>
        <div class="hero-subtitle">🔮 SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX 🛡️</div>
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