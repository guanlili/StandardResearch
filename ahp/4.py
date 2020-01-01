import numpy as np
import pandas as pd
import math

class AHP:

    def __init__(self, array):
        self.row = len(array)
        self.col = len(array[0])

def main():
    df = pd.read_excel('/Users/sss/PycharmProjects/StandardResearch/ahp/testmodel张惠锋.xlsx')
    # A-B
    dfab = df.iloc[1:4, 2:5]
    dfab.columns = ['B1', 'B2', 'B3']
    # print(dfab.iloc[0,0])#打印0,0位置数据
    # n1 = dfab.size**0.5#获取指标的个数
    n1 = len(dfab)

    def mb(self, mb):
        for a in range(len(dfab)):
            for b in range(len(dfab)):
                mb[a] = dfab.iloc[a, b]
            print(mb[a])

    mb1 = dfab.iloc[0, 0] * dfab.iloc[0, 1] * dfab.iloc[0, 2]
    mb2 = dfab.iloc[1, 0] * dfab.iloc[1, 1] * dfab.iloc[1, 2]
    mb3 = dfab.iloc[2, 0] * dfab.iloc[2, 1] * dfab.iloc[2, 2]

    w1 = math.pow(mb1, 1 / n1)  # M的n次方根(W)
    w2 = math.pow(mb2, 1 / n1)
    w3 = math.pow(mb3, 1 / n1)

    B1 = w1 / (w1 + w2 + w3)  # 归一化处理
    B2 = w2 / (w1 + w2 + w3)
    B3 = w3 / (w1 + w2 + w3)

    # B1-C
    dfb1c = df.iloc[7:12, 2:7]
    dfb1c.columns = ['C11', 'C12', 'C13', 'C14', 'C15']

    dfb2c = df.iloc[15:19, 2:6]
    dfb2c.columns = ['C21', 'C22', 'C23', 'C24']

    # print("获取到所有的值:\n{0}".format(dfab))  #格式化输出
    # print(B1,B2,B3)
    # print(format(dfb1c))
    # print(format(dfb2c))

    if __name__ == '__main__':
        main()
        mb()
        print(mb())



