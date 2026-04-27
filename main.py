"""
main.py — Entry point for the School Multi-Agent System

Run modes:
  CLI interactive:  python main.py
  ADK Web UI:       adk web   (in the school-agent/ directory)
"""

import asyncio
import uuid

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from root_agent import root_agent

# ─────────────────────────────────────────────────────────────────────────────
# Session & Runner Setup  (Level 2: Memory / Conversation History)
# ─────────────────────────────────────────────────────────────────────────────
APP_NAME = "school_agent_app"

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)


# ─────────────────────────────────────────────────────────────────────────────
# CLI Interactive Loop
# ─────────────────────────────────────────────────────────────────────────────
async def main():
    print("\n" + "=" * 60)
    print("🏫  Welcome to the School Multi-Agent System")
    print("    Powered by Google ADK  |  A2A Architecture")
    print("=" * 60)
    print("Subjects: English | Maths | Science | History | Geography | CS")
    print("Type 'quit' or 'exit' to leave.\n")

    # Each run gets a unique user + session so memory persists across turns
    user_id = f"student_{uuid.uuid4().hex[:8]}"
    session_id = f"session_{uuid.uuid4().hex[:8]}"

    session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
    )

    print(f"📋 Session started  [user: {user_id}]\n")

    from google.adk.types import Content, Part

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye! Keep learning!")
            break

        if not user_input:
            continue
        if user_input.lower() in {"quit", "exit", "bye"}:
            print("👋 Goodbye! Keep learning!")
            break

        message = Content(role="user", parts=[Part(text=user_input)])

        print("\n🤖 School Agent: ", end="", flush=True)
        full_response = ""

        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=message,
        ):
            if event.is_final_response():
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, "text") and part.text:
                            full_response += part.text

        print(full_response)
        print()


if __name__ == "__main__":
    asyncio.run(main())
