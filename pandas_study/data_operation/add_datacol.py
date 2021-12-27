import pandas as pd

fpath = './wheather.txt'
df = pd.read_csv(
    fpath,
    sep='\t',
    header=None,
    names=['data', 'high', 'low', 'weather', 'wind', 'quality']
)
print(df.head())
print('#' * 60)

""" 1.直接赋值法 """
df.loc[:, 'high'] = df['high'].str.replace('°', '').astype('int32')
df.loc[:, 'low'] = df['low'].str.replace('°', '').astype('int32')
print(df.head())
print('#' * 60)

# 计算温度差
df.loc[:, 'wencha'] = df['high'] - df['low']
print(df.head())
print('#' * 60)

"""2.df.apply方法"""


def get_wendu_type(x):
    if x['high'] > 33:
        return '高温'
    if x['low'] < 5:
        return '低温'
    return '常温'


#  注意设置axis==1，这表示series的index是columns
#  如果axis == 0 ，表示添加行
df.loc[:, 'wendu_type'] = df.apply(get_wendu_type, axis=1)
print(df['wendu_type'].value_counts())
print(df.head())
print('#' * 60)

"""3.df.assign方法
    返回新的一个dataframe,不会改原来df
"""
# 可以同时添加多个列
df2 = df.assign(
    # 温度转化为华氏度
    high_huashi=lambda x: x['high'] * 9 / 5 + 32,
    low_huashi=lambda x: x['low'] * 9 / 5 + 32
)
print(df2.head())
print('#' * 60)

"""
4.按条件选择分组，分别赋值
"""
# 先创建空列
df['wencha_type'] = ''
df.loc[df['high']-df['low']>10, "wencha_type"] = '温差大'
df.loc[df['high']-df['low']<=10, "wencha_type"] = '温差正常'
print(df['wencha_type'].value_counts())

df.to_excel('天气处理后数据.xlsx')