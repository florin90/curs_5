import matplotlib.pyplot as plt
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 8, 4)
f = web.DataReader('AMZN', 'quandl', start=start, end=end, access_key = "x-8yTbx2SSaS-9k1N6wY")
print(f.describe())
print("Media pe open", f['Open'].mean())
print("Media pe high", f['High'].mean())
print("Standard deviation open", f['Open'].std())
print("Standard deviation high", f['High'].std())
print("Variance for open", f['Open'].var())
print("Variance for hihg", f['High'].var())
print("Covariance of this dataframe")
print(f.cov())
print(f.columns)
print(f.rolling(20).mean())
print(f.rolling(50).mean())
plt.figure()
plt.scatter(f['Open'],f['Close'])
plt.show()