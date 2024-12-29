import numpy as np
x=np.arange(1,13)
print(x)
xx=x.reshape((4,3),order='C')
print(xx)
print("===================")
x=np.arange(1,13)
print(x)
yy=x.reshape((4,3),order='A')
print(yy)

