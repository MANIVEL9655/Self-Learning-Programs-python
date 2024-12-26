import numpy as np
a=np.arange(1,10,dtype=int)
print(a)
arr=np.array(a)
print(a)
print("===============")
view1=arr.view()
view1[1]=12
print(view1)
print(arr)
print("=============")
copy1=arr.copy()
copy1[1]=13
print(copy1)
print(a)
