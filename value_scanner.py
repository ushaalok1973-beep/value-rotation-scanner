from feature_engine import weekly_trend_filter
import pandas as pd

from data_loader import load_universe
from feature_engine import build_features
from scorer import compute_score

from config import UNIVERSE_FILE


# =========================
# LOAD UNIVERSE
# =========================

def load_symbols():
    df = pd.read_csv(UNIVERSE_FILE)

    symbol_col = None
    for col in df.columns:
        if col.lower() in ["symbol", "ticker"]:
            symbol_col = col
            break

    if symbol_col is None:
        raise ValueError(f"No Symbol column found. Available columns: {list(df.columns)}")

    symbols = (
        df[symbol_col]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    symbols = [
        s.upper().replace(".NS.NS", ".NS").strip()
        for s in symbols
    ]

    symbols = [
        s if s.endswith(".NS") else s + ".NS"
        for s in symbols
    ]

    print("SAMPLE SYMBOLS:", symbols[:10])

    return symbols


# =========================
# MAIN SCANNER
# =========================

def run_scanner():
    symbols = load_symbols()

    print(f"\nTotal symbols: {len(symbols)}")

    # Step 1: fetch data
    raw_data = load_universe(symbols)

    results = []

    # Step 2: feature + scoring
for i, stock in enumerate(raw_data):
    try:
        features = build_features(stock)
        score = compute_score(features)

        symbol = stock["symbol"]

        from feature_engine import get_sector
        sector = get_sector(symbol)

        results.append({
            "symbol": symbol,
            "sector": sector,
            "score": score,
            "correction": features["correction"],
            "ema_trend": features["ema_trend"],
            "rsi": features["rsi"],
            "growth": features["growth"],
            "debt": features["debt"]
        })

    except Exception as e:
        print(f"[ERROR] {stock.get('symbol', 'UNKNOWN')}: {e}")
        continue

    # Step 3: ranking
    df = pd.DataFrame(results)

sector_strength = df.groupby("sector")["score"].mean().to_dict()

df["sector_boost"] = df["sector"].map(sector_strength)

df["score"] = df["score"] + (df["sector_boost"] * 0.15)
# =========================
# STEP 2B: APPLY WEEKLY TREND FILTER (SOFT FILTER)
# =========================
df["score"] = df.apply(
    lambda x: x["score"] * 1.2 if x["ema_trend"] == True else x["score"] * 0.6,
    axis=1
)

# NOW SORT AFTER ADJUSTMENT
df = df.sort_values(by="score", ascending=False)

    # Step 4: filters (your thesis filter)
    df_filtered = df[
        (df["correction"] >= 40) &
        (df["correction"] <= 50) &
        (df["ema_trend"] == True)
    ]

    # Step 5: output
    print("\nTop 20 Value Rotation Candidates:\n")
    print(df_filtered.head(20))

    df_filtered.to_csv("rotation_candidates.csv", index=False)

    print("\nSaved: rotation_candidates.csv")


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    run_scanner()
