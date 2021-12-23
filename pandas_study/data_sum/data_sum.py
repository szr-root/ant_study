import pandas as pd

df = pd.read_excel('../add_data_col/天气处理后数据.xlsx')
print(df.head())
df.set_index('data', inplace=True)
print(df.head())
print(df.loc['2020-01-01', :])

"""汇总类统计"""

# 一下子提取所有数字列统计结果
print(df.describe())

# 查看单个series数据
print(df['low'].mean())

# 最高温
print(df['high'].max())

# 最低温度
print(df['low'].min())

"""
唯一去重和按值计数
一般不用于数值列，而是枚举、分类列
"""
print(df['wind'].unique())
print(df['wendu_type'].unique())

# 按值计数
# print(df['wind'].value_counts())
# print(df['weather'].value_counts())

print(df.loc[df['weather'] == '晴', 'high':'weather'])
print(len(df.loc[df['weather'] == '晴']))


"""
协方差 :衡量同向反向程度，如果协方差为正，说明X、Y同向变化，协方差越大说明同向程度越高；
    如果协方差为负，说明X、Y反向运动，协方差越小说明反向程度越高

相关系数：衡量相似程度，当他们的相关系数为1时，说明两个变量变化时的正向相似度最大，
    当相关系数为-1时，说明两个变量变化的反向相似度最大
"""
# 协方差矩阵
print(df.cov())
print('#'*60)
# 相关系数矩阵
print(df.corr())
print('#'*60)

# 单独查看温差和最高温度的相关系数
print(df['wencha'].corr(df['high']))

print(df['high'].corr(df['high']-df['low']))
