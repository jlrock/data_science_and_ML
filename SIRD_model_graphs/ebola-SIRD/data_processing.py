import pandas as pd

def normaliza_sird(filepath: str, populacao: int) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    df_sird = df.iloc[:, 1:5].copy()
    df_normalizado = df_sird/populacao

    return df_normalizado