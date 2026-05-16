# =========================
# VALUE ROTATION SCANNER CONFIG
# =========================

UNIVERSE_FILE = "universe.csv"

# -------------------------
# COLUMN SAFETY (FIX FOR CRASH)
# -------------------------

SYMBOL_COLUMN_PRIMARY = "Symbol"

ALT_SYMBOL_COLUMNS = [
    "Symbol",
    "SYMBOL",
    "Ticker",
    "TICKER",
    "NSE Symbol",
    "nse_symbol",
    "tradingsymbol",
    "TradingSymbol"
]

PRICE_COLUMNS = ["Close", "close", "LTP", "ltp"]
VOLUME_COLUMNS = ["Volume", "volume"]

# -------------------------
# CORE VALUE ROTATION FILTERS
# -------------------------

MIN_MARKET_CAP_CR = 1000

# Deep correction zone (your core idea)
MIN_CORRECTION = 40
MAX_CORRECTION = 50

# Technical filters
MAX_RSI = 45
EMA_PERIOD = 20

# Fundamental filters
MAX_PEG = 1.0
MIN_PEG = 0   # ✅ ADD THIS (fixes ImportError)
MIN_FII_DII_HOLDING = 2  # combined %

# -------------------------
# OPTIONAL FUNDAMENTAL EXPANSION (future-ready)
# -------------------------

MAX_PE = None
MIN_REVENUE_GROWTH = None
MIN_ROE = None
MAX_DEBT_EQUITY = None

# -------------------------
# SCORING SYSTEM
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
    "peg": 1.0
}

# -------------------------
# OUTPUT CONTROL (NEW FIX)
# -------------------------

TOP_RESULTS_LIMIT = 10

SORT_BY = "score"   # or "momentum", "correction", etc.

# -------------------------
# ADVANCED FEATURES
# -------------------------

SECTOR_ROTATION = True
AI_RANKING_SCORE = True
CANDLE_DETECTION_WEEKLY = True

# -------------------------
# RISK / STABILITY
# -------------------------

AI_BONUS_MAX = 2.0
STRICT_COLUMN_CHECK = False
AUTO_DETECT_SYMBOL = True
