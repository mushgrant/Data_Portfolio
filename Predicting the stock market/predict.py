import pandas as pd
from datetime import datetime
df = pd.read_csv('sphist.csv')

df['Date'] = pd.to_datetime(df['Date'])
print(df.head(1))
print(df.shape)
df_after = df[df["Date"] > datetime(year=2015,month=4,day=1)]

df.sort('Date',ascending=True)
print(df_after.head(1))
print(df_after.shape)

df['_5day_Avg_Close'] = pd.rolling_mean(df['Close'],window=5).shift(1)
df['_1year_Avg_Close'] = pd.rolling_mean(df['Close'],window=365).shift(1)
print(df.tail())
df['day_Yr_Close_ratio'] = df['_5day_Avg_Close']/df['_1year_Avg_Close']

df['_5day_Vol_Avg'] = pd.rolling_mean(
    df['Volume'],window=5).shift(1)
df['_1year_Vol_Avg'] = pd.rolling_mean(
    df['Volume'], window=365).shift(1)
df['Vol_Ratio_Avg'] = df['_5day_Vol_Avg']/df['_1year_Vol_Avg']

df['_5day_Close_std'] = pd.rolling_std(df['Close'],window=5).shift(1)
df['_1year_Close_std'] = pd.rolling_std(df['Close'],window=365).shift(1)

print(df.tail(5))

df = df[df["Date"] > datetime(year=1951, month=1, day=2)]

df.dropna(axis=0, inplace=True)

df_train = df[df["Date"] < datetime(year=2013,month=1,day=1)]

df_test = df[df["Date"] >= datetime(year=2013,month=1,day=1)]

print(df.columns)
cols = ['_5day_Avg_Close', '_1year_Avg_Close',
       'day_Yr_Close_ratio','_5day_Vol_Avg',
       '_1year_Vol_Avg','Vol_Ratio_Avg',
       '_5day_Close_std','_1year_Close_std']
X_train = df_train[cols]
y_train = df_train['Close']

X_test = df_test[cols]
y_test = df_test['Close']

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
lr = LinearRegression()
lr.fit(X_train, y_train)
pred = lr.predict(X_test)

MAE = mean_absolute_error(y_test, pred)
print(MAE)






