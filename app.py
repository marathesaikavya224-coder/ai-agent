import os
import streamlit as st
from openai import OpenAI
import time

# Page configuration
st.set_page_config(
    page_title="⚡ AUTONOMOUS AI CORE // MATRIX HUD ⚡",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Cinematic Neon Cyberpunk CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: linear-gradient(135deg, #020205 0%, #080c19 50%, #020205 100%);
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
    }

    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Glowing Matrix Header Banner */
    .matrix-banner {
        background: radial-gradient(circle, rgba(0,255,204,0.15) 0%, rgba(5,11,24,0.9) 100%);
        border: 2px solid #00ffcc;
        box-shadow: 0 0 30px rgba(0,255,204,0.3), inset 0 0 20px rgba(0,255,204,0.2);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        animation: pulseGlow 3s infinite alternate;
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 20px rgba(0,255,204,0.2); }
        100% { box-shadow: 0 0 40px rgba(0,255,204,0.6); }
    }

    .matrix-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 3rem;
        color: #ffffff;
        text-shadow: 0 0 10px #00ffcc, 0 0 25px #00ffcc, 0 0 50px #0077ff;
        letter-spacing: 5px;
        margin: 0;
    }

    .matrix-sub {
        font-family: 'Share Tech Mono', monospace;
        color: #ff007f;
        font-size: 1.2rem;
        letter-spacing: 4px;
        margin-top: 10px;
        text-transform: uppercase;
        text-shadow: 0 0 8px rgba(255,0,127,0.6);
    }

    /* Holographic HUD Cards */
    .hud-box {
        background: rgba(10, 15, 30, 0.85);
        border: 1px solid #00ffcc;
        border-radius: 8px;
        padding: 18px;
        box-shadow: 0 0 15px rgba(0,255,204,0.15);
        margin-bottom: 15px;
    }

    /* Glowing Buttons */
    .stButton button {
        background: linear-gradient(45deg, #ff007f, #00ffcc);
        color: #020205;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        border: none;
        border-radius: 4px;
        box-shadow: 0 0 15px rgba(255,0,127,0.4);
        transition: 0.3s;
    }
    .stButton button:hover {
        box-shadow: 0 0 25px #00ffcc;
        transform: scale(1.02);
    }

    /* Futuristic Chat Input */
    .stChatInput input {
        background-color: #050814 !important;
        color: #00ffcc !important;
        border: 2px solid #ff007f !important;
        font-family: 'Share Tech Mono', monospace !important;
        border-radius: 6px !important;
        box-shadow: 0 0 15px rgba(255,0,127,0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Cinematic Sidebar HUD Panel with Emojis & Icons
with st.sidebar:
    st.markdown("<h2 style='font-family: Orbitron; color: #ff007f; text-align: center;'>🛡️ CORE HUD 🛡️</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="hud-box">
            <p style="margin:0; font-size: 0.85rem; color: #8be9fd;">🎯 TARGET ENTITY</p>
            <h3 style="margin:2px 0; color: #ffffff; font-family: Orbitron;">CANDIDATE_001</h3>
            <p style="margin:5px 0 0 0; color: #00ffcc; font-weight: bold;">🟢 LINK: SYNCHRONIZED</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 LIVE MATRIX METRICS")
    st.metric(label="⚡ System Load", value="14.2%", delta="+1.2%")
    st.metric(label="🔥 Core Temp", value="38.9°C", delta="-0.4°C")
    st.metric(label="🛡️ Defense Matrix", value="ACTIVE // LEVEL 5")
    
    st.markdown("---")
    if st.button("🔄 HARD REBOOT MATRIX", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Cinematic Header Banner with Visual Icons
st.markdown("""
    <div class="matrix-banner">
        <h1 class="matrix-title">⚡ AUTONOMOUS AI CORE ⚡</h1>
        <div class="matrix-sub">🚀 SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX 🛡️</div>
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
    st.error("🚨 CRITICAL ALERT: Groq API Key missing! Configure it in Streamlit Cloud Secrets.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # Manage chat history state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "🤖 **INITIALIZED.** Welcome, Candidate 001. Transmit your architectural breakdown or scaling design for high-tier evaluation. ⚡"}
        ]

    # Render chat history with visual flair
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # High-octane chat input prompt
    user_input = st.chat_input("💬 Transmit your architectural decision / system breakdown...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            # Real-time simulation effect
            message_placeholder = st.empty()
            message_placeholder.markdown("🔍 *[DECODING ARCHITECTURAL VULNERABILITIES & SCALING TRADE-OFFS...]*")
            time.sleep(0.6)
            
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[
                        {"role": "system", "content": "You are an intense, high-tech cybernetic AI technical interviewer evaluating architectural trade-offs, scaling bottlenecks, and system failures. Keep your tone immersive, sharp, and high-stakes. Use formatting, icons, and structured bullet points."},
                        *st.session_state.messages
                    ]
                )
                answer = response.choices[0].message.content
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                message_placeholder.error(f"❌ Transmission Interrupted: {e}")