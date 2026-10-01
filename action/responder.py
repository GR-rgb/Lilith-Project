# ===== LILITH AGENT - RESPONDER =====
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
import memory
from reasoning.llm_client import ask_llm
from perception.screen_capture import get_screen_context

def respond(user_message: str, use_screen: bool = True) -> str:
    """Proses pesan user dan hasilkan response Lilith."""

    history = memory.get_history()
    pinned = memory.get_pinned()

    screen_base64 = None
    if use_screen:
        try:
            screen = get_screen_context()
            screen_base64 = screen["base64"]
            print(f"📸 Screen captured: {screen['size']}")
        except Exception as e:
            print(f"⚠️ Screen capture gagal: {e}")

    response = ask_llm(
        prompt=user_message,
        history=history,
        pinned=pinned,
        image_base64=screen_base64
    )

    memory.add_to_history("user", user_message)
    memory.add_to_history("assistant", response)

    return response

def respond_no_screen(user_message: str) -> str:
    """Respond tanpa screen capture."""
    return respond(user_message, use_screen=False)