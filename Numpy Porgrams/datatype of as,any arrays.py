import numpy as np
a=np.array([1,2],dtype=np.float32)
print(np.asarray(a,dtype=np.float32) is a)

print("==========")

print(np.asarray(a,dtype=np.int16))

print("========")

print(np.asanyarray(a,dtype=np.float32))

print("==========")

