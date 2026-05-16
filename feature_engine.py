import pandas as pd
import numpy as np

from config import (
    MIN_CORRECTION,
    MAX_CORRECTION,
    MAX_RSI,
    EMA_PERIOD
)

# =========================
# PRICE CORRECTION %
# =========================

def calc_correction(hist):
    """
    Peak to current correction %
    """
    if hist is None or hist.empty:
        return None

    peak = hist["Close"].max()
    current = hist["Close"].iloc[-1]

    correction = ((peak - current) / peak) * 100
    return correction


# =========================
# EMA TREND (20 WEEK APPROX)
# =========================

def ema_trend(hist):
    """
    Simple trend filter using EMA
    """
    close = hist["Close"]

    ema = close.ewm(span=EMA_PERIOD, adjust=False).mean()

    if len(ema) < 2:
        return False

    return ema.iloc[-1] > ema.iloc[-5]  # rising trend


# =========================
# RSI CALCULATION
# =========================

def compute_rsi(hist, period=14):
    delta = hist["Close"].diff()

    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()

    rs = gain / (loss + 1e-9)
    rsi = 100 - (100 / (1 + rs))

    return rsi


def rsi_filter(hist):
    rsi = compute_rsi(hist)

    if rsi is None or len(rsi) < 2:
        return False, None

    latest = rsi.iloc[-1]
    prev = rsi.iloc[-3]

    # Rising but below threshold (your condition)
    condition = (latest < MAX_RSI) and (latest > prev)

    return condition, latest


# =========================
# GROWTH PROXY (SIMPLIFIED)
# =========================

def growth_score(info):
    """
    Proxy using revenue + profit growth if available
    """

    try:
        profit_margin = info.get("profitMargins", 0) or 0
        revenue_growth = info.get("revenueGrowth", 0) or 0

        score = (profit_margin * 50) + (revenue_growth * 50)
        return min(max(score, 0), 100)

    except:
        return 0


# =========================
# DEBT CHECK
# =========================

def debt_score(info):
    try:
        debt = info.get("debtToEquity", 0) or 0

        # lower debt = higher score
        if debt == 0:
            return 100

        return max(0, 100 - debt)

    except:
        return 50


# =========================
# MASTER FEATURE BUILDER
# =========================

def build_features(stock_data):
    """
    Returns all computed signals for scoring
    """

    hist = stock_data["history"]
    info = stock_data["info"]
    symbol = stock_data["symbol"]

    correction = calc_correction(hist)
    ema_ok = ema_trend(hist)
    rsi_ok, rsi_value = rsi_filter(hist)

    growth = growth_score(info)
    debt = debt_score(info)

    return {
        "symbol": symbol,
        "correction": correction,
        "ema_trend": ema_ok,
        "rsi_ok": rsi_ok,
        "rsi": rsi_value,
        "growth": growth,
        "debt": debt
    }
