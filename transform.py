import numpy as np
import pandas as pd

def link2matrix(link):
    # 数据格式参考权力的游戏，将连接类转化为关联矩阵
    label = np.union1d(link.iloc[:, 0], link.iloc[:, 1])
    matrix = pd.DataFrame(0, index=label, columns=label)
    for i in range(len(link.iloc[:, 0])):
        matrix.loc[link.iloc[i, 0], link.iloc[i, 1]] += link.iloc[i, 2]
    return matrix

f = open(r'D:\code\bp\visulization\files\weight_test0828.csv','r',encoding="UTF-8")
data = link2matrix(pd.read_csv(f))
data.to_excel(r'D:\code\bp\visulization\files\weight_test_out0828.xlsx')