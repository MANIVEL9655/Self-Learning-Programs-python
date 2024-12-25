import numpy as np
a=np.arange(3)
print(a)
print("=========================")

b=np.random.randint(5,10, size=(3,))
print(b)
print("====================")
print(a*b)
print("==================")

c=np.matmul(a,b)
print(c)