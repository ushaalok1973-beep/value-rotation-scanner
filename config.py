# =========================
# VALUE ROTATION SCANNER CONFIG (CLEANED)
# =========================

# Universe
UNIVERSE_FILE = "universe.csv"

# Market cap filter
MIN_MARKET_CAP_CR = 1000

# =========================
# PRICE CORRECTION LOGIC
# =========================
# Your strategy: stocks corrected from highs
MIN_CORRECTION = 40
MAX_CORRECTION = 50

# =========================
# TECHNICAL FILTERS
# =========================
MAX_RSI = 45
EMA_PERIOD = 20

# =========================
# FUNDAMENTAL FILTERS
# =========================

# FIX: unified PEG naming (this was causing your crash)
MIN_PEG = 0.0
MAX_PEG = 1.0

# FII + DII combined holding %
MIN_FII_DII_HOLDING = 2

# Optional safety filters (recommended for scanner stability)
MIN_ROE = 10
MAX_DEBT_TO_EQUITY = 2.0
MIN_REVENUE_GROWTH = 0

# =========================
# SCORING SYSTEM
# =========================

WEIGHTS = {
    "correction": 1.5,
    "growth": 1.5,
    "roe": 1.0,
    "debt": 1.0,
    "fii_dii": 1.0,
    "promoter": 1.0,
    "trend": 1.0,
    "rsi": 1.0,
    "orderbook": 1.0,
    "peg": 1.0
}

# =========================
# AI LAYER
# =========================
AI_BONUS_MAX = 2.0

# =========================
# OUTPUT SETTINGS
# =========================
TOP_N_RESULTS = 10

# =========================
# TELEGRAM (used later)
# =========================
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

# =========================
# DEBUG MODE
# =========================
DEBUG = True
