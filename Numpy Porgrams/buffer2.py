

import numpy as np


a=np.frombuffer(b"We Learn the Numpy",dtype="S1", count=-1,offset=0)
# print(a)
# print(a.size)
#Remove the b from the a
b=list(a)
print(type(b))
print(b)
print(len(b))
emptylist=[]
for item in b:
    item=str(item)
    emptylist.append(item[2])
print(emptylist)