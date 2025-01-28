import pandas as pd
import numpy as np
from pandas import pivot

Internal_Marks=[2,4,6,8,10]
External_Marks = [23,34,55,66,45]
s1=pd.Series(data=Internal_Marks,dtype=float,copy=True,name="Internal Marks")
print("original series\n\n",s1,end="\n")
print("=========================")
s2=pd.Series(data=External_Marks,dtype=float,copy=True,name="External Marks")
print("original series\n",s2)
print("=========================")
print(s1+s2)
print("=========================")
print(s1*s2)
