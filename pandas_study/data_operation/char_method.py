import pandas as pd

df = pd.read_excel('./天气处理后数据.xlsx')
print(df.head())

condition = df['data'].str.startswith('2020-03')

print(df[condition].head())