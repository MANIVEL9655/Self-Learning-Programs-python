import numpy as np
a=[[2,5],
   [3,4],
   [10,20]]
print("Dime",np.ndim(a))
print("Shape",np.shape(a))

print("Axis=0")

sumanswer = np.sum(a,axis=0)
print("="*30)

print(np.sum(a,axis=1))

