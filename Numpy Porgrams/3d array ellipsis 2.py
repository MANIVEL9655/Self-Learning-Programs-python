import numpy as np
a=np.random.randint(4,20,size=(3,2,2))
print(a)
print(len(a))
print(a.ndim)
print("=====================")
print(a[...,1:])
print("=====================")
print(a[...,1])