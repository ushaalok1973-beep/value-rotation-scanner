from config import (
    MIN_CORRECTION,
    MAX_CORRECTION,
    WEIGHTS,
    AI_BONUS_MAX,
    MIN_PEG
)

# =========================
# CORRECTION SCORE (40–50%)
# =========================

def correction_score(value):
    if value is None:
        return 0

    if MIN_CORRECTION <= value <= MAX_CORRECTION:
        return 10

    # partial scoring outside band
    if 30 <= value < MIN_CORRECTION:
        return 6
    if MAX_CORRECTION < value <= 60:
        return 6

    return 0


# =========================
# RSI SCORE
# =========================

def rsi_score(rsi_ok):
    return 10 if rsi_ok else 0


# =========================
# TREND SCORE
# =========================

def trend_score(ema_ok):
    return 10 if ema_ok else 0


# =========================
# FUNDAMENTAL COMPOSITE
# =========================

def fundamental_score(growth, debt):
    return (growth * 0.6) + (debt * 0.4)


# =========================
# RERATING BONUS LOGIC
# =========================

def rerating_bonus(features):
    bonus = 0

    # strong combination triggers rerating
    if features["growth"] > 60:
        bonus += 0.5

    if features["debt"] > 70:
        bonus += 0.3

    if features["ema_trend"] and features["rsi_ok"]:
        bonus += 0.7

    if features["correction"] and 40 <= features["correction"] <= 50:
        bonus += 0.5

    return min(bonus, AI_BONUS_MAX)


# =========================
# MAIN SCORER
# =========================

def compute_score(features):
    """
    Returns final score out of 10
    """

    corr = correction_score(features["correction"])
    rsi = rsi_score(features["rsi_ok"])
    trend = trend_score(features["ema_trend"])
    fund = fundamental_score(features["growth"], features["debt"])

    raw = (
        corr * WEIGHTS["correction"] +
        rsi * WEIGHTS["rsi"] +
        trend * WEIGHTS["trend"] +
        fund * WEIGHTS["growth"]
    ) / 4

    bonus = rerating_bonus(features)

    final_score = raw / 10 + bonus

    # clamp 0–10
    return max(0, min(10, final_score))
