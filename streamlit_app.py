"""
School Agent — Clean Professional UI v4
GDG London | Google ADK A2A Architecture
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg:      #09090b;
    --bg2:     #0f0f12;
    --bg3:     #18181b;
    --bg4:     #27272a;
    --border:  rgba(255,255,255,0.06);
    --border2: rgba(255,255,255,0.1);
    --purple:  #8b5cf6;
    --green:   #10b981;
    --amber:   #f59e0b;
    --blue:    #3b82f6;
    --red:     #ef4444;
    --text:    #fafafa;
    --text2:   #a1a1aa;
    --text3:   #52525b;
    --r:       12px;
    --r2:      8px;
}

.stApp {
    background: var(--bg) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text) !important;
}

#MainMenu, footer, header, .stDeployButton { display:none !important; }
.block-container { padding:0 0 0 0 !important; max-width:100% !important; display: flex !important; flex-direction: column !important; min-height: 100vh !important; }
.main .block-container { padding-bottom:0 !important; }
section[data-testid="stMain"] { padding-bottom:0 !important; }
section[data-testid="stMain"] > div { padding-bottom:0 !important; display: flex !important; flex-direction: column !important; min-height: 100vh !important; }
div[data-testid="stVerticalBlock"] { gap:0 !important; display: flex !important; flex-direction: column !important; flex-grow: 1 !important; height: 100% !important; }
div[data-testid="stVerticalBlock"] > div { padding-bottom:0 !important; }
.element-container { margin-bottom:0 !important; }
div.element-container:has(#bottom-panel-anchor) { margin-top: auto !important; width: 100%; }
iframe { display:block; }

[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child { padding:0 !important; }

::-webkit-scrollbar { width:3px; }
::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:var(--bg4); border-radius:99px; }

/* Buttons */
.stButton > button {
    background: var(--bg3) !important;
    color: var(--text2) !important;
    border: 1px solid var(--border2) !important;
    border-radius: var(--r2) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 400 !important;
    padding: 10px 14px !important;
    width: 100% !important;
    text-align: left !important;
    transition: all 0.15s ease !important;
    line-height: 1.5 !important;
    white-space: normal !important;
    height: auto !important;
    min-height: 52px !important;
}
.stButton > button:hover {
    background: var(--bg4) !important;
    border-color: var(--purple) !important;
    color: var(--text) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(139,92,246,0.15) !important;
}

.clear-btn .stButton > button {
    background: transparent !important;
    border-color: rgba(239,68,68,0.2) !important;
    color: rgba(239,68,68,0.5) !important;
    text-align: center !important;
    font-size: 12px !important;
    min-height: 34px !important;
    padding: 6px 12px !important;
}
.clear-btn .stButton > button:hover {
    background: rgba(239,68,68,0.06) !important;
    border-color: var(--red) !important;
    color: var(--red) !important;
    box-shadow: none !important;
    transform: none !important;
}

/* Chat input */
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
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    padding: 14px 18px !important;
    transition: all 0.2s ease !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: var(--purple) !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important;
    outline: none !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: var(--text3) !important;
    font-style: italic !important;
    font-size: 13px !important;
}
[data-testid="stChatInput"] button {
    background: var(--purple) !important;
    border: none !important;
    border-radius: var(--r2) !important;
    color: white !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(139,92,246,0.3) !important;
}
[data-testid="stChatInput"] button:hover {
    background: #7c3aed !important;
    transform: scale(1.05) !important;
}
[data-testid="stChatInput"] button svg { fill:white !important; stroke:white !important; }

.stSpinner > div { border-top-color: var(--purple) !important; }

.stTextInput { margin:0 !important; padding:0 36px !important; }
.stTextInput input {
    background: #18181b !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: #fafafa !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    padding: 14px 18px !important;
    height: 52px !important;
}
.stTextInput input:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important;
}
.stTextInput input::placeholder { color: #52525b !important; font-style:italic !important; }
div[data-testid="column"]:last-child .stButton button {
    background: #8b5cf6 !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    height: 52px !important;
    font-size: 18px !important;
    min-height: 52px !important;
    box-shadow: 0 2px 8px rgba(139,92,246,0.3) !important;
}
div[data-testid="column"]:last-child .stButton button:hover {
    background: #7c3aed !important;
    transform: scale(1.05) !important;
}
</style>
""", unsafe_allow_html=True)

