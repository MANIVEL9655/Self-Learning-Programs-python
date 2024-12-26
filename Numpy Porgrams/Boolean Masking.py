import numpy as np
from scipy import stats as sc
studenmarksFile = np.genfromtxt("NumeriFile.txt",delimiter=",")
print(studenmarksFile)
print("===================")
print(studenmarksFile>20)
# print(studenmarksFile<20 or studenmarksFile<50)
print("=====================")
valueget=studenmarksFile[studenmarksFile>20]
print(valueget)