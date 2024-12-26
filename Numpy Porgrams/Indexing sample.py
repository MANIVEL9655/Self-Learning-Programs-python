import  numpy as np
a=np.array([1,3,4,56,67,9,3,21,4])
for i in enumerate(a):
    print(i)
print("====================")
print(a[[3,4,0]])
print(a[[-1,2,3]])