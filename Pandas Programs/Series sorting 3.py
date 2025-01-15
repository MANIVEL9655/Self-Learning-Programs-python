from trace import Trace

import pandas as pd
import numpy as np
data1= {'a':70,'b':20,'c':100,'d':40,'e':10}
s=pd.Series(data=data1,index=['b','c','d','e','f','a'])
print(s)
print("========================")
print(s.sort_values(ascending=True,ignore_index=False,inplace=False,axis=0))
# print(s.sort_index())