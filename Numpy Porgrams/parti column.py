import numpy as np
x=np.array([[0,1,3],[300,400,500],[100,200,500]])
print(x)
print("======================")
z=x[1:4]
print(z)
print("======================")
z=x[1:4,[2,1]]
print(z)
