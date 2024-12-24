import numpy as np

a= np.asarray( [ (1,2,3,4,5),(6,7,8,9,0),(12,34,56,78,90), ],dtype="f8",order="F").reshape(5,3)
print(a)
print(type(a))
