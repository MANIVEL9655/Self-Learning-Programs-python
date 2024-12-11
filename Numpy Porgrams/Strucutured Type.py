import numpy as np

dt= np.dtype([('age', np.int16),('salary',np.float16)])
a=np.array([(100,20000),(200,400),(300,600)],dtype=dt)
print(a)

print(a['age'])
print(a['salary'])