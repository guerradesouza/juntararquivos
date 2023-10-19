import pandas as pd
import os

files = [i for i in os.listdir() if ".csv" in i]

df = pd.DataFrame()
for file in files:
    df_temp = pd.read_csv(file)
    df = pd.concat([df, df_temp])

df.to_csv("grouped.csv", sep=",")