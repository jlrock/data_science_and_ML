import numpy as np
import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess

def suavizar_df(df: pd.DataFrame, frac: float = 0.15) -> pd.DataFrame:
    df_suavizado = pd.DataFrame(index=df.index)
    dias = np.arange(len(df))
    for coluna in df.columns:
        suavizado = lowess(df[coluna].values, dias, frac=frac, return_sorted=True)
        df_suavizado[coluna] = suavizado[:, 1]
    return df_suavizado