import yfinance as yf
import pandas as pd
import time

# =========================
# BASIC SAFE DATA LOADER
# =========================

def get_stock_data(symbol):
    """
    Fetch stock data safely from Yahoo Finance.
    Returns dict or None if fails.
    """

    try:
        ticker = yf.Ticker(symbol)

        # Historical data (2y for trend + correction logic)
        hist = ticker.history(period="2y")

        if hist is None or hist.empty:
            return None

        info = ticker.info

        return {
            "symbol": symbol,
            "history": hist,
            "info": info
        }

    except Exception as e:
        print(f"[YF ERROR] {symbol}: {e}")
        return None


# =========================
# SCREENER (OPTIONAL FALLBACK)
# =========================

def get_screener_data(symbol):
    """
    Placeholder for screener.in scraping.
    If it fails → must NOT break system.
    """

    try:
        # Future integration point
        # Currently disabled safely
        return None

    except Exception:
        return None


# =========================
# MAIN SAFE WRAPPER
# =========================

def fetch_stock(symbol):
    """
    Try YFinance first.
    Screener optional fallback.
    Never crash pipeline.
    """

    data = get_stock_data(symbol)

    if data is None:
        data = get_screener_data(symbol)

    return data


# =========================
# BATCH LOADER (FOR 401 STOCKS)
# =========================

def load_universe(symbol_list, sleep_time=0.2):
    """
    Loads all stocks safely with throttling.
    """

    results = []

    for i, sym in enumerate(symbol_list):
        print(f"Fetching {i+1}/{len(symbol_list)}: {sym}")

        data = fetch_stock(sym)

        if data is not None:
            results.append(data)

        time.sleep(sleep_time)

    print(f"\nLoaded {len(results)} stocks successfully.")
    return results
