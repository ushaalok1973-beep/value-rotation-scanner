# =========================
# VALUE ROTATION SCANNER CONFIG
# =========================

UNIVERSE_FILE = "universe.csv"

MIN_MARKET_CAP_CR = 1000

# Price correction range (your core idea)
MIN_CORRECTION = 40
MAX_CORRECTION = 50

# Technical filters
MAX_RSI = 45
EMA_PERIOD = 20

# Fundamental filters
MAX_PEG = 1.0
MIN_FII_DII_HOLDING = 2  # combined %

# Scoring weights (base 10 system)
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

# AI adjustment (hybrid layer)
AI_BONUS_MAX = 2.0
