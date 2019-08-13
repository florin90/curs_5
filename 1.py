# import numpy as np
# import pandas as pd
#
# my_numpy_array = np.random.rand(3)
# print(my_numpy_array)
# my_first_series = pd.Series(np.random.rand(3))
# # print(type(my_first_series))
# print(my_first_series)
# print(my_first_series[0])


# import numpy as np
# import pandas as pd
#
# my_first_series = pd.Series(np.random.rand(3), index=["First", "Second", "Third"])
# print(my_first_series)
# print(my_first_series.index)


# import numpy as np
# import pandas as pd
#
# array_2d = np.random.rand(3, 2)
# print(array_2d[0,1])
# df = pd.DataFrame(array_2d)
# print(df)
# print(df[0][0])
# print(df.columns)
# df.columns = ["First", "Second"]
# print(df)
# print(df["Second"])


# import pandas as pd
#
# a = [{"playerID":"hopkide01","name":"Dean Hopkins"},{"playerID":"mairad01","name":"Adam Mair"},{"playerID":"chaseke01","name":"Kelly Chase"}]
# df1 = pd.DataFrame(a)
# print(df1)
# b = [{"playerID":"hopkide01","goals":4},{"playerID":"mairad","goals":1},{"playerID":"chaseke01","goals":5}]
# df2 = pd.DataFrame(b)
# print(df2)
# print(pd.merge(df1, df2,on="playerID"))
# print(pd.merge(df1, df2,on="playerID",how='left'))
# print(pd.merge(df1, df2,on="playerID",how='right'))


# import pandas as pd
#
# a = [{"id":1, "name":"George"},{"id":2, "name":"Sorin"}, {"id":3,"name":"Andrei"},{"id":4, "name":"Catalin"}]
# df = pd.DataFrame(a)
# df1 = df.set_index('id')
# print(df)
# print(df1)


# import pandas as pd
#
# a = [{"id":1, "name":"George"},{"id":2, "name":"Sorin"}, {"id":3,"name":"Andrei"},{"id":4, "name":"Catalin"}]
# df = pd.DataFrame(a)
# df1 = df.set_index('id')
# print(df)
# print(df['name'])
# print(df1)


# pd.loc - select by label, pd.iloc - select by position

#
# import pandas as pd
#
# a = [{"playerID":1, "name":"George"},{"playerID":2, "name":"Sorin"}, {"playerID":3,"name":"Andrei"},{"playerID":4, "name":"Catalin"},{"palyerID":5,"name":"George"}]
# df = pd.DataFrame(a)
# print(df.loc[0,"name"])
# print(df.iloc[0,0])
# names = df['name']
# print(pd.unique(names))


# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
#                    'B': 'one one two three two two one three'.split(),
#                    'C': np.arange(8), 'D': np.arange(8) * 2})
# print(df)
# print(df.loc[df['A'] == 'foo'])
# print(df.loc[df['B'].isin(['one','three'])])


# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
#  'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
#  'C' : np.random.randn(8),
#  'D' : np.random.randn(8)})
# print(df)
# grouped = df.groupby('A')
# print("Minimum per group")
# print(grouped.min())
# print("Maximum per group")
# print(grouped.max())
# print("Suma per group")
# print(grouped.sum())
#
# for latter, group_df in grouped:
#  print(latter)
#  print(group_df)


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



















