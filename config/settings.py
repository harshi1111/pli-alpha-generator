"""Configuration management for PLI Alpha Generator"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
LOGS_DIR = ROOT_DIR / "logs"
REPORTS_DIR = ROOT_DIR / "reports"

# Create directories if they don't exist
for dir_path in [DATA_DIR, LOGS_DIR, REPORTS_DIR]:
    dir_path.mkdir(exist_ok=True)

# API Keys (from environment variables)
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Analysis settings
PLI_SECTORS = {
    'electronics': ['DIXON.NS', 'AMBER.NS', 'SYRMA.NS'],
    'semiconductor': ['SAHASRA.NS', 'MOSCHIP.NS'],
    'logistics': ['TCIEXP.NS', 'BLUEDART.NS'],
    'components': ['PGEL.NS', 'BUTTERFLY.NS']
}

# Risk thresholds
DEBT_EQUITY_THRESHOLD = 0.25  # Industry average
PE_HIGH_THRESHOLD = 150  # Overvalued threshold
VOLUME_LOW_THRESHOLD = 100000  # Low volume threshold

# Buy/Sell parameters
BUY_TRIGGER_PERCENTAGE = 1.02  # 2% above 52-week low
STOP_LOSS_PERCENTAGE = 0.95  # 5% below 52-week low