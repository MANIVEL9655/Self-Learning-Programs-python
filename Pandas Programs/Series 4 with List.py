import pandas as pd
import numpy as np
lst = [1,2,3,4,5,6]
indx=[10,20,30,40,50,60]
s=pd.Series(data=lst,dtype=float,index=indx,copy=True,name="Dataset")
print(s)