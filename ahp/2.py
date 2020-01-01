import pandas as pd
# 创建空DataFrame实例，DataFrame就是数据帧
df = pd.DataFrame({'id':[1,2,3],'name':['张三','李四','王五']})
# pandas默认第一个列会自动创建索引，使用set_index()方法指定索引
df = df.set_index('id')
df.to_excel("/Users/sss/PycharmProjects/StandardResearch/ahp/output.xlsx") #导出xlsx表
print('Done!')

# index_col参数表示读取时就指定索引列
people = pd.read_excel("/Users/sss/PycharmProjects/StandardResearch/ahp/output.xlsx", index_col='id')

# header=1表示跳过第一行，从第二行开始；当第一行位脏数据时可以这么设置，如果第一行每一列全部为空，那么pandas自动从第二行开始
# people = pd.read_excel("D:\py_workspace\pandas_excel\People.xlsx",header=1)
# shape表示属性，返回元组,元组第一个表示行，第二表示列

# 如果我们excel表格没有列名，需要把header设置为None,那么默认给列名是0，1，2...形式
# people = pd.read_excel("D:\py_workspace\pandas_excel\People.xlsx",header=None)
# 设置列名
# people.columns= ['ID','Type','Title','FirstName','MiddleName','LastName']
# 设置ID列为索引，inplace=True表示直接修改这个DataFrame
# people.set_index('ID',inplace=True) # 注意区别people = people.set_index('ID') 代码
print(people.shape)  # 输出结果:(19972, 6)
# columns属性是列,类型<class 'pandas.core.indexes.base.Index'>
print(people.columns)  # 输出结果:Index(['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName'], dtype='object')
# print("前五行\n", people.head(5))
# print("后三行\n", people.tail(3))
# 由于读取pepole文件时index_col指定了索引列，所以新产生的索引列就是ID，不会自动生成一个索引列
