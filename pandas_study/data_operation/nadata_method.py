"""
isnull和notnull：检测是否空值，可用于df和series

dropna：丢弃、删除缺失值
    axis：删除行还是列，0（index）；1（columns）；default：0
    how：如果等于any则任何值为空都删除，如果等于all则所有值都为空才删除
    inplace：如果为True则修改当前df，否则返回新的df

fillna：填充空值
    value：用于填充的值，可以是单个值，或者字典（key：列名，value：值）
    method：等于ffill使用前一个不为空的值填充forword fill；
            等于bfill使用后一个不为空的值填充backword fill
    axis：按行还是列填充，0（index）；1（columns）
    inplace：如果为True则修改当前df，否则返回新的df

"""
import pandas as pd

studf = pd.read_excel('./student2.xlsx', skiprows=2)
print(studf)

# 检测空值
print(studf.isnull())

# 单个series检测空值
print(studf['分数'].isnull())

# 检测非空
print(studf['分数'].notnull())
print('#' * 60)

# 筛选没有空分数的所有行
print(studf.loc[studf['分数'].notnull(), :])

"""
删掉全是空值的列,行
"""
# studf2 = studf.dropna(axis="columns",how='all',inplace=False)
# print(studf,studf2)
studf.dropna(axis="columns", how='all', inplace=True)
print(studf)
print('#' * 60)
# 删掉全部为空值的行
studf.dropna(axis='index', how='all', inplace=True)
print(studf)
print('#' * 60)
"""
将分数为空的填充为0分
"""
# studf.fillna({'分数': 0}, inplace=True)
# 等同于
studf.loc[:, '分数'] = studf['分数'].fillna(0)
print(studf)
print('#' * 60)
"""
将姓名缺失的填充
使用前面的有效值进行填充，ffill:forword fill
"""
# studf.fillna(method='ffill', inplace=True)
# print(studf.columns)
studf.loc[:, '姓名'] = studf['姓名'].fillna(method='ffill')
print(studf)

"""
保存清洗好的数据
"""
# studf.to_excel('./student_clean.xlsx', index=False)
