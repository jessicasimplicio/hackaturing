import pandas as p
import pandas as pd
import numpy as np

with open('C:/Users/Paloma/Desktop/Hackthon/BASE_DE_DADOS_HACKATUNING.csv') as csv_file:
    df = p.read_csv(csv_file, na_values='NaN', delimiter=';')
    df = df.dropna(1)#clear all columns an rows (NULL)

#print(df.head(2))
archive = 'C:/Users/Paloma/Desktop/Hackthon/BASE_DE_DADOS_HACKATUNING_CLEANUP.csv'
df.to_csv(archive, sep= ';', header=True) 

