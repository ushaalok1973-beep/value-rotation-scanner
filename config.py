# =========================
# VALUE ROTATION SCANNER CONFIG (FIXED)
# =========================

# -------------------------
# DATA INPUT
# -------------------------
UNIVERSE_FILE = "universe.csv"

# IMPORTANT: column name expected in CSV
SYMBOL_COLUMN = "Symbol"

# If your CSV uses different naming, fallback logic can use this list in code
POSSIBLE_SYMBOL_COLUMNS = ["Symbol", "SYMBOL", "Ticker", "TICKER"]

# -------------------------
# UNIVERSE CONTROL
# -------------------------
USE_NIFTY50 = True
USE_MIDCAP150 = True
USE_SMALLCAP250 = True

# -------------------------
# OUTPUT CONTROL
# -------------------------
TOP_N_RESULTS = 10   # ✅ FIX: you asked top 10 only

# -------------------------
# MARKET CAP FILTER
# -------------------------
MIN_MARKET_CAP_CR = 1000

# -------------------------
# PRICE CORRECTION FILTER (CORE STRATEGY)
# -------------------------
MIN_CORRECTION = 40
MAX_CORRECTION = 50

# -------------------------
# TECHNICAL FILTERS
# -------------------------
MAX_RSI = 45
EMA_PERIOD = 20

# -------------------------
# FUNDAMENTAL FILTERS
# -------------------------
MAX_PEG = 1.0
MIN_PEG = 0.0   # ✅ FIX: required for scorer import compatibility

MAX_PE = 25

MIN_FII_DII_HOLDING = 2  # combined %
MIN_ROE = 10
MAX_DEBT_TO_EQUITY = 1.5

# -------------------------
# SCORING WEIGHTS (BASE 10 SYSTEM)
# -------------------------
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
    "peg": 1.0,
    "pe": 1.0
}

# -------------------------
# AI LAYER
# -------------------------
AI_BONUS_MAX = 2.0

# -------------------------
# DATA QUALITY SETTINGS
# -------------------------
DROP_INVALID_ROWS = True
REQUIRE_ALL_COLUMNS = False

# -------------------------
# SAFE DEFAULTS FOR SCANNER
# -------------------------
MAX_STOCKS_TO_PROCESS = 700


SECTOR_MAP = {
    "TCS": "IT",
    "INFY": "IT",
    "HCLTECH": "IT",
    "WIPRO": "IT",
    "TECHM": "IT",

    "HDFCBANK": "BANKING",
    "ICICIBANK": "BANKING",
    "SBIN": "BANKING",
    "KOTAKBANK": "BANKING",
    "AXISBANK": "BANKING",

    "MARUTI": "AUTO",
    "M&M": "AUTO",
    "TATAMOTORS": "AUTO",

    "SUNPHARMA": "PHARMA",
    "CIPLA": "PHARMA",
    "DRREDDY": "PHARMA",

    "RELIANCE": "ENERGY",
    "ONGC": "ENERGY",
    "IOC": "ENERGY",
}
