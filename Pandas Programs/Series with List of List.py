import pandas as pd
import numpy as np
lst=[[10,20,30,40,50,60],[1,2,3,4,5,6],[12,34,556],[45,67,8,90],[234.5667,56,34,343],[45,55,33,44]]
indx = [1,2,3,4,5,6]
s=pd.Series(data=lst,index=indx,copy=True,name="Dataset")
print(s)
# print(type(lst))
# print(s.ndim)
# print(s.size)
# print(len(s))
