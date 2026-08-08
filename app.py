import os
import streamlit as st
from openai import OpenAI
import time

# Page configuration
st.set_page_config(
    page_title="⚡ AI COHORT INTERVIEW AGENT // CINEMATIC MATRIX",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Cinematic CSS with responsive, perfectly-fitting typography
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #05050a 0%, #0b1021 50%, #020205 100%);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Perfectly proportioned hero banner to prevent awkward text wrapping */
    .hero-banner {
        position: relative;
        background: linear-gradient(to right, rgba(5,5,10,0.88), rgba(11,16,33,0.88)), 
                    url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1600&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border: 2px solid rgba(0, 255, 204, 0.4);
        box-shadow: 0 0 35px rgba(0, 255, 204, 0.25);
        padding: 30px 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 25px;
        width: 100%;
        box-sizing: border-box;
    }

    /* Fluid font scaling so text fits cleanly within any screen bounds */
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: clamp(1.8rem, 3.2vw, 2.6rem);
        color: #ffffff;
        text-shadow: 0 0 15px #00ffcc, 0 0 30px #0077ff;
        letter-spacing: 2px;
        margin: 0;
        white-space: nowrap;
    }

    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        color: #38bdf8;
        font-size: clamp(0.75rem, 1.4vw, 0.95rem);
        font-weight: 600;
        letter-spacing: 1.5px;
        margin-top: 10px;
        text-transform: uppercase;
        white-space: nowrap;
    }

    /* Glowing Sidebar HUD Cards */
    .sidebar-hud {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 10px;
        padding: 15px;
        box-shadow: inset 0 0 15px rgba(0, 255, 204, 0.05);
        margin-bottom: 15px;
    }

    /* Custom Input Box Styling */
    .stChatInput input {
        background-color: #0b1021 !important;
        color: #00ffcc !important;
        border: 2px solid #00ffcc !important;
        font-family: 'Inter', sans-serif !important;
        border-radius: 8px !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2) !important;
    }

    /* Cinematic Action Button */
    .stButton button {
        background: linear-gradient(135deg, #00ffcc 0%, #0077ff 100%);
        color: #05050a;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        box-shadow: 0 0 25px #00ffcc;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# Cinematic Sidebar HUD Panel with Rich Visuals & Emojis
with st.sidebar:
    st.markdown("<h2 style='font-family: Orbitron; color: #00ffcc; text-align: center; font-size: 1.3rem;'>🛡️ COMMAND HUD 🛡️</h2>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="sidebar-hud">
            <p style="margin:0; font-size: 0.75rem; color: #94a3b8;">🎯 ACTIVE TARGET</p>
            <h3 style="margin:4px 0; color: #ffffff; font-family: Orbitron; font-size: 1rem;">CANDIDATE_001</h3>
            <p style="margin:4px 0 0 0; color: #10b981; font-weight: 600; font-size: 0.8rem;">🟢 STATUS: SYNCHRONIZED</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 LIVE TELEMETRY")
    st.metric(label="⚡ System Load", value="12.4%", delta="-1.1%")
    st.metric(label="🔥 Core Temp", value="37.2°C", delta="+0.3°C")
    st.metric(label="🛡️ Defense Matrix", value="ACTIVE // TIER-1")
    
    st.markdown("---")
    if st.button("🔄 HARD REBOOT MATRIX", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Cinematic Hero Banner with perfectly fitted text boundaries
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">⚡ AUTONOMOUS AI CORE ⚡</h1>
        <div class="hero-subtitle">🚀 SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX 🛡️</div>
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

    # Manage chat history state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "🤖 **SYSTEM INITIALIZED.** Welcome, Candidate 001. Transmit your architectural breakdown, scaling logic, or system trade-offs for high-tier evaluation. Let's begin! ⚡"}
        ]

    # Render chat history with cinematic formatting
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
            # Real-time simulation placeholder effect
            message_placeholder = st.empty()
            message_placeholder.markdown("🔍 *[DECODING ARCHITECTURAL VULNERABILITIES & SCALING TRADE-OFFS...]*")
            time.sleep(0.5)
            
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
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