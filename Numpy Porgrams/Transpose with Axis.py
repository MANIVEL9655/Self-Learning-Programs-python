import numpy as np
a=np.arange(24).reshape([2,3,4])
print(a)
print("====================")
b=a.transpose(1,2,0)
print(b)