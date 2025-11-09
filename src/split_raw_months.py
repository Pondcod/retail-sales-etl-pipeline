import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
SOURCE_FILE = RAW_DIR / "sales_2023_all.csv"

def main():
    df = pd.read_csv(SOURCE_FILE)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    for (year, month), group in df.groupby([df["Date"].dt.year, df["Date"].dt.month]):
        out_name = f"sales_{year}_{month:02d}.csv"
        out_path = RAW_DIR / out_name
        group.to_csv(out_path, index=False)
        print(f"Saved {len(group)} rows to {out_path}")

if __name__ == "__main__":
    main()
