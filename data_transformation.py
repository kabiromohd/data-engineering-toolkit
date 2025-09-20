"""
data_transformation.py - simple transformation helpers.
"""
import pandas as pd

def classify_text(text: str, mapping: dict) -> str:
    txt = (text or "").lower()
    for cat, keywords in mapping.items():
        if any(k in txt for k in keywords):
            return cat
    return "other"

def add_complaint_category(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    df = df.copy()
    df['complaint_category'] = df['raw_text'].apply(lambda t: classify_text(t, mapping))
    return df
