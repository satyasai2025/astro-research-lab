"""
Astro Research Lab
Global Application Settings
"""

from pathlib import Path

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "Astro Research Lab"

APP_VERSION = "0.0.1"

ORGANIZATION = "Astro Research Lab"

AUTHOR = "Astro Research Lab Team"

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "datasets"

DOCS_DIR = BASE_DIR / "docs"

DATABASE_DIR = BASE_DIR / "database"

LOG_DIR = BASE_DIR / "logs"

EXPORT_DIR = BASE_DIR / "exports"

TEMP_DIR = BASE_DIR / "temp"

# ==========================================================
# Database
# ==========================================================

DATABASE_NAME = "astro_research_lab.db"

DATABASE_PATH = DATABASE_DIR / DATABASE_NAME

# ==========================================================
# Window
# ==========================================================

WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"

WINDOW_WIDTH = 1600

WINDOW_HEIGHT = 900

MINIMUM_WIDTH = 1200

MINIMUM_HEIGHT = 700

# ==========================================================
# Theme
# ==========================================================

DEFAULT_THEME = "Light"

# ==========================================================
# Research
# ==========================================================

DEFAULT_AYANAMSA = "Lahiri"

DEFAULT_HOUSE_SYSTEM = "Whole Sign"

# ==========================================================
# Create Required Directories
# ==========================================================

REQUIRED_DIRECTORIES = [
    DATA_DIR,
    DATABASE_DIR,
    LOG_DIR,
    EXPORT_DIR,
    TEMP_DIR,
]

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)