import pandas as pd
data = pd.read_csv('data/CRDC2013_14.csv', encoding="Latin-1")

data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']

data['all_enrollment'] = data['total_enrollment'].apply(sum)

