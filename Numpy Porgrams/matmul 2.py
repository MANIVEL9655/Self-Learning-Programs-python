import numpy as np
a=np.arange(1,10).reshape(3,3)
print(a)
print("====================")

b=np.random.randint(1,5,size=(3,3))
print(b)
print("====================")

c=np.matmul(a,b)
print(c)
