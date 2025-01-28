import pandas as pd
import numpy as np
from matplotlib.pyplot import prism

istbankbal = [-67,-45,42,343,23,343]
idx = [200,300,400,500,600,700]
bankData =  np.array(istbankbal)
print(bankData)
print('=========================================')
s=pd.Series(data=bankData,copy=True,index=idx,name="The Data")
print(s)
print("==========================================")
print("Adding index integer new")
s[9]=2334.444
print(s)
print("=========================================")
s[300]=123
print(s)
print("=========================================")
print("dtype",s.dtype)
print("length", len(s))
print("s.size",s.size)
print("keys",s.keys())
print("ndim",s.ndim)
print("itemsize",s.items())
print("values",s.values)
print("==================")
print("arrauy",s.array)
# print("abs",s.abs())
print("axes",s.axes)
print(s.any())
print(s.all())
print(s.name)