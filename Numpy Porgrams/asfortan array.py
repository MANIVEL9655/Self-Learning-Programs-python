import numpy as np

a= np.ascontiguousarray( [ (1,2,3,4,5),(6,7,8,9,0),(12,34,56,78,90) ]).reshape(5,3)
print(a)
print(type(a))
print(a.dtype)
