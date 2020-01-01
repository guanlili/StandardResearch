import math
from collections import defaultdict

import numpy as np
import pandas as pd

from excel.common import Grade


class AHP:
    def __init__(self):
        self.arrays = dict()

    def read(self,file ='./ahp/testmodel张惠锋.xlsx'):
        self.arrays.clear()
        with pd.ExcelFile(file) as xls:
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name,header=None)
                df = df.loc[2:,2:]
                self.arrays[sheet_name] = df.values
                # print(self.arrays[sheet])
            xls.close()

    def weight_normalize(self):
        self.weight_arrays = defaultdict(list)
        grade = Grade()
        for sheet_name in self.arrays:
            w_arr =self.weight_normalize_one(self.arrays[sheet_name])
            p_c = grade.find(sheet_name)
            grade_class = p_c[0][0]
            # 每个大类按小表顺序放置到列表，坑
            self.weight_arrays[grade_class].append(w_arr)
        print(self.weight_arrays)

    @staticmethod
    def weight_normalize_one(array):
        row_weight_array = np.zeros((array.shape[0]))
        for a in range(array.shape[0]):
            mb = 1
            # 每行相乘得到mb
            for b in range(array.shape[1]):
                mb *= array[a][b]
            # mb的n次方根(W)
            w = math.pow(mb, 1 / array.shape[0])
            row_weight_array[a]=w
        row_weight_array /= np.sum(row_weight_array)
        return row_weight_array

    def deliver_grade_weight(self, parent_name, child_name):
        res = []
        child_pointer = 0
        for parent in self.weight_arrays[parent_name]:
            for i in range(parent.shape[0]):
                child =self.weight_arrays[child_name][child_pointer]
                # print(parent[i],child)
                temp = parent[i] * child
                res.append(temp)
                child_pointer+=1
        res_name = parent_name+child_name
        self.weight_arrays[res_name] = res
        return res_name
    def get_weight_array(self,name):#指标矩阵
        res =self.weight_arrays[name]
        print(res)
        return res