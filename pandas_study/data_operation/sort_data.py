import pandas
import pandas as pd

df = pandas.read_excel('./天气处理后数据.xlsx')
print(df.head())

# 按series进行排序()
"""
365     0
45      0
221    25
217    25
"""
# print(df['low'].sort_values())

# 排序
"""
显示每一行所有列
"""
# df.sort_values(by='high', inplace=True)
print(df)

# 倒序
df.set_index('data', inplace=True)
print(df.sort_values(by='quality_num', ascending=False))
# 拆分一列
# df[['quality_num', 'quality_type']] = df['quality'].str.split(' ', 2, expand=True)
print(df.head())

"""
多列进行排序
"""
print(df.sort_values(by=['quality_num', 'high'], ascending=[True, False]))

