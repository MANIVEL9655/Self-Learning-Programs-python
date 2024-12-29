import numpy as np


a=np.arange(1,196_609).reshape(256,256,3)
print(a)
print("===================================================")
b=np.arange(1,2)
print(b)
print("===================================================")
result= a*b
print(result)
print("====================================================")
print(np.ndim(result))
print(np.shape(result))
print(len(result))
