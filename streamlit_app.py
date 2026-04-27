"""
School Agent — Premium Streamlit UI v3
GDG London | Google ADK A2A Architecture
Fresh Interactive Color Theme
"""

import streamlit as st
import asyncio
import uuid
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), 'agents/.env'))
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="School Agent — GDG London",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg:       #0f0e17;
    --bg2:      #16152a;
    --bg3:      #1e1d35;
    --bg4:      #252440;
    --border:   rgba(255,255,255,0.07);
    --border2:  rgba(255,255,255,0.13);

    --purple:   #7c3aed;
    --violet:   #a855f7;
    --coral:    #ff6b6b;
    --mint:     #06d6a0;
    --amber:    #ffd60a;
    --sky:      #38bdf8;

    --purple-glow: rgba(124,58,237,0.25);
    --mint-glow:   rgba(6,214,160,0.2);
    --coral-glow:  rgba(255,107,107,0.2);

    --text:     #f0eeff;
    --text2:    #9892c8;
    --text3:    #4a4875;
    --r:        14px;
    --r2:       10px;
}

.stApp {
    background: var(--bg) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: var(--text) !important;
}

#MainMenu, footer, header, .stDeployButton { display:none !important; visibility:hidden !important; }
.block-container { padding:0 !important; max-width:100% !important; }

[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child { padding:0 !important; }

::-webkit-scrollbar { width:3px; }
::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:rgba(124,58,237,0.4); border-radius:99px; }

