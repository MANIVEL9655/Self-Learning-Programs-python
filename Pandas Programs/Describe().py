import pandas as pd
import numpy as np
lst=[2,4,6,8,10]
idx=list("ABCED")
s=pd.Series(data=lst,dtype=float,copy=True,index=idx,name="DESCRIBE")
print(s)
print("=========================")
print(s.describe(percentiles=None))