# ===== LILITH AGENT - SCREEN CAPTURE =====
import mss
import mss.tools
from PIL import Image
import base64
import io
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def capture_screen() -> Image.Image:
    """Capture seluruh layar dan return sebagai PIL Image."""
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return img

def resize_for_llm(img: Image.Image, max_width: int = 1280) -> Image.Image:
    """Resize image supaya tidak terlalu besar."""
    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)
    return img

def image_to_base64(img: Image.Image) -> str:
    """Convert PIL Image ke base64 string."""
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("utf-8")

def get_screen_context() -> dict:
    """Capture layar dan return context siap pakai."""
    img = capture_screen()
    img = resize_for_llm(img)
    return {
        "image": img,
        "base64": image_to_base64(img),
        "size": img.size
    }