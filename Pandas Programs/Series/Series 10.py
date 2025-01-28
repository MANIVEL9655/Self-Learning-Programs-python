import pandas as pd
import numpy as np
data = np.array(['a','b','c','d','e'])
s=  pd.Series(data,index=[10,20,30,40,50], copy=True,dtype=str,name="Manivrl")
print(s)
print(15*"=")
s[60]='f'
print(s)
