import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')
df = pd.read_sql_query('Select SUM(area_land),SUM(area_water) from facts WHERE area_land !="";',con = conn)

#print(df)

print(df['SUM(area_land)']/df['SUM(area_water)'])

