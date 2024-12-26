import numpy as np
x=np.array([
    [0,1,2],
    [300,400,500],
    [6,7,8],
    [900,1000,1100]
])

print(x)
print("=============")
rows = x[[[1,3],[3,3]],[[1,2],[0,2]]]
print(rows)