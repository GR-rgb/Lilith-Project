# ===== LILITH AGENT - LLM CLIENT (Vision Support) =====
import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def ask_llm(
    prompt: str,
    history: list = [],
    pinned: list = [],
    image_base64: str = None
) -> str:
    """
    Kirim prompt ke Ollama dan dapatkan response.
    Support vision — bisa kirim screenshot ke llava:7b.
    """

    # ─── Bangun system prompt ──────────────────────────
    pinned_text = ""
    if pinned:
        pinned_text = "\n\n[Hal yang kamu ingat tentang pengguna]\n"
        for p in pinned:
            pinned_text += f"- {p}\n"

    system_prompt = config.LILITH_PERSONA + pinned_text

    # ─── Bangun messages ───────────────────────────────
    messages = [{"role": "system", "content": system_prompt}]

    for msg in history[-config.MAX_HISTORY:]:
        messages.append(msg)

    # ─── Pesan user + image ────────────────────────────
    if image_base64:
        user_content = {
            "role": "user",
            "content": prompt,
            "images": [image_base64]
        }
    else:
        user_content = {
            "role": "user",
            "content": prompt
        }

    messages.append(user_content)

    # ─── Kirim ke Ollama ───────────────────────────────
    try:
        response = requests.post(
            f"{config.OLLAMA_URL}/api/chat",
            json={
                "model": config.LLM_MODEL,
                "messages": messages,
                "stream": False
            },
            timeout=300
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "[ERROR] Tidak bisa connect ke Ollama. Pastikan Ollama sedang berjalan."
    except requests.exceptions.Timeout:
        return "[ERROR] Ollama timeout. Model sedang sibuk atau terlalu berat."
    except Exception as e:
        return f"[ERROR] {str(e)}"


def test_connection() -> bool:
    """Test apakah Ollama bisa diakses."""
    try:
        response = requests.get(f"{config.OLLAMA_URL}/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False