import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.int16)
print(a)
print(id(a))
print("=================")
copy1=a.copy()
print(copy1)
print(type(copy1))
print("====================")
print(a)
print("====================")
copy1[1][2]=50
print(copy1)
print(type(copy1))
print(a)