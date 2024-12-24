import numpy as np

a= np.fromiter([ (1,2,3,4,5),(6,7,8,9,0),(12,34,56,78,90) ],dtype="f8").reshape(5,3)
print(nex(a))
print(type(a))
print(a.dtype)
