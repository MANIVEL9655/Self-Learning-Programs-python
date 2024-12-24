import numpy as np
x=(1,2,3,4,5,6)
a=np.asarray(x,dtype="S1",order="C").reshape(2,3)
print(a)
print(type(a))