import numpy as np
import pandas as pd
import math

df = pd.read_excel('../ahp/testmodel张惠锋 - 副本.xlsx')
# A-B
list1 = [1, 4, 2, 5, 7, 12, 2, 7, 15, 19, 2, 6, 22, 25, 2, 5, 28, 30, 2, 4, 33, 35, 2, 4, 38, 40, 2, 4, 43, 45, 2, 4,
         48,51, 2, 5, 54, 56, 2, 4, 59, 61, 2, 4, 64, 66, 2, 4, 69, 71, 2, 4, 74, 76, 2, 4, 79, 81, 2, 4, 84, 86, 2, 4]
i = 0
list3 = []
list4 = []
# dfb2c.columns = ['C21', 'C22', 'C23', 'C24']
for q in range(int(len(list1) / 4)):  # 循环读取每一个权重表格
    dfab = df.iloc[list1[i]:list1[i + 1], list1[i + 2]:list1[i + 3]]
    i = i + 4

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
        Normalizedindex = c / sumw  # w归一化处理
        list2.append(Normalizedindex)  # 按指标矩阵存储归一化处理的数据 循环16个list
    list3.append(list2)  # 将16个list当成元素存到一个list中 【【】，【】】
print(list3)
for r in list3:  # 将16个list循环取出
    for t in r:  # 将每一个list循环取出存到list4中
        list4.append(t)  # list4里有40个指标
        # array4 = np.array(list4)
print(list4)

# fristindex
B = np.array(list4[0:3])
# secondindex
C1 = np.array(list4[3:8]) * B[0]
C2 = np.array(list4[8:12]) * B[1]
C3 = np.array(list4[12:15]) * B[2]
# thridindex
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

df1 = pd.read_excel('../ahp/Scoresheet.xlsx')
expertnum = 8
# 读评分表数据
Scoresheet = df1.iloc[1:26, 1:6]
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

B11 = np.dot(D11,R1)
B12 = np.dot(D12,R2)
B13 = np.dot(D13,R3)
B14 = np.dot(D14,R4)
B15 = np.dot(D15,R5)

RR1 = np.vstack((B11,B12,B13,B14,B15)) #vertical stack 上下合并，

B21 = np.dot(D21,R6)
B22 = np.dot(D22,R7)
B23 = np.dot(D23,R8)
B24 = np.dot(D24,R9)

RR2 = np.vstack((B21,B22,B23,B24))

B31 = np.dot(D31,R10)
B32 = np.dot(D32,R11)
B33 = np.dot(D33,R12)
RR3 = np.vstack((B31,B32,B33))

B1 = np.dot(C1,RR1)
B2 = np.dot(C2,RR2)
B3 = np.dot(C3,RR3)

RRR = np.vstack((B1,B2,B3))

BB = np.dot(B,RRR)
print(BB)
j = np.argmax(BB)
if j ==0:
    print("非常不好")
if j ==1:
    print("不好")
if j ==2:
    print("一般")
if j ==3:
    print("较好")
if j ==4:
    print("非常好")












