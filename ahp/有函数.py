import numpy as np
import pandas as pd
import math
def ahp():
    df = pd.read_excel('/Users/sss/PycharmProjects/StandardResearch/ahp/testmodel张惠锋.xlsx')
    # A-B
    list1=[1,4,2,5,7,12,2,7,15,19,2,6,22,25,2,5,28,30,2,4,33,35,2,4,38,40,2,4,43,45,2,4,48,
           51,2,5,54,56,2,4,59,61,2,4,64,66,2,4,69,71,2,4,74,76,2,4,79,81,2,4,84,86,2,4]
    i=0
    list3 =[]
    list4 =[]



    #dfb2c.columns = ['C21', 'C22', 'C23', 'C24']
    for q in range(int(len(list1)/4)):#循环读取每一个权重表格
        dfab = df.iloc[list1[i]:list1[i+1], list1[i+2]:list1[i+3]]
        i=i + 4

        list = []
        list2 = []
        G = globals()


        sumw = 0
        for a in range(len(dfab)):  # 每行相乘
            mb1 = 1
            for b in range(len(dfab)):
                num1 = dfab.iloc[a, b]
                mb1 = mb1 * num1
            w = math.pow(mb1, 1 / len(dfab))  # M的n次方根(W)

            list.append(w)

            sumw = sumw + w

        for c in list:
            Normalizedindex = c / sumw #w归一化处理
            list2.append(Normalizedindex) #按指标矩阵存储归一化处理的数据 循环16个list
        list3.append(list2)#将16个list当成元素存到一个list中 【【】，【】】
    #print(list3)
    for r in list3:#将16个list循环取出
        for t in r:#将每一个list循环取出存到list4中
            list4.append(t)#list4里有40个指标
            #array4 = np.array(list4)

#fristindex
    B = np.array(list4[0:3])
#secondindex
    C1 = np.array(list4[3:8]) * B[0]
    C2 = np.array(list4[8:12]) * B[1]
    C3 = np.array(list4[12:15]) * B[2]
#thridindex
    D11 = np.array(list4[15:17]) * C1[0]
    D12 = np.array(list4[17:19]) * C1[1]
    D13 = np.array(list4[19:21]) * C1[2]
    D14 = np.array(list4[21:23]) * C1[3]
    D15 = np.array(list4[23:26]) * C1[4]
    D21 = np.array(list4[26:28]) * C2[0]
    D22 = np.array(list4[28:30]) * C2[1]
    D23 = np.array(list4[30:32]) * C2[2]
    D24 = np.array(list4[32:34]) * C2[3]
    D31 = np.array(list4[34:36]) * C3[0]
    D32 = np.array(list4[36:38]) * C3[1]
    D33 = np.array(list4[38:40]) * C3[2]
#指标对应下标  一级指标B[0]开始 二级C1[0] 三级D11[0]
    #print(list4)
    #print(len(list4))

    #print(D33[0])
    return B,C1,C2,C3,D11,D12,D12,D13,D14,D15,D21,D22,D23,D24,D31,D32,D33

def fuzzy():
    df = pd.read_excel('/Users/sss/PycharmProjects/StandardResearch/ahp/Scoresheet.xlsx')
    expertnum = 8
    # 读评分表数据
    Scoresheet = df.iloc[1:26, 1:6]
    # 归一化处理
    Normalizedsheet = Scoresheet / expertnum
    R = np.array(Normalizedsheet)
    s1 = slice(0, 2)
    R1 = R[s1]

    s2 = slice(2, 4)
    R2 = R[s2]
    s3 = slice(4, 6)
    R3 = R[s3]
    s4 = slice(6, 8)
    R4 = R[s4]
    s5 = slice(8, 11)
    R5 = R[s5]
    s6 = slice(11, 13)
    R6 = R[s6]
    s7 = slice(13, 15)
    R7 = R[s7]
    s8 = slice(15, 17)
    R8 = R[s8]
    s9 = slice(17, 19)
    R9 = R[s9]
    s10 = slice(19, 21)
    R10 = R[s10]
    s11 = slice(21, 23)
    R11 = R[s11]
    s12 = slice(23, 25)
    R12 = R[s12]


    print(ahp())

    #print(R.shape)

    #print(R)

if __name__ == '__main__':
    ahp()
    fuzzy()
    #print(D11)
    # print("获取到所有的值:\n{0}".format(dfab))  #格式化输出

    '''mb1 = dfab.iloc[0, 0] * dfab.iloc[0, 1] * dfab.iloc[0, 2]
    mb2 = dfab.iloc[1, 0] * dfab.iloc[1, 1] * dfab.iloc[1, 2]
    mb3 = dfab.iloc[2, 0] * dfab.iloc[2, 1] * dfab.iloc[2, 2]

    w1 = math.pow(mb1, 1 / n1)  # M的n次方根(W)
    w2 = math.pow(mb2, 1 / n1)
    w3 = math.pow(mb3, 1 / n1)

    B1 = w1 / (w1 + w2 + w3)  # 归一化处理
    B2 = w2 / (w1 + w2 + w3)
    B3 = w3 / (w1 + w2 + w3)'''



    # print("获取到所有的值:\n{0}".format(dfab))  #格式化输出
    # print(B1,B2,B3)
    # print(format(dfb1c))
    # print(format(dfb2c))






'''dfbAB = df.iloc[1:4, 2:5]
    dfB1C = df.iloc[7:12, 2:7]
    dfB2C = df.iloc[15:19, 2:6]
    dfB3C = df.iloc[22:25, 2:5]
    dfC11D = df.iloc[28:30, 2:4]
    dfC12D = df.iloc[33:35, 2:4]
    dfC13D = df.iloc[38:40, 2:4]
    dfC14D = df.iloc[43:45, 2:4]
    dfC15D = df.iloc[48:51, 2:5]
    dfC21D = df.iloc[54:56, 2:4]
    dfC22D = df.iloc[59:61, 2:4]
    dfC23D = df.iloc[64:66, 2:4]
    dfC24D = df.iloc[69:71, 2:4]
    dfC31D = df.iloc[74:76, 2:4]
    dfC32D = df.iloc[79:81, 2:4]
    dfC33D = df.iloc[84:86, 2:4]'''
