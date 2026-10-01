# ===== LILITH AGENT - PROMPT ENGINE =====

def build_prompt_with_screen(
    user_message: str,
    screen_description: str = None
) -> str:
    """Gabungkan pesan user dengan screen context."""
    if screen_description:
        return f"[Yang kamu lihat di layar]\n{screen_description}\n\n[Pesan user]\n{user_message}"
    return user_message