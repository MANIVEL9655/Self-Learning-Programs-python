import numpy as np
a=np.arange(1,21).reshape(5,4)
b=np.arange(1,5).reshape(4,)
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