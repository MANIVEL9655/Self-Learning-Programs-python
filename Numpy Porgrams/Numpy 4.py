import numpy as np
a =[[[2,5],[3,5],[2,5]],
    [[12,3],[1,6],[4,6]]]
print("Dim", np.ndim(a))
print("Shape", np.shape(a))
print("AXIS 0")
sumanswer= np.sum(a,axis=0)

print(sumanswer)
print("Dim", np.ndim(sumanswer))
print("Shape", np.shape(sumanswer))
print("="*30)

print("AXIS 2")
sumanswer=np.sum(a,axis=2)
print(sumanswer)
print("DIM",np.ndim(sumanswer))
print("shape",np.shape(sumanswer))