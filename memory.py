# ===== LILITH AGENT - MEMORY SYSTEM =====
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config

MEMORY_FILE = "lilith_memory.json"

def _load_memory() -> dict:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "history": [],
        "pinned": config.PINNED_MEMORIES.copy()
    }

def _save_memory(data: dict):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ─── HISTORY (Sliding Window) ─────────────────────────

def add_to_history(role: str, content: str):
    data = _load_memory()
    data["history"].append({"role": role, "content": content})
    if len(data["history"]) > config.MAX_HISTORY:
        data["history"] = data["history"][-config.MAX_HISTORY:]
    _save_memory(data)

def get_history() -> list:
    return _load_memory()["history"]

def clear_history():
    data = _load_memory()
    data["history"] = []
    _save_memory(data)
    print("✅ History cleared.")

# ─── PINNED MEMORY ────────────────────────────────────

def get_pinned() -> list:
    return _load_memory()["pinned"]

def add_pinned(fact: str) -> bool:
    data = _load_memory()
    if len(data["pinned"]) >= config.MAX_PINNED:
        print(f"❌ Pinned memory penuh! Maksimal {config.MAX_PINNED}.")
        return False
    if fact in data["pinned"]:
        print("⚠️ Fakta ini sudah ada di pinned memory.")
        return False
    data["pinned"].append(fact)
    _save_memory(data)
    print(f"✅ Pinned: '{fact}'")
    return True

def remove_pinned(index: int) -> bool:
    data = _load_memory()
    if index < 0 or index >= len(data["pinned"]):
        print("❌ Index tidak valid.")
        return False
    removed = data["pinned"].pop(index)
    _save_memory(data)
    print(f"✅ Removed: '{removed}'")
    return True

def list_pinned():
    pinned = get_pinned()
    if not pinned:
        print("📭 Belum ada pinned memory.")
        return
    print(f"📌 Pinned Memories ({len(pinned)}/{config.MAX_PINNED}):")
    for i, fact in enumerate(pinned):
        print(f"   [{i}] {fact}")