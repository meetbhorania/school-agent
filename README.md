# 🏫 School Multi-Agent System (A2A) using Google ADK

> **GDG London Assignment** — Built by Meet Bhorania  
> A production-grade multi-agent AI school system using Google Agent Development Kit (ADK) with Agent-to-Agent (A2A) communication protocol.

[![Google ADK](https://img.shields.io/badge/Google%20ADK-Python-blue?logo=google)](https://google.github.io/adk-docs/)
[![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-orange?logo=google)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

---

## 🏗️ Architecture Overview

```
Student Query
     │
     ▼
┌─────────────────────────────────────────┐
│       ROOT AGENT (School Agent)         │
│  ┌─────────────────────────────────┐    │
│  │     Orchestration Layer         │    │
│  │  Intent Recognition + Routing   │    │
│  └──────────────┬──────────────────┘    │
│                 │ A2A Communication     │
└─────────────────┼───────────────────────┘
                  │
    ┌─────────────┼──────────────┐
    │             │              │
    ▼             ▼              ▼
English       Maths          Science
Teacher       Teacher        Teacher
              (+ calc)
    ▼             ▼              ▼
History      Geography       CS Teacher
Teacher       Teacher        (+ search)
```

---

## ✅ Features Implemented

| Feature | Status | Details |
|---|---|---|
| Root Orchestrator Agent | ✅ | School Agent — routes all queries |
| English Teacher Agent | ✅ | Grammar, Essays, Literature, Poetry |
| Maths Teacher Agent | ✅ | Algebra, Calculus, Geometry, Stats |
| Science Teacher Agent | ✅ | Physics, Chemistry, Biology |
| History Teacher Agent | ✅ | World History, Civilizations, Wars |
| 🔥 Geography Agent (L1) | ✅ | Physical/Human Geo, Countries, Climate |
| 🔥 CS Agent (L1) | ✅ | Programming, Algorithms, AI/ML |
| 🚀 Memory / Context (L2) | ✅ | `InMemorySessionService` — full conversation history |
| 🚀 Calculator Tool (L2) | ✅ | Safe expression evaluator in Maths Agent |
| 🚀 Google Search Tool (L2) | ✅ | Live search in CS Agent + Root fallback |
| A2A Protocol | ✅ | Google ADK native sub-agent delegation |
| ADK Web UI Demo | ✅ | `adk web` — one command launch |

---

## 📁 Project Structure

```
school-agent/
├── root_agent.py          # Root orchestrator (School Agent)
├── main.py                # CLI entry point + session/memory setup
├── streamlit_app.py       # Premium Streamlit UI
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── .gitignore
├── README.md
└── agents/
    ├── __init__.py
    ├── agent.py           # ADK entry point (exposes root_agent)
    ├── english_agent.py   # English Teacher
    ├── maths_agent.py     # Maths Teacher + Calculator Tool
    ├── science_agent.py   # Science Teacher
    ├── history_agent.py   # History Teacher
    ├── geography_agent.py # 🔥 Geography Teacher (Level 1)
    └── cs_agent.py        # 🔥 CS Teacher (Level 1)
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/school-agent.git
cd school-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

Get your free API key at: https://aistudio.google.com/apikey

### 5. Run

#### 🌐 Option A — Live Demo (Streamlit Cloud) ⭐ Recommended
Access the live deployed app instantly — no setup required:

> **[https://meetbhorania-school-agent.streamlit.app](https://school-agent-eqcbb2kpgdghyvzg2s3ec4.streamlit.app/)**

#### 🖥️ Option B — Streamlit UI (Local)
```bash
streamlit run streamlit_app.py
```
Then open: **http://localhost:8501**

#### 🤖 Option C — ADK Web UI (Local)
```bash
adk web --port 8080
```
Then open: **http://localhost:8080**  
Select `school_agent` from the dropdown and start chatting!

#### ⌨️ Option D — CLI Interactive Mode
```bash
python main.py
```

---

---

## 💬 Example Queries to Try

| Query | Routes To |
|---|---|
| `"What is the difference between a metaphor and a simile?"` | 📚 English Teacher |
| `"Solve: 2x² + 5x - 3 = 0"` | 📐 Maths Teacher + Calculator |
| `"Explain Newton's Third Law with examples"` | 🔬 Science Teacher |
| `"What caused World War 1?"` | 📜 History Teacher |
| `"What is the capital of New Zealand and what climate does it have?"` | 🌍 Geography Teacher |
| `"Write a Python function to reverse a linked list"` | 💻 CS Teacher + Search |
| `"What is the difference between RAM and ROM?"` | 💻 CS Teacher |
| `"Calculate the area of a circle with radius 7.5"` | 📐 Maths Teacher + Calculator |

---

## 🧠 A2A Communication — How It Works

1. **Student asks** a question in natural language
2. **School Agent** uses intent recognition to identify the subject
3. **School Agent delegates** to the relevant Subject Teacher via A2A protocol
4. **Subject Teacher** processes the query using its specialised knowledge + tools
5. **School Agent** aggregates the response and returns it to the student

```
User → School Agent → [A2A] → Subject Teacher → Response → School Agent → User
```

---

## 🔧 Technical Details

### Memory (Level 2)
- Uses `InMemorySessionService` from Google ADK
- Each session maintains full conversation history
- Students can ask follow-up questions with full context preserved
- Session ID and User ID generated per run

### Tools (Level 2)

**Calculator Tool** (Maths Agent)
- Custom `FunctionTool` wrapping Python's `math` library
- Supports: `sqrt`, `log`, `sin`, `cos`, `tan`, `factorial`, `pi`, `e`
- Safe evaluation with character whitelist (no code injection)
- Handles expressions like `sqrt(144)`, `3**2 + 4**2`, `factorial(5)`

**Google Search Tool** (CS Agent + Root Agent)
- Uses ADK's built-in `google_search` tool
- CS Agent uses it for latest documentation, code examples, and CS news
- Root Agent uses it as fallback for general knowledge queries

### Models
All agents use `gemini-2.5-flash` for fast, high-quality responses.

### Transport
- A2A Communication: JSON over HTTP (via Google ADK)
- Session Management: In-memory (upgradeable to Cloud Firestore)

---

## 🌟 Bonus Challenges Completed

### 🔥 Level 1
- [x] **Geography Agent** — Physical/Human Geography, Countries, Climate, Ecosystems
- [x] **Computer Science Agent** — Programming, Algorithms, Data Structures, AI/ML + Google Search

### 🚀 Level 2
- [x] **Memory (Conversation History)** — `InMemorySessionService` with persistent session across turns
- [x] **Tool Usage** — Calculator tool (Maths) + Google Search tool (CS + Root)

---

## 🛠️ Extending the System

Adding a new subject agent is simple:

```python
# agents/physics_agent.py
from google.adk.agents import Agent

physics_agent = Agent(
    name="physics_teacher",
    model="gemini-2.0-flash",
    description="Expert Physics Teacher...",
    instruction="You are a Physics Teacher..."
)
```

Then register in `root_agent.py`:
```python
from agents.physics_agent import physics_agent

root_agent = Agent(
    ...
    sub_agents=[..., physics_agent],
)
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

## 👤 Author

**Meet Bhorania**  
AI Engineer & Builder · GDG London Speaker · Hackathon Winner  
[GitHub](https://github.com/meetbhorania) · [LinkedIn](https://www.linkedin.com/in/meetbhorania/)

---

*Built for GDG London ADK Assignment — demonstrating A2A multi-agent architecture with Google ADK*
