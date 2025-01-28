import pandas as pd
import numpy as np
lst = [2,4,6,8,10]
data1 = np.array(lst)
print(data1)

s=pd.Series(data1,dtype=float,copy=True)
print("Original series\n",s)
for index,item in enumerate(s):
    print("Index is {},items is {}".format(index,item))
    print('===================================================')

s[2]=400
print(s)
print('============================')
for index,item in enumerate(s):
    print("Index is {},items is {}".format(index,item))
    print('===================================================')
print(s.dtype)
