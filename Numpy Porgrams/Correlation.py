import numpy as np
# from scipy.special import dtype

a=[       [[10,80],[40,20],[60,40]],[[1,2],[2,3],[4,5]], [[12,3],[6,7],[9,8]]    ]
print("Length", len(a))
print("Dimension", np.ndim(a))
print("Shape",np.shape(a))
print(a[2][0][1])
print(a[1][1])
print("Shape", np.shape(a[2][0][1]))
print("Shape",np.shape(a[1][1]))