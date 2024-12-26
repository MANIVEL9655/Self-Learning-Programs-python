import numpy as np
a=np.array([np.nan,2,3,np.nan,5,6])
print(a)
print(len(a))
print(type(a))
print("========"*5)
print(a[~np.isnan(a)])
print("===================")
print([~np.isnan(a)])