/* ── Sample query buttons ── */
.stButton > button {
    background: var(--bg3) !important;
    color: var(--text2) !important;
    border: 1px solid var(--border2) !important;
    border-radius: var(--r2) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 12px 14px !important;
    width: 100% !important;
    text-align: left !important;
    transition: all 0.18s ease !important;
    cursor: pointer !important;
    line-height: 1.5 !important;
    white-space: normal !important;
    height: auto !important;
    min-height: 52px !important;
}
.stButton > button:hover {
    background: var(--bg4) !important;
    border-color: var(--violet) !important;
    color: var(--text) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px var(--purple-glow) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* Clear button */
.clear-btn .stButton > button {
    background: transparent !important;
    border-color: rgba(255,107,107,0.25) !important;
    color: rgba(255,107,107,0.6) !important;
    text-align: center !important;
    font-size: 12px !important;
    min-height: 36px !important;
    padding: 6px 16px !important;
}
.clear-btn .stButton > button:hover {
    background: rgba(255,107,107,0.08) !important;
    border-color: var(--coral) !important;
    color: var(--coral) !important;
    box-shadow: none !important;
    transform: none !important;
}

[data-testid="stChatInput"] {
    background: var(--bg2) !important;
    border-top: 1px solid var(--border) !important;
    padding: 16px 32px !important;
}
[data-testid="stChatInput"] textarea {
    background: var(--bg3) !important;
    border: 1px solid var(--border2) !important;
    border-radius: var(--r) !important;
    color: var(--text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: var(--violet) !important;
    box-shadow: 0 0 0 3px var(--purple-glow) !important;
}

.stSpinner > div { border-top-color: var(--violet) !important; }

[data-testid="stChatInput"] {
    background: linear-gradient(135deg,rgba(124,58,237,0.05),rgba(6,214,160,0.03)) !important;
    border-top: 1px solid rgba(124,58,237,0.2) !important;
    padding: 20px 36px !important;
}
[data-testid="stChatInput"] textarea {
    background: var(--bg3) !important;
    border: 1px solid rgba(124,58,237,0.25) !important;
    border-radius: 16px !important;
    color: var(--text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
    padding: 14px 20px !important;
    transition: all 0.2s ease !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: var(--violet) !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.15), 0 4px 24px rgba(124,58,237,0.1) !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #4a4875 !important;
    font-style: italic !important;
}
[data-testid="stChatInput"] button {
    background: linear-gradient(135deg,#7c3aed,#a855f7) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 12px rgba(124,58,237,0.4) !important;
}
[data-testid="stChatInput"] button:hover {
    transform: scale(1.08) !important;
    box-shadow: 0 6px 20px rgba(124,58,237,0.5) !important;
}
[data-testid="stChatInput"] button svg { fill:white !important; stroke:white !important; }
</style>
""", unsafe_allow_html=True)

import streamlit.components.v1 as components
components.html("""
<script>
const placeholders = [
    "Ask anything — English, Maths, Science, History, Geography, CS...",
    "💬 Try: What is the difference between a metaphor and a simile?",
    "📐 Try: Solve 2x² + 5x - 3 = 0 step by step",
    "🔬 Try: Explain Newton's Third Law with examples",
    "📜 Try: What caused World War 1?",
    "🌍 Try: What is the capital of New Zealand?",
    "💻 Try: Write a Python Fibonacci function",
    "🧠 Follow-up questions work too — memory is ON!"
];
let idx = 0;
function rotate() {
    const areas = window.parent.document.querySelectorAll('[data-testid="stChatInput"] textarea');
    areas.forEach(el => { if (!el.value) el.setAttribute('placeholder', placeholders[idx % placeholders.length]); });
    idx++;
}
rotate();
setInterval(rotate, 4000);
</script>
""", height=0)


# ─── Agent config ─────────────────────────────────────────────────────────────
AGENTS = {
    "english_teacher":   {"emoji": "📚", "color": "#38bdf8", "label": "English",   "topics": "Grammar · Essays · Literature · Poetry", "r": 56,  "g": 189, "b": 248},
    "maths_teacher":     {"emoji": "📐", "color": "#a855f7", "label": "Maths",     "topics": "Algebra · Calculus · Geometry · Stats",  "r": 168, "g": 85,  "b": 247},
    "science_teacher":   {"emoji": "🔬", "color": "#06d6a0", "label": "Science",   "topics": "Physics · Chemistry · Biology",          "r": 6,   "g": 214, "b": 160},
    "history_teacher":   {"emoji": "📜", "color": "#ffd60a", "label": "History",   "topics": "Events · Civilisations · Wars",          "r": 255, "g": 214, "b": 10},
    "geography_teacher": {"emoji": "🌍", "color": "#ff6b6b", "label": "Geography", "topics": "Countries · Climate · Ecosystems",       "r": 255, "g": 107, "b": 107},
    "cs_teacher":        {"emoji": "💻", "color": "#06d6a0", "label": "CS",        "topics": "Code · Algorithms · AI/ML · Web",        "r": 6,   "g": 214, "b": 160},
}

SAMPLES = [
    ("📚", "English",   "What is the difference between a metaphor and a simile?"),
    ("📐", "Maths",     "Solve: 2x² + 5x - 3 = 0 step by step"),
    ("🔬", "Science",   "Explain Newton's Third Law with real examples"),
    ("📜", "History",   "What were the main causes of World War 1?"),
    ("🌍", "Geography", "What is the capital of New Zealand and its climate?"),
    ("💻", "CS",        "Write a Python function for the nth Fibonacci number"),
]


# ─── Session state ────────────────────────────────────────────────────────────
for k, v in {
    "messages": [], "session_id": str(uuid.uuid4()),
    "user_id": f"student_{uuid.uuid4().hex[:8]}",
    "total_queries": 0, "agents_used": set(), "routing_log": [],
}.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─── ADK ─────────────────────────────────────────────────────────────────────
@st.cache_resource
def init_runner():
    try:
        from google.adk.runners import Runner
        from google.adk.sessions import InMemorySessionService
        from agents.agent import root_agent
        svc = InMemorySessionService()
        runner = Runner(agent=root_agent, app_name="school_agent_app", session_service=svc)
        return runner, svc, None
    except Exception as e:
        return None, None, str(e)


async def run_query(runner, svc, user_id, session_id, query):
    from google.genai.types import Content, Part
    try:
        session = await svc.get_session(app_name="school_agent_app", user_id=user_id, session_id=session_id)
        if session is None:
            raise Exception("no session")
    except Exception:
        try:
            await svc.create_session(app_name="school_agent_app", user_id=user_id, session_id=session_id)
        except Exception:
            pass

    message = Content(role="user", parts=[Part(text=query)])
    response_text = ""
    agent_used = "school_agent"
    routing_path = []

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=message):
        if hasattr(event, 'author') and event.author:
            if event.author not in routing_path:
                routing_path.append(event.author)
            agent_used = event.author
        if event.is_final_response():
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text:
                        response_text += part.text

    return response_text, agent_used, routing_path


def process_query(query, runner, svc):
    ts = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({"role": "user", "content": query, "time": ts})
    st.session_state.total_queries += 1
    with st.spinner("⚡ Routing to specialist teacher..."):
        try:
            start = time.time()
            response, agent_used, routing_path = asyncio.run(
                run_query(runner, svc, st.session_state.user_id, st.session_state.session_id, query)
            )
            elapsed = round(time.time() - start, 1)
            st.session_state.agents_used.add(agent_used)
            st.session_state.routing_log.append({
                "query": query[:55], "agent": agent_used,
                "path": routing_path, "time": ts, "elapsed": elapsed,
            })
            st.session_state.messages.append({
                "role": "assistant", "content": response, "agent": agent_used,
                "routing_path": routing_path, "elapsed": elapsed, "time": ts,
            })
        except Exception as e:
            st.session_state.messages.append({
                "role": "assistant", "content": f"⚠️ Error: {str(e)}",
                "agent": "school_agent", "routing_path": [], "elapsed": 0, "time": ts,
            })


runner, svc, init_error = init_runner()


# ═══════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════
with st.sidebar:

    # Branding
    st.markdown("""
    <div style="padding:24px 18px 18px; border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
            <div style="width:44px; height:44px; border-radius:14px; flex-shrink:0;
                background:linear-gradient(135deg,#7c3aed,#06d6a0);
                display:flex; align-items:center; justify-content:center; font-size:22px;
                box-shadow:0 4px 20px rgba(124,58,237,0.4);">🎓</div>
            <div>
                <div style="font-size:16px; font-weight:800; color:#f0eeff; letter-spacing:-0.3px;">School Agent</div>
                <div style="font-size:10px; color:#4a4875; font-weight:600; letter-spacing:1px; margin-top:2px;">GOOGLE ADK · A2A</div>
            </div>
        </div>
        <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <div style="padding:4px 10px; border-radius:99px; background:rgba(6,214,160,0.1);
                border:1px solid rgba(6,214,160,0.3); font-size:11px; color:#06d6a0; font-weight:700;">● LIVE</div>
            <div style="padding:4px 10px; border-radius:99px; background:rgba(168,85,247,0.1);
                border:1px solid rgba(168,85,247,0.25); font-size:11px; color:#a855f7; font-weight:500;">Gemini 2.5</div>
            <div style="padding:4px 10px; border-radius:99px; background:rgba(255,214,10,0.08);
                border:1px solid rgba(255,214,10,0.2); font-size:11px; color:#ffd60a; font-weight:500;">Memory ON</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    q = st.session_state.total_queries
    a = len(st.session_state.agents_used)
    st.markdown(f"""
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px; padding:14px 18px; border-bottom:1px solid rgba(255,255,255,0.07);">
        <div style="background:rgba(168,85,247,0.08); border:1px solid rgba(168,85,247,0.18); border-radius:10px; padding:10px 6px; text-align:center;">
            <div style="font-size:20px; font-weight:800; color:#a855f7;">{q}</div>
            <div style="font-size:10px; color:#4a4875; margin-top:1px;">Queries</div>
        </div>
        <div style="background:rgba(6,214,160,0.06); border:1px solid rgba(6,214,160,0.18); border-radius:10px; padding:10px 6px; text-align:center;">
            <div style="font-size:20px; font-weight:800; color:#06d6a0;">{a}</div>
            <div style="font-size:10px; color:#4a4875; margin-top:1px;">Agents</div>
        </div>
        <div style="background:rgba(255,214,10,0.06); border:1px solid rgba(255,214,10,0.18); border-radius:10px; padding:10px 6px; text-align:center;">
            <div style="font-size:20px; font-weight:800; color:#ffd60a;">6</div>
            <div style="font-size:10px; color:#4a4875; margin-top:1px;">Teachers</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Teachers list
    st.markdown("""
    <div style="padding:14px 18px 8px;">
        <div style="font-size:10px; font-weight:700; color:#4a4875; letter-spacing:1.2px;">SUBJECT TEACHERS</div>
    </div>
    """, unsafe_allow_html=True)

    for key, ag in AGENTS.items():
        active = key in st.session_state.agents_used
        r, g, b = ag['r'], ag['g'], ag['b']
        if active:
            border = f"border:1px solid rgba({r},{g},{b},0.4)"
            bg = f"background:rgba({r},{g},{b},0.08)"
            opacity = "opacity:1"
            used_badge = f'<span style="margin-left:auto; padding:2px 8px; border-radius:99px; background:rgba({r},{g},{b},0.15); font-size:10px; color:rgb({r},{g},{b}); font-weight:700; flex-shrink:0; white-space:nowrap;">✓ USED</span>'
        else:
            border = "border:1px solid rgba(255,255,255,0.05)"
            bg = "background:rgba(255,255,255,0.02)"
            opacity = "opacity:0.45"
            used_badge = '<span></span>'

        st.markdown(f"""
        <div style="margin:0 10px 6px; padding:10px 12px; border-radius:10px;
            {border}; {bg}; {opacity}; transition:all 0.2s;">
            <div style="display:flex; align-items:center; gap:10px;">
                <div style="width:34px; height:34px; border-radius:9px; flex-shrink:0;
                    background:rgba({r},{g},{b},0.12);
                    display:flex; align-items:center; justify-content:center; font-size:16px;">
                    {ag['emoji']}
                </div>
                <div style="flex:1; min-width:0;">
                    <div style="font-size:13px; font-weight:600; color:#f0eeff;">{ag['label']} Teacher</div>
                    <div style="font-size:11px; color:#4a4875; margin-top:1px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{ag['topics']}</div>
                </div>
                {used_badge}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Routing history
    if st.session_state.routing_log:
        st.markdown("""
        <div style="padding:14px 18px 8px; border-top:1px solid rgba(255,255,255,0.07); margin-top:6px;">
            <div style="font-size:10px; font-weight:700; color:#4a4875; letter-spacing:1.2px;">ROUTING HISTORY</div>
        </div>
        """, unsafe_allow_html=True)
        for log in reversed(st.session_state.routing_log[-4:]):
            ag_info = AGENTS.get(log['agent'], {"emoji": "🎓", "color": "#a855f7", "label": "School", "r": 168, "g": 85, "b": 247})
            r2, g2, b2 = ag_info['r'], ag_info['g'], ag_info['b']
            st.markdown(f"""
            <div style="margin:0 10px 5px; padding:8px 12px; border-radius:8px;
                background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05);">
                <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:3px;">
                    <div style="font-size:11px; color:rgb({r2},{g2},{b2}); font-weight:600;">
                        {ag_info['emoji']} {ag_info['label']}
                    </div>
                    <div style="font-size:10px; color:#4a4875;">⚡{log['elapsed']}s · {log['time']}</div>
                </div>
                <div style="font-size:11px; color:#9892c8; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
                    {log['query']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Capabilities
    st.markdown("""
    <div style="padding:14px 18px 8px; border-top:1px solid rgba(255,255,255,0.07); margin-top:6px;">
        <div style="font-size:10px; font-weight:700; color:#4a4875; letter-spacing:1.2px; margin-bottom:10px;">CAPABILITIES</div>
        <div style="display:flex; flex-direction:column; gap:7px;">
            <div style="font-size:12px; color:#9892c8; display:flex; align-items:center; gap:8px;"><span style="color:#06d6a0;">✦</span> A2A Multi-Agent Routing</div>
            <div style="font-size:12px; color:#9892c8; display:flex; align-items:center; gap:8px;"><span style="color:#06d6a0;">✦</span> Conversation Memory</div>
            <div style="font-size:12px; color:#9892c8; display:flex; align-items:center; gap:8px;"><span style="color:#06d6a0;">✦</span> Calculator Tool (Maths)</div>
            <div style="font-size:12px; color:#9892c8; display:flex; align-items:center; gap:8px;"><span style="color:#06d6a0;">✦</span> Real-time Routing Log</div>
            <div style="font-size:12px; color:#9892c8; display:flex; align-items:center; gap:8px;"><span style="color:#06d6a0;">✦</span> Response Time Tracking</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # GDG badge
    st.markdown("""
    <div style="margin:12px 10px; padding:12px; border-radius:12px;
        background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(6,214,160,0.06));
        border:1px solid rgba(124,58,237,0.2); text-align:center;">
        <div style="font-size:14px;">🇬🇧</div>
        <div style="font-size:11px; color:#a855f7; font-weight:700; letter-spacing:0.5px; margin-top:4px;">GDG LONDON</div>
        <div style="font-size:10px; color:#4a4875; margin-top:2px;">Google ADK Assignment 2025</div>
    </div>
    """, unsafe_allow_html=True)

    # Clear button
    st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
    if st.button("🗑️ Clear conversation", use_container_width=True, key="clear_btn"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.total_queries = 0
        st.session_state.agents_used = set()
        st.session_state.routing_log = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════

# Header
st.markdown("""
<div style="padding:28px 36px 22px; border-bottom:1px solid rgba(255,255,255,0.07);
    background:linear-gradient(135deg,rgba(124,58,237,0.04) 0%,rgba(6,214,160,0.02) 100%);">
    <div style="display:flex; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; gap:12px;">
        <div>
            <h1 style="font-size:27px; font-weight:800; color:#f0eeff; letter-spacing:-0.5px; margin:0; line-height:1.2;">
                🏫 School Multi-Agent System
            </h1>
            <p style="font-size:13px; color:#9892c8; margin-top:7px; line-height:1.5; max-width:520px;">
                Built on <strong style="color:#a855f7;">Google ADK</strong> with A2A protocol —
                every question is intelligently routed to the right specialist teacher in real-time.
            </p>
        </div>
        <div style="display:flex; gap:8px; flex-wrap:wrap; align-items:center;">
            <div style="padding:5px 12px; border-radius:99px; background:rgba(6,214,160,0.1);
                border:1px solid rgba(6,214,160,0.3); font-size:11px; color:#06d6a0; font-weight:700;">● LIVE</div>
            <div style="padding:5px 12px; border-radius:99px; background:rgba(168,85,247,0.08);
                border:1px solid rgba(168,85,247,0.2); font-size:11px; color:#a855f7; font-weight:500;">6 Agents Active</div>
            <div style="padding:5px 12px; border-radius:99px; background:rgba(255,214,10,0.06);
                border:1px solid rgba(255,214,10,0.2); font-size:11px; color:#ffd60a; font-weight:500;">Memory ON</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Error
if init_error:
    st.markdown(f"""
    <div style="margin:20px 36px; padding:14px 18px; border-radius:10px;
        background:rgba(255,107,107,0.06); border:1px solid rgba(255,107,107,0.2);
        color:#ff6b6b; font-size:13px;">
        ⚠️ <strong>Error:</strong> {init_error}
    </div>
    """, unsafe_allow_html=True)

# Sample queries
if not st.session_state.messages and runner:
    st.markdown("""
    <div style="padding:28px 36px 12px;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
            <div style="width:3px; height:16px; border-radius:99px; background:linear-gradient(180deg,#7c3aed,#06d6a0);"></div>
            <div style="font-size:11px; font-weight:700; color:#4a4875; letter-spacing:1.2px;">TRY THESE — one for each teacher</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    for i, (emoji, subject, query) in enumerate(SAMPLES):
        with cols[i % 3]:
            if st.button(f"{emoji} {subject}\n{query}", key=f"s_{i}", use_container_width=True):
                process_query(query, runner, svc)
                st.rerun()

    st.markdown("""
    <div style="margin:16px 36px; padding:14px 18px; border-radius:12px;
        background:rgba(168,85,247,0.05); border:1px solid rgba(168,85,247,0.15);">
        <div style="font-size:12px; color:#9892c8; line-height:1.6;">
            🧠 <strong style="color:#f0eeff;">Memory demo:</strong>
            Ask a Maths question, then follow up with
            <em style="color:#a855f7;">"Now calculate the area of a circle with the same radius"</em>
            — the agent remembers!
        </div>
    </div>
    """, unsafe_allow_html=True)

# Chat messages
st.markdown('<div style="padding:20px 36px 8px;">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        ts = msg.get("time", "")
        content = msg['content'].replace('<', '&lt;').replace('>', '&gt;')
        st.markdown(f"""
        <div style="display:flex; justify-content:flex-end; margin-bottom:20px; align-items:flex-end; gap:10px;">
            <div style="font-size:10px; color:#4a4875; padding-bottom:2px;">{ts}</div>
            <div style="max-width:65%;">
                <div style="padding:13px 17px; border-radius:16px 16px 3px 16px;
                    background:linear-gradient(135deg,#7c3aed,#a855f7);
                    color:white; font-size:14px; line-height:1.6;
                    box-shadow:0 4px 24px rgba(124,58,237,0.3);">
                    {content}
                </div>
            </div>
            <div style="width:32px; height:32px; border-radius:99px; flex-shrink:0;
                background:linear-gradient(135deg,#7c3aed,#06d6a0);
                display:flex; align-items:center; justify-content:center; font-size:14px;">👤</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        agent_key = msg.get("agent", "school_agent")
        ag = AGENTS.get(agent_key, {"emoji": "🎓", "color": "#a855f7", "label": "School Agent", "r": 168, "g": 85, "b": 247})
        r, g, b = ag['r'], ag['g'], ag['b']
        ts = msg.get("time", "")
        elapsed = msg.get("elapsed", 0)
        routing_path = msg.get("routing_path", [])
        path_str = " → ".join(routing_path) if routing_path else agent_key
        content = msg['content'].replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')

        st.markdown(f"""
        <div style="margin-bottom:8px; padding-left:44px; display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
            <div style="font-size:10px; color:rgb({r},{g},{b}); font-weight:700; letter-spacing:0.5px;">
                {ag['emoji']} {ag['label'].upper()} TEACHER
            </div>
            <div style="font-size:10px; color:#4a4875;">·</div>
            <div style="font-size:10px; color:#4a4875; font-family:'Fira Code',monospace;">⚡ {elapsed}s</div>
            <div style="font-size:10px; color:#4a4875;">·</div>
            <div style="font-size:10px; color:#4a4875;">{ts}</div>
        </div>
        <div style="display:flex; gap:12px; margin-bottom:20px; align-items:flex-start;">
            <div style="width:34px; height:34px; border-radius:10px; flex-shrink:0; margin-top:2px;
                background:rgba({r},{g},{b},0.1); border:1px solid rgba({r},{g},{b},0.25);
                display:flex; align-items:center; justify-content:center; font-size:16px;">
                {ag['emoji']}
            </div>
            <div style="flex:1; max-width:82%;">
                <div style="padding:16px 18px; border-radius:3px 16px 16px 16px;
                    background:#1e1d35; border:1px solid rgba(255,255,255,0.07);
                    font-size:14px; line-height:1.75; color:#dddcf5;">
                    {content}
                </div>
                <div style="margin-top:6px; padding:5px 12px; border-radius:6px; display:inline-block;
                    background:rgba({r},{g},{b},0.05); border:1px solid rgba({r},{g},{b},0.12);
                    font-size:11px; color:rgba({r},{g},{b},0.75); font-family:'Fira Code',monospace;">
                    route: {path_str}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Ask anything — English, Maths, Science, History, Geography, CS..."):
    if runner:
        process_query(prompt, runner, svc)
        st.rerun()
    else:
        st.error("⚠️ Agent not initialised. Check your API key.")
