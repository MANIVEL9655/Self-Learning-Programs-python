import numpy as np
a=np.array([[[[[[[[[[[[[[[[[[[[[[[1,2,3,4]]]]]]]]]]]]]]]]]]]]]]])
b=(a[:,np.newaxis])
print(b)
print(b.ndim)
print(b.shape)