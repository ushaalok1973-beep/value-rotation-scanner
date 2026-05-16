import pandas as pd

# =========================
# LOAD NSE FILES
# =========================

midcap = pd.read_csv("ind_niftymidcap150list.csv")
smallcap = pd.read_csv("ind_niftysmallcap250list.csv")

# =========================
# DETECT SYMBOL COLUMN
# =========================

print("\nMidcap Columns:")
print(midcap.columns)

print("\nSmallcap Columns:")
print(smallcap.columns)

# Change this if needed after checking output
symbol_col = "Symbol"

# =========================
# EXTRACT SYMBOLS
# =========================

mid_symbols = midcap[symbol_col].astype(str).tolist()
small_symbols = smallcap[symbol_col].astype(str).tolist()

# =========================
# COMBINE + REMOVE DUPLICATES
# =========================

all_symbols = list(set(mid_symbols + small_symbols))

# =========================
# ADD NSE SUFFIX
# =========================

all_symbols = [s.strip() + ".NS" for s in all_symbols]

# =========================
# SORT
# =========================

all_symbols.sort()

# =========================
# SAVE FINAL UNIVERSE
# =========================

universe = pd.DataFrame({
    "symbol": all_symbols
})

universe.to_csv("universe.csv", index=False)

# =========================
# OUTPUT
# =========================

print(f"\nUniverse created successfully.")
print(f"Total stocks: {len(universe)}")

print("\nSample symbols:")
print(universe.head())
