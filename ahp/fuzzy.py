import numpy as np
import pandas as pd

from excel.common import Index


class Fuzzy:
    def __init__(self):
        self.arrays=dict()

    def read(self,file ='./ahp/Scoresheet.xlsx'):
        id = Index()
        with pd.ExcelFile(file) as xls:
            df = pd.read_excel(xls,header=None)
            name_arr,value_arr = df.loc[2:,0].values,df.loc[2:,1:].values.astype(np.float)
            for i in range(name_arr.shape[0]):
                row_value_arr = value_arr[i,:]
                row_value_arr/=np.sum(row_value_arr)
                found = id.find(name_arr[i])
                self.add(found, row_value_arr)
            # print(self.arrays)
            xls.close()

    def add(self, found, temp):
        #并行放置同name类的一行一维矩阵temp
        if found not in self.arrays:
            self.arrays[found] = temp
        else:
            self.arrays[found] = np.vstack((self.arrays[found], temp))

    def calculate(self, array_list):
        R_array_dict=self.arrays.copy()
        self.arrays.clear()
        id = Index()
        pointer = 0
        for key in R_array_dict:
            A = array_list[pointer]
            R = R_array_dict[key]
            B = np.dot(A,R)
            found = id.find(key)
            # 只有一类时
            if not found:
                found = '1'
            self.add(found, B)
            pointer+=1
        print(self.arrays)

    def judge(self):
        result = self.arrays['1']
        j = np.argmax(result)
        if j == 0:
            print("非常不好")
        if j == 1:
            print("不好")
        if j == 2:
            print("一般")
        if j == 3:
            print("较好")
        if j == 4:
            print("非常好")