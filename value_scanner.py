from telegram_alert import send_telegram_message
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
            # Step 2A: build features + score
            features = build_features(stock)
            score = compute_score(features)

            # symbol extraction
            symbol = stock.get("symbol", None)
            if symbol is None:
                continue

            # sector mapping
            from feature_engine import get_sector
            sector = get_sector(symbol)

            # Step 2B: normalize outputs safely
            correction = features.get("correction", 0)
            ema_trend = features.get("ema_trend", False)
            rsi = features.get("rsi", 0)
            growth = features.get("growth", 0)
            debt = features.get("debt", 0)

            results.append({
                "symbol": symbol,
                "sector": sector,
                "score": score,
                "correction": correction,
                "ema_trend": ema_trend,
                "rsi": rsi,
                "growth": growth,
                "debt": debt
            })

        except Exception as e:
            print(f"[ERROR] {stock.get('symbol', 'UNKNOWN')}: {e}")
            continue

    # Step 3: ranking
    df = pd.DataFrame(results)
    df = df.sort_values(by="score", ascending=False)

    # Step 4: filters (your thesis filter)
    df_filtered = df[
        (df["correction"] >= 40) &
        (df["correction"] <= 50) &
        (df["ema_trend"] == True)
    ]
    if len(df_filtered) > 0:

        top = df_filtered.head(5)

        message = "<b>Value Rotation Scan</b>\n\n"

        for _, row in top.iterrows():
        message += (
            f"{row['symbol']} | {row['sector']}\n"
            f"Score: {row['score']:.2f}\n\n"
        )

        send_telegram_message(message)

    print("\nTop 20 Value Rotation Candidates:")
    print(df_filtered.head(20))

    # Save output
    df_filtered.to_csv("rotation_candidates.csv", index=False)
    print("Saved: rotation_candidates.csv")


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    run_scanner()
