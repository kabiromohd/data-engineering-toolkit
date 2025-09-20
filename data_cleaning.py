"""
data_cleaning.py - small utilities to clean pandas DataFrames.
"""
import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    str_cols = df.select_dtypes(include=['object']).columns
    for c in str_cols:
        df[c] = df[c].str.strip()
    df = df.drop_duplicates()
    return df

if __name__ == "__main__":
    print("data_cleaning module")
