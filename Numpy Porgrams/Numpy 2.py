import numpy as np

a=[[10,80],
   [100,800],
   [1,8]]

print(np.ndim(a))
print(np.shape(a))

print("Dimension", np.ndim(a))
sumanswer = (np.sum(a,axis=1))
print(sumanswer)
print(np.ndim(sumanswer))
print(np.shape(sumanswer))

