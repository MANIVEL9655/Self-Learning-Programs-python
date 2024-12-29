import numpy as np

a=np.arange(1,226).reshape(15,3,5)
b=np.arange(1,76).reshape(15,1,5)
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
