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
