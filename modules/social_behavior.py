import numpy as np
import pandas as pd

def generate_behavior(df):
    """Madde bağımlılığı, psikiyatrik ilaç kullanımı, suç kaydı üretir."""
    np.random.seed(42)
    df = df.copy()
    def row_fn(row):
        sub_p = 0.08 if row.get("hld_electricity", 0) == 0 else 0.04
        psych_p = 0.15 if row.get("average_age", 0) >= 50 else 0.08
        crime_p = 0.06 if row.get("quintile", 1) >= 4 else 0.02
        return pd.Series({
            "Substance_Abuse": np.random.choice([0, 1], p=[1-sub_p, sub_p]),
            "Psych_Med_Use": np.random.choice([0, 1], p=[1-psych_p, psych_p]),
            "Criminal_Record": np.random.choice([0, 1], p=[1-crime_p, crime_p])
        })
    df[["Substance_Abuse", "Psych_Med_Use", "Criminal_Record"]] = df.apply(row_fn, axis=1)
    return df
