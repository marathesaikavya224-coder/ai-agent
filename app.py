import streamlit as st
import requests
import uuid

# Page Configuration
st.set_page_config(
    page_title="NEURAL NEXUS // AI Command Core",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-Contrast Cinematic Sci-Fi HUD CSS Overhaul
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Share+Tech+Mono&display=swap');

    /* Global Deep Space Matrix Background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #0a0218 0%, #020005 70%, #000000 100%);
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Solid Matte-Black Cinematic Hero Box with Neon Frame */
    .cinematic-hero {
        background: linear-gradient(135deg, rgba(10, 5, 25, 0.95), rgba(3, 0, 8, 0.98));
        border: 2px solid #00ffcc;
        padding: 30px 35px;
        border-radius: 18px;
        box-shadow: 0 0 35px rgba(0, 255, 204, 0.25), inset 0 0 20px rgba(0, 255, 204, 0.1);
        margin-bottom: 25px;
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 2.2rem;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.6);
    }

    .hero-subtitle {
        color: #00ffcc;
        font-size: 0.95rem;
        font-family: 'Share Tech Mono', monospace;
        margin-top: 8px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Holographic Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020005 0%, #080114 100%) !important;
        border-right: 2px solid rgba(0, 255, 204, 0.2);
    }

    /* Sci-Fi Glass Panels */
    .hud-panel {
        background: rgba(10, 5, 25, 0.85);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 255, 204, 0.3);
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
        margin-bottom: 20px;
    }

    /* Pulsing Reactor Dot */
    @keyframes reactorPulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 204, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 255, 204, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 204, 0); }
    }

    .reactor-core {
        width: 12px;
        height: 12px;
        background: #00ffcc;
        border-radius: 50%;
        display: inline-block;
        animation: reactorPulse 2s infinite;
        margin-right: 8px;
    }

    /* Custom Input Terminal Bar */
    .stChatInput input {
        background-color: #05020d !important;
        color: #00ffcc !important;
        border: 2px solid #00ffcc !important;
        border-radius: 12px !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 1rem !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }
    
    .stChatInput input:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 25px rgba(168, 85, 247, 0.4) !important;
    }

    /* Metrics Styling */
    [data-testid="stMetricValue"] {
        font-family: 'Orbitron', sans-serif !important;
        color: #00ffcc !important;
        font-size: 1.6rem !important;
        text-shadow: 0 0 10px rgba(0,255,204,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "candidate_id" not in st.session_state:
    st.session_state.candidate_id = "CANDIDATE_001"
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.q_count = 0
    st.session_state.interview_complete = False
    
    try:
        response = requests.post(
            "http://localhost:8000/api/v1/interview",
            json={
                "session_id": st.session_state.session_id,
                "candidate_id": st.session_state.candidate_id,
                "message": None
            }
        )
        if response.status_code == 200:
            data = response.json()
            st.session_state.messages.append({"role": "assistant", "content": data["agent_response"]})
            st.session_state.q_count = data.get("metadata", {}).get("questions_asked_count", 1)
    except Exception as e:
        st.error(f"⚠️ NEURAL UPLINK OFFLINE. Boot backend via Uvicorn: {e}")

# --- SIDEBAR HUD CONTROLS ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; font-family: Orbitron; color: #00ffcc; letter-spacing: 3px; text-shadow: 0 0 15px rgba(0,255,204,0.4);'>⚛️ NEXUS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a855f7; font-size: 0.75rem; letter-spacing: 2px;'>SYSTEM TELEMETRY MATRIX</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=80", use_container_width=True)
    
    st.markdown("""
        <div class="hud-panel" style="margin-top: 15px;">
            <span style="color: #94a3b8; font-size: 0.7rem; letter-spacing: 1px;">CONNECTED TARGET</span><br>
            <b style="color: #ffffff; font-family: Orbitron; font-size: 1.1rem; text-shadow: 0 0 10px #00ffcc;">CANDIDATE_001</b><br><br>
            <div style="display: flex; align-items: center;">
                <span class="reactor-core"></span>
                <span style="color: #00ffcc; font-size: 0.85rem; font-weight: bold; letter-spacing: 1px;">SYNCHRONIZED</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Live Grid Metrics")
    q_target = 8
    current_q = min(st.session_state.q_count, q_target)
    progress_pct = current_q / q_target
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Depth", value=f"{current_q}/{q_target}")
    with col2:
        status_txt = "SECURE" if st.session_state.interview_complete else "ACTIVE"
        st.metric(label="Status", value=status_txt)
        
    st.markdown("<p style='font-size: 0.7rem; color: #a855f7; letter-spacing: 1px; margin-bottom: 5px;'>SEQUENCE PROGRESS</p>", unsafe_allow_html=True)
    st.progress(progress_pct)
    
    st.markdown("---")
    if st.button("🔄 HARD REBOOT MATRIX", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# --- MAIN CINEMATIC BANNER ---
st.markdown("""
    <div class="cinematic-hero">
        <h1 class="hero-title">⚡ Autonomous AI Core</h1>
        <p class="hero-subtitle">SECURE TERMINAL // ARCHITECTURAL TRADE-OFF DEFENSE MATRIX</p>
    </div>
""", unsafe_allow_html=True)

# Render Chat Stream
for message in st.session_state.messages:
    role = message["role"]
    avatar_icon = "🪐" if role == "assistant" else "💻"
    with st.chat_message(role, avatar=avatar_icon):
        st.markdown(message["content"])

# Completion Block or Chat Input Box
if st.session_state.get("interview_complete", False):
    st.balloons()
    st.markdown("""
        <div style="background: rgba(0, 255, 204, 0.1); border: 2px solid #00ffcc; padding: 25px; border-radius: 16px; text-align: center; margin-top: 25px; box-shadow: 0 0 40px rgba(0, 255, 204, 0.3);">
            <h2 style="color: #00ffcc; font-family: Orbitron; margin: 0; text-shadow: 0 0 20px rgba(0,255,204,0.7);">🚀 EVALUATION SEQUENCE SECURED</h2>
            <p style="color: #e2e8f0; margin-top: 10px; font-size: 1.1rem; letter-spacing: 1px;">All architectural matrices successfully verified. Neural uplink terminating with honors.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    if prompt := st.chat_input("Transmit your architectural decision / system breakdown..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="💻"):
            st.markdown(prompt)

        try:
            response = requests.post(
                "http://localhost:8000/api/v1/interview",
                json={
                    "session_id": st.session_state.session_id,
                    "candidate_id": st.session_state.candidate_id,
                    "message": prompt
                }
            )
            if response.status_code == 200:
                data = response.json()
                agent_reply = data["agent_response"]
                st.session_state.q_count = data.get("metadata", {}).get("questions_asked_count", st.session_state.q_count)
                st.session_state.interview_complete = data.get("metadata", {}).get("interview_complete", False)
                
                st.session_state.messages.append({"role": "assistant", "content": agent_reply})
                with st.chat_message("assistant", avatar="🪐"):
                    st.markdown(agent_reply)
                
                st.rerun()
            else:
                st.error(f"Error from server: {response.text}")
        except Exception as e:
            st.error(f"Connection failed: {e}")