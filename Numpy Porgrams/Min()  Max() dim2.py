import numpy as np
stats = np.array([[1,2,3],[2,34,45],[90,30,10]])
print(stats)
print(type(stats))
print(np.min(stats,axis=0))
print(np.min(stats,axis=1))
print("=====================")
print(np.max(stats,axis=0))
print(np.max(stats,axis=1))