# Rotating placeholder
st.components.v1.html("""
<script>
const ph = [
    "Ask anything — the right teacher will respond instantly...",
    "💬 Try: What is the difference between a metaphor and a simile?",
    "📐 Try: Solve 2x² + 5x - 3 = 0 step by step",
    "🔬 Try: Explain Newton's Third Law with real examples",
    "📜 Try: What caused World War 1?",
    "🌍 Try: Capital of New Zealand and its climate?",
    "💻 Try: Write a Python Fibonacci function",
    "🧠 Memory is ON — ask follow-up questions freely"
];
let i = 0;
function go() {
    const els = window.parent.document.querySelectorAll('[data-testid="stChatInput"] textarea');
    els.forEach(el => { if (!el.value) el.setAttribute('placeholder', ph[i % ph.length]); });
    i++;
}
go(); setInterval(go, 4000);
</script>
""", height=0)

# ── Agent config ──────────────────────────────────────────────────────────────
AGENTS = {
    "english_teacher":   {"emoji": "📚", "label": "English",   "topics": "Grammar · Essays · Literature · Poetry", "r": 59,  "g": 130, "b": 246, "hex": "#3b82f6"},
    "maths_teacher":     {"emoji": "📐", "label": "Maths",     "topics": "Algebra · Calculus · Geometry · Stats",  "r": 139, "g": 92,  "b": 246, "hex": "#8b5cf6"},
    "science_teacher":   {"emoji": "🔬", "label": "Science",   "topics": "Physics · Chemistry · Biology",          "r": 16,  "g": 185, "b": 129, "hex": "#10b981"},
    "history_teacher":   {"emoji": "📜", "label": "History",   "topics": "Events · Civilisations · Wars",          "r": 245, "g": 158, "b": 11,  "hex": "#f59e0b"},
    "geography_teacher": {"emoji": "🌍", "label": "Geography", "topics": "Countries · Climate · Ecosystems",       "r": 20,  "g": 184, "b": 166, "hex": "#14b8a6"},
    "cs_teacher":        {"emoji": "💻", "label": "CS",        "topics": "Code · Algorithms · AI/ML · Web",        "r": 239, "g": 68,  "b": 68,  "hex": "#ef4444"},
}

SAMPLES = [
    ("📚", "English",   "What is the difference between a metaphor and a simile?"),
    ("📐", "Maths",     "Solve: 2x² + 5x - 3 = 0 step by step"),
    ("🔬", "Science",   "Explain Newton's Third Law with real examples"),
    ("📜", "History",   "What were the main causes of World War 1?"),
    ("🌍", "Geography", "What is the capital of New Zealand and its climate?"),
    ("💻", "CS",        "Write a Python function for the nth Fibonacci number"),
]

# ── Session state ─────────────────────────────────────────────────────────────
for k, v in {
    "messages": [], "session_id": str(uuid.uuid4()),
    "user_id": f"student_{uuid.uuid4().hex[:8]}",
    "total_queries": 0, "agents_used": set(), "routing_log": [],
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── ADK ───────────────────────────────────────────────────────────────────────
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
        if session is None: raise Exception("no session")
    except Exception:
        try: await svc.create_session(app_name="school_agent_app", user_id=user_id, session_id=session_id)
        except Exception: pass

    message = Content(role="user", parts=[Part(text=query)])
    response_text, agent_used, routing_path = "", "school_agent", []

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=message):
        if hasattr(event, 'author') and event.author:
            if event.author not in routing_path: routing_path.append(event.author)
            agent_used = event.author
        if event.is_final_response():
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text: response_text += part.text

    return response_text, agent_used, routing_path

def process_query(query, runner, svc):
    ts = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({"role": "user", "content": query, "time": ts})
    st.session_state.total_queries += 1
    with st.spinner("Routing to specialist teacher..."):
        try:
            start = time.time()
            response, agent_used, routing_path = asyncio.run(
                run_query(runner, svc, st.session_state.user_id, st.session_state.session_id, query)
            )
            elapsed = round(time.time() - start, 1)
            st.session_state.agents_used.add(agent_used)
            st.session_state.routing_log.append({"query": query[:55], "agent": agent_used, "time": ts, "elapsed": elapsed})
            st.session_state.messages.append({"role": "assistant", "content": response, "agent": agent_used, "routing_path": routing_path, "elapsed": elapsed, "time": ts})
        except Exception as e:
            st.session_state.messages.append({"role": "assistant", "content": f"⚠️ Error: {str(e)}", "agent": "school_agent", "routing_path": [], "elapsed": 0, "time": ts})
            st.session_state["chat_input"] = ""

