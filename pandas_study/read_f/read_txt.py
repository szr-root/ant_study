import pandas as pd

# grades = pd.read_csv(
#     './gards.txt',
#     sep='\t',
#     header=None,
#     names=['学号','语文','数学','英语']
# )
#
# print(grades)

df = pd.read_csv(
    '../wheather.txt',
    sep='\t',
    header=None,
    names=['data', 'high', 'low', 'weather', 'wind', 'quality']
)
# print(df.head())
# 使日期成为第一列index
df.set_index('data', inplace=True)
# print(df.index)
print(df.head())

# 查询所有行，列为'xx'
df.loc[:, 'high'] = df['high'].str.replace('°', '').astype('int32')
df.loc[:, 'low'] = df['low'].str.replace('°', '').astype('int32')
# print(df.dtypes)
# print(df.head())

# 精准查询单个
print(df.loc['2020-01-04', 'high'])

# 得到一个series,行列分别传列表
print(df.loc['2020-01-03', ['high', 'low']])
print('#' * 30)
print(df.loc[['2020-01-01', '2020-01-02', '2020-01-03'], 'high'])

# 得到DataForm
print('#' * 30)
print(df.loc[['2020-01-01', '2020-01-02'], ['high', 'low']])
print(df.loc[['2020-01-01', '2020-01-02'], ['low', 'high']])

print('#' * 30)

# 使用数值区间进行范围查询
print(df.loc['2020-01-01':'2020-01-03', ['low']])
print('#' * 30)
print(df.loc['2020-01-01', 'high':'quality'])
print('#' * 30)
print(df.loc['2020-01-01':'2020-01-03', 'high':'low'])

print('#' * 30)
# 条件表达式进行查询
print(df.loc[df['low'] < 5, 'high':'low'])
print('#' * 30)
print(df.loc[df['low'] < 5, :])
print('#' * 30)
print(df['low'] < 3)
print('#' * 30)

# 复杂查询
print(df.loc[(df['high'] <= 28) & (df['low'] >= 15) & (df['weather'] == '阴')])
print('#' * 30)

# 调用函数查询
print(df.loc[lambda df: (df['high'] <= 30) & (df['low'] >= 15), :])
print('#' * 30)


# 编写函数查询
def query_my_data(df):
    return df.index.str.startswith('2020-09') & df['low'] == 17

print(df.loc[query_my_data, :])
