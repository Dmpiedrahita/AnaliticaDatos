import pandas as pd
import numpy as np

route = r"C:\Users\dmpie\Documentos\AnaliticaDatos\data\\"

df = pd.read_csv(route + "D.csv")

# Mostrar las primeras filas del DataFrame
print(df.head)
print(df.shape)
print(df.columns)
print(df.tail)

df['Symbol'] = 'D'
df['Volume_Millions'] = df['Volume'] / 1000000

print(df.head)

df["VolStat"] = (df["High"] - df["Low"]) / df["Open"]
df["Return"] = (df["Close"] / df["Open"]) - 1.0
df.head()

# print(df["Volume_Millions"].min())
# print(df["Volume_Millions"].max())
# print(df["Volume_Millions"].mean().round(4))
# print(df["Volume_Millions"].quantile(0.2))
# print(df["Volume_Millions"].median())
# print(df["Volume_Millions"].describe())

empresas = ["D", "EXC", "NEE", "SO", "DUK"]
variables = ["Open", "High", "Close", "Volume_Millions"]

dfAll = pd.concat(
    pd.read_csv(route + c + ".csv").assign(Empresa=c) for c in empresas
)

dfAll['Volume_Millions'] = dfAll['Volume'] / 1000000

resumen = (
    dfAll.groupby("Empresa")[variables]
    .quantile(0.25)
    .reset_index()
)


print(resumen.describe)
