import numpy as np
from numpy.ma.core import array

for i in np.arange(5):
    print(i)
print("===="*6)

np_array_2d= np.arange(0,12).reshape(6,2)
print(np_array_2d)
sumof_array = np.sum(np_array_2d, axis=0)
print("#",sumof_array)
print("==="*4)
sumof_array = np.sum(np_array_2d, axis=1)
print("Axis is 1",sumof_array)
