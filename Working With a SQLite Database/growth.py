import pandas as pd 
import sqlite3
import math

conn = sqlite3.connect('factbook.db')
df = pd.read_sql_query('Select * from facts;',con = conn)
#print(df.head())
df = df.dropna(axis=0)

df = df[(df['area_land'] >0) & (df['population'] > 0) ]
print(df.head(1))

def pop_growth(country):
    n = country['population'] *(math.e**((country['population_growth']/100)*35))
    return n
df['pop_2050'] = df.apply(pop_growth,axis=1)

df_top = df.sort_values('pop_2050', ascending=False)
print(df_top.head(10))