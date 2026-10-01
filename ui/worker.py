# ===== LILITH AGENT - WORKER THREAD =====
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from action.responder import respond, respond_no_screen

class LilithWorker(QThread):
    """
    Background thread untuk proses LLM.
    Emit signal ketika response sudah siap.
    """

    response_ready = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, message: str, use_screen: bool = True):
        super().__init__()
        self.message = message
        self.use_screen = use_screen

    def run(self):
        """Jalankan LLM di background thread."""
        try:
            if self.use_screen:
                response = respond(self.message)
            else:
                response = respond_no_screen(self.message)

            self.response_ready.emit(response)

        except Exception as e:
            self.error_occurred.emit(f"[ERROR] {str(e)}")