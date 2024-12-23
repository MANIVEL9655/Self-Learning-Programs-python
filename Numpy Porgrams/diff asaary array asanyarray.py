import numpy as np
list = ([2,3,5])
a=np.array([1,2,3])
c=np.asarray(list)
f=np.asarray(list)
d=np.asarray(a)

f[1]=200
print(f)
print(list)
print(type(c))
print("===========")
d[1]=100
print(a)
print(d)



# c[1]=100
# print(c)
# print(a)
# d[2]=100
# print(a)