runner, svc, init_error = init_runner()

# ═══════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════
with st.sidebar:

    html_top = f"""<div style="padding:24px 20px 16px; display:flex; flex-direction:column; gap:24px;">
<div style="display:flex; align-items:center; gap:16px;">
<div style="width:42px; height:42px; border-radius:10px; background:linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.03)); border:1px solid rgba(255,255,255,0.1); display:flex; align-items:center; justify-content:center; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>
</div>
<div>
<div style="font-size:18px; font-weight:600; color:#ffffff; letter-spacing:-0.5px;">School Agent</div>
<div style="font-size:12px; color:#a1a1aa;">Google ADK Backbone</div>
</div>
</div>
<div style="display:flex; gap:8px;">
<div style="padding:4px 12px; border-radius:12px; background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.2); font-size:11px; color:#10b981; font-weight:500; display:flex; align-items:center; gap:6px;">
<div style="width:6px; height:6px; border-radius:50%; background:#10b981; box-shadow: 0 0 6px rgba(16,185,129,0.5);"></div> Live
</div>
<div style="padding:4px 12px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06); font-size:11px; color:#a1a1aa; font-weight:500;">Gemini 2.5</div>
<div style="padding:4px 12px; border-radius:12px; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.06); font-size:11px; color:#a1a1aa; font-weight:500;">Memory</div>
</div>
<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; border-bottom:1px solid rgba(255,255,255,0.06); padding-bottom:24px;">
<div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:10px; padding:12px 0; text-align:center;">
<div style="font-size:18px; font-weight:600; color:#ffffff;">{st.session_state.total_queries}</div>
<div style="font-size:11px; color:#a1a1aa; margin-top:2px;">Queries</div>
</div>
<div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:10px; padding:12px 0; text-align:center;">
<div style="font-size:18px; font-weight:600; color:#ffffff;">{len(st.session_state.agents_used)}</div>
<div style="font-size:11px; color:#a1a1aa; margin-top:2px;">Agents</div>
</div>
<div style="background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:10px; padding:12px 0; text-align:center;">
<div style="font-size:18px; font-weight:600; color:#ffffff;">6</div>
<div style="font-size:11px; color:#a1a1aa; margin-top:2px;">Teachers</div>
</div>
</div>
<div style="font-size:11px; font-weight:600; color:#71717a; letter-spacing:0.5px; padding-top:8px;">ORCHESTRATION</div>
</div>"""
    st.markdown(html_top, unsafe_allow_html=True)

    for key, ag in AGENTS.items():
        active = key in st.session_state.agents_used
        if active:
            bg = "rgba(255,255,255,0.05)"
            border = "rgba(255,255,255,0.15)"
            opacity = "1"
            title_color = "#ffffff"
            desc_color = "#a1a1aa"
            indicator = '<div style="width:6px; height:6px; border-radius:50%; background:#ffffff; box-shadow:0 0 6px #ffffff;"></div>'
        else:
            bg = "transparent"
            border = "transparent"
            opacity = "0.5"
            title_color = "#d4d4d8"
            desc_color = "#71717a"
            indicator = ''

        agent_html = f"""<div style="margin:4px 20px; padding:10px 14px; border-radius:10px; background:{bg}; border:1px solid {border}; opacity:{opacity}; display:flex; align-items:center; gap:14px; transition:all 0.2s;">
<div style="font-size:18px; background:rgba(255,255,255,0.05); width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center;">{ag['emoji']}</div>
<div style="flex:1; min-width:0;">
<div style="font-size:13px; font-weight:500; color:{title_color}; display:flex; align-items:center; justify-content:space-between;"><span>{ag['label']}</span>{indicator}</div>
<div style="font-size:11px; color:{desc_color}; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{ag['topics']}</div>
</div>
</div>"""
        st.markdown(agent_html, unsafe_allow_html=True)

    if st.session_state.routing_log:
        st.markdown("""<div style="padding:24px 20px 12px;"><div style="font-size:11px; font-weight:600; color:#71717a; letter-spacing:0.5px;">RECENT ACTIVITY</div></div>""", unsafe_allow_html=True)
        for log in reversed(st.session_state.routing_log[-3:]):
            ag_info = AGENTS.get(log['agent'], {"emoji": "🎓", "label": "School", "r": 139, "g": 92, "b": 246})
            r2, g2, b2 = ag_info['r'], ag_info['g'], ag_info['b']
            
            log_html = f"""<div style="padding:0 20px; margin-bottom:16px; display:flex; gap:12px; align-items:start;">
<div style="width:2px; height:32px; background:rgb({r2},{g2},{b2}); border-radius:2px; opacity:0.8;"></div>
<div style="flex:1; min-width:0; padding-top:2px;">
<div style="display:flex; justify-content:space-between; align-items:center;">
<span style="font-size:13px; color:#ffffff; font-weight:500;">{ag_info['label']}</span>
<span style="font-size:10px; color:#71717a; font-family:monospace;">{log['elapsed']}s</span>
</div>
<div style="font-size:12px; color:#a1a1aa; margin-top:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{log['query']}</div>
</div>
</div>"""
            st.markdown(log_html, unsafe_allow_html=True)

    features_html = """<div style="padding:24px 20px 16px;">
<div style="font-size:11px; font-weight:600; color:#71717a; letter-spacing:0.5px; margin-bottom:12px;">CAPABILITIES</div>
<div style="display:flex; flex-direction:column; gap:12px;">
<div style="font-size:12px; color:#a1a1aa; display:flex; align-items:center; gap:10px;">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#71717a" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg> Multi-Agent Routing
</div>
<div style="font-size:12px; color:#a1a1aa; display:flex; align-items:center; gap:10px;">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#71717a" stroke-width="2"><path d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg> Memory Context
</div>
<div style="font-size:12px; color:#a1a1aa; display:flex; align-items:center; gap:10px;">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#71717a" stroke-width="2"><path d="M12 20V10M18 20V4M6 20v-4"/></svg> Real-time Telemetry
</div>
</div>
</div>
<div style="padding:0 20px 16px;">
<div style="padding:12px 14px; border-radius:10px; border:1px solid rgba(255,255,255,0.06); display:flex; align-items:center; gap:12px; background:rgba(255,255,255,0.02);">
<div style="font-size:18px;">🇬🇧</div>
<div>
<div style="font-size:12px; font-weight:600; color:#e4e4e7;">GDG London</div>
<div style="font-size:11px; color:#71717a; margin-top:2px;">Google ADK Assignment '26</div>
</div>
</div>
</div>"""
    st.markdown(features_html, unsafe_allow_html=True)

    st.markdown('<div style="padding:0 20px 20px;">', unsafe_allow_html=True)
    if st.button("🗑️ Clear Conversation", use_container_width=True, key="clear_btn"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.total_queries = 0
        st.session_state.agents_used = set()
        st.session_state.routing_log = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════
# MAIN
# ═══════════════════════════════════════

# Header
st.markdown("""
<div style="padding:24px 36px 20px; border-bottom:1px solid rgba(255,255,255,0.06);">
    <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
        <div>
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
                <span style="font-size:22px;">🏫</span>
                <h1 style="font-size:22px; font-weight:600; color:#fafafa; letter-spacing:-0.3px; margin:0;">School Multi-Agent System</h1>
            </div>
            <p style="font-size:13px; color:#71717a; margin:0; line-height:1.5;">
                Google ADK · A2A Protocol · Every question routed to the right specialist teacher instantly
            </p>
        </div>
        <div style="display:flex; gap:6px; align-items:center; flex-wrap:wrap;">
            <span style="padding:4px 10px; border-radius:99px; background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.2); font-size:11px; color:#10b981; font-weight:600;">● Live</span>
            <span style="padding:4px 10px; border-radius:99px; background:rgba(139,92,246,0.08); border:1px solid rgba(139,92,246,0.18); font-size:11px; color:#8b5cf6;">6 Agents</span>
            <span style="padding:4px 10px; border-radius:99px; background:rgba(245,158,11,0.06); border:1px solid rgba(245,158,11,0.18); font-size:11px; color:#f59e0b;">Memory On</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

if init_error:
    st.markdown(f'<div style="margin:16px 36px; padding:12px 16px; border-radius:8px; background:rgba(239,68,68,0.06); border:1px solid rgba(239,68,68,0.2); color:#ef4444; font-size:13px;">⚠️ {init_error}</div>', unsafe_allow_html=True)

# Sample queries
if not st.session_state.messages and runner:
    st.markdown("""
<style>
[data-testid="stMainBlockContainer"] button[kind="primary"] {
    text-align: left !important;
    background: linear-gradient(145deg, rgba(255,255,255,0.02), rgba(0,0,0,0.1)) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 12px !important;
    padding: 16px 20px !important;
    width: 100% !important;
    height: auto !important;
    min-height: 125px !important;
    display: flex !important;
    align-items: flex-start !important;
    justify-content: flex-start !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
[data-testid="stMainBlockContainer"] button[kind="primary"]:hover {
    background: rgba(255,255,255,0.04) !important;
    border-color: rgba(255,255,255,0.15) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25) !important;
}
[data-testid="stMainBlockContainer"] button[kind="primary"] p {
    font-family: inherit !important;
    text-align: left !important;
    white-space: pre-wrap !important;
    line-height: 1.6 !important;
    margin: 0 !important;
    font-size: 13px !important;
    color: #a1a1aa !important;
}
[data-testid="stMainBlockContainer"] button[kind="primary"] p::first-line {
    color: #fafafa !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}
</style>
""", unsafe_allow_html=True)

    st.markdown('<div style="padding:24px 36px 12px;"><div style="font-size:11px; font-weight:600; color:#71717a; letter-spacing:0.8px; margin-bottom:12px;">TRY ASKING</div></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    cols = [c1, c2, c3]
    for i, (emoji, subject, query) in enumerate(SAMPLES):
        with cols[i % 3]:
            # Use type=primary to trigger the CSS override!
            if st.button(f"{emoji} {subject.upper()}\n\n{query}", key=f"s_{i}", use_container_width=True, type="primary"):
                process_query(query, runner, svc)
                st.rerun()

    st.markdown("""
<div style="margin:24px 36px 0; display:flex; justify-content:center;">
    <div style="padding:10px 24px; border-radius:99px; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.06); display:flex; align-items:center; gap:12px;">
        <div style="font-size:14px; background:rgba(255,255,255,0.05); border-radius:6px; padding:2px 6px;">💡</div>
        <div style="font-size:12px; color:#a1a1aa; font-weight:400; letter-spacing:0.3px;">
            <span style="color:#d4d4d8; font-weight:500;">Memory test:</span> Ask Maths a question, then follow up with <span style="background:rgba(255,255,255,0.05); padding:3px 8px; border-radius:6px; color:#e4e4e7; margin:0 4px;">"now calculate the area using the same radius"</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Chat messages
st.markdown('<div style="padding:20px 36px 4px;">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        ts = msg.get("time", "")
        content = msg['content'].replace('<', '&lt;').replace('>', '&gt;')
        st.markdown(f"""
        <div style="display:flex; justify-content:flex-end; margin-bottom:18px; align-items:flex-end; gap:8px;">
            <div style="font-size:10px; color:#3f3f46; padding-bottom:2px;">{ts}</div>
            <div style="max-width:62%;">
                <div style="padding:11px 15px; border-radius:14px 14px 3px 14px;
                    background:#8b5cf6; color:white; font-size:14px; line-height:1.6;
                    box-shadow:0 2px 12px rgba(139,92,246,0.25);">
                    {content}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        agent_key = msg.get("agent", "school_agent")
        ag = AGENTS.get(agent_key, {"emoji": "🎓", "label": "School Agent", "r": 139, "g": 92, "b": 246, "hex": "#8b5cf6"})
        r, g, b = ag['r'], ag['g'], ag['b']
        elapsed = msg.get("elapsed", 0)
        routing_path = msg.get("routing_path", [])
        path_str = " → ".join(routing_path) if routing_path else agent_key
        ts = msg.get("time", "")
        content = msg['content'].replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')

        st.markdown(f"""
        <div style="display:flex; gap:10px; margin-bottom:18px; align-items:flex-start;">
            <div style="width:30px; height:30px; border-radius:8px; flex-shrink:0; margin-top:18px;
                background:rgba({r},{g},{b},0.1); border:1px solid rgba({r},{g},{b},0.2);
                display:flex; align-items:center; justify-content:center; font-size:14px;">
                {ag['emoji']}
            </div>
            <div style="flex:1; max-width:80%;">
                <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px; flex-wrap:wrap;">
                    <span style="font-size:11px; color:rgb({r},{g},{b}); font-weight:600; letter-spacing:0.3px;">{ag['label'].upper()} TEACHER</span>
                    <span style="font-size:10px; color:#3f3f46;">·</span>
                    <span style="font-size:10px; color:#3f3f46; font-family:'JetBrains Mono',monospace;">{elapsed}s</span>
                    <span style="font-size:10px; color:#3f3f46;">·</span>
                    <span style="font-size:10px; color:#3f3f46;">{ts}</span>
                </div>
                <div style="padding:14px 16px; border-radius:3px 12px 12px 12px;
                    background:#18181b; border:1px solid rgba(255,255,255,0.06);
                    font-size:14px; line-height:1.75; color:#d4d4d8;">
                    {content}
                </div>
                <div style="margin-top:5px; display:inline-block; padding:3px 10px; border-radius:5px;
                    background:rgba({r},{g},{b},0.04); border:1px solid rgba({r},{g},{b},0.1);
                    font-size:10px; color:rgba({r},{g},{b},0.6); font-family:'JetBrains Mono',monospace;">
                    {path_str}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Anchor to push following elements to the bottom using margin-top: auto
st.markdown('<div id="bottom-panel-anchor"></div>', unsafe_allow_html=True)

# Chat input
col1, col2 = st.columns([11, 1])
with col1:
    prompt = st.text_input("", placeholder="Ask anything — the right teacher will respond instantly...", label_visibility="collapsed", key="chat_input")
with col2:
    send = st.button("➤", use_container_width=True)

if prompt and runner and st.session_state.get("last_query") != prompt:
    st.session_state["last_query"] = prompt
    process_query(prompt, runner, svc)
    st.rerun()

# Footer
st.markdown("""
<table style="width:100%; border-collapse:collapse; border-top:1px solid rgba(255,255,255,0.06); margin-top:8px;">
<tr>
<td style="padding:14px 36px; vertical-align:middle; width:35%;">
    <span style="display:inline-flex; align-items:center; gap:10px;">
        <span style="width:32px; height:32px; border-radius:8px; background:linear-gradient(135deg,#8b5cf6,#10b981); display:inline-flex; align-items:center; justify-content:center; font-size:15px;">👨‍💻</span>
        <span>
            <span style="display:block; font-size:13px; font-weight:600; color:#fafafa;">Meet Bhorania</span>
            <span style="display:block; font-size:11px; color:#71717a; margin-top:2px;">AI Engineer &amp; Builder · GDG London Speaker · Hackathon Winner</span>
        </span>
    </span>
</td>
<td style="padding:14px 20px; vertical-align:middle; text-align:center; width:40%;">
    <span style="font-size:11px; color:#52525b;">Built with &nbsp;</span>
    <span style="padding:3px 9px; border-radius:99px; background:rgba(139,92,246,0.08); border:1px solid rgba(139,92,246,0.18); font-size:11px; color:#8b5cf6;">Google ADK</span>
    &nbsp;
    <span style="padding:3px 9px; border-radius:99px; background:rgba(16,185,129,0.06); border:1px solid rgba(16,185,129,0.16); font-size:11px; color:#10b981;">Gemini 2.5 Flash</span>
    &nbsp;
    <span style="padding:3px 9px; border-radius:99px; background:rgba(59,130,246,0.06); border:1px solid rgba(59,130,246,0.16); font-size:11px; color:#3b82f6;">A2A Protocol</span>
</td>
<td style="padding:14px 36px; vertical-align:middle; text-align:right; width:25%; white-space:nowrap;">
    <a href="https://github.com/meetbhorania/school-agent" target="_blank" style="padding:5px 12px; border-radius:7px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); color:#a1a1aa; font-size:12px; font-weight:500; text-decoration:none; margin-right:6px;">GitHub ↗</a>
    <a href="https://linkedin.com/in/meetbhorania" target="_blank" style="padding:5px 12px; border-radius:7px; background:rgba(59,130,246,0.08); border:1px solid rgba(59,130,246,0.2); color:#3b82f6; font-size:12px; font-weight:500; text-decoration:none; margin-right:8px;">LinkedIn ↗</a>
    <span style="font-size:11px; color:#3f3f46;">GDG London · Apr 2026</span>
</td>
</tr>
</table>
""", unsafe_allow_html=True)