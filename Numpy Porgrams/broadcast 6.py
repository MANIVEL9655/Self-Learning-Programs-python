import numpy as np


a=np.arange(1,49).reshape(8,1,6,1)
b=np.arange(1,36).reshape(7,1,5)
print(a)
print(np.ndim(a))
print(np.shape(a))
print("=========================================")
print(b)
print(np.ndim(b))
print(np.shape(b))
print("==========================================")

results = a*b
print(results)
print("======================")
print(np.ndim(results))
print(np.shape(results))