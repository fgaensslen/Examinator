"""Configuration and constants for Examinator."""

from pathlib import Path

# Path Configuration
BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_DIR = BASE_DIR / "static" / "questions"
LAST_UPDATES_FILE = BASE_DIR / "static" / "last_update.md"

# UI Configuration
ITEMS_PER_PAGE = 20
DEFAULT_QUESTIONS = 10
PAGE_TITLE = "Examinator"
PAGE_ICON = "🎓"

# Layout Constants
HR_DIVIDER = '<hr style="margin: 10px 0 15px 0; border: none; border-top: 1px solid #e0e0e0;">'

# Code Language Patterns
SUPPORTED_LANGUAGES = ["JSON", "SQL", "TEXT"]

# Question Rendering
MAX_QUESTIONS_LOAD = None  # None = load all, or set a limit for dev
