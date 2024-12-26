import numpy as np
x=np.array([
    [0,1,2],
    [300,400,500],
    [6,7,8],
    [900,1000,1100]
])

print(x)
print("=============")
rows = np.array([[2,3],[0,3],[3,0],[3,2],[1,1]])
cols = np.array([[0,0],[2,1],[2,1],[1,0],[2,2]])
# print(rows)
# print(cols)
# print("==========================")
# y=[rows,cols]
# print(y)
y=x[rows,cols]
print(y)