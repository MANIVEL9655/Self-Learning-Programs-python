import numpy as np
a = np.array([[4,2,3],[2,2,3],[1,4,5]])
b = np.array([[4,2,3],[2,2,3],[1,4,5]])
print(a)
d=a,b
print(d)
c=np.linalg.det(d)
print(c)