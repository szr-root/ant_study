import pandas as pd

df = pd.read_excel('./result.xlsx')
df.set_index('赛事日期', inplace=True)
print(df.head())
print(df['状态'].value_counts())
# df.loc[:, '状态'] = df['状态'].replace('2', '已完成', inplace=True)
# print(df['状态'].value_counts())
# print(df.columns)
print(df.loc[df['状态'] == 2.0, :])
df.loc[:, '状态'] = df['状态'].replace(2.0, '已完成')
df.loc[:, '状态'] = df['状态'].replace(0.0, '取消')
df.loc[:, '客队 vs 主队'] = df['客队 vs 主队'].replace("[", '')
df.loc[:, '客队 vs 主队'] = df['客队 vs 主队'].replace("]", '')
print(df.loc[df['状态'] == '已完成', :])
# df.to_excel('./修改状态.xlsx')
# print(df['状态'].value_counts())
# print(df.loc['2021-01-21',:])