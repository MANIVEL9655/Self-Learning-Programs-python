import numpy as np
a=np.identity(4,dtype=bool).reshape(4,4)
print(a)

print("="*50)

b=np.identity(4,dtype=bytes).reshape(4,4)
print(b)

print(5*"===========")
c=np.identity(4,dtype=str).reshape(4,4)
print(c)


print(5*"===========")
c=np.identity(4,dtype=bytearray).reshape(4,4)
print(c)

print(5*"===========")
c=np.identity(4,dtype=None).reshape(4,4)
print(c)

re=np.array([[1,2,3]])
repeat_=np.repeat(re,5)
print(repeat_)