import numpy as np
from scipy import stats as sc
student_marksFile = np.genfromtxt("NumeriFile.txt", delimiter=',', skip_header=0,dtype=int)
print(student_marksFile)
print(type(student_marksFile))
print("=========================")
a=student_marksFile.reshape((10,3))
print(a)
print("============================")
print(np.sort(student_marksFile,axis=1))
print("==========================")
print(np.min(student_marksFile))
print(np.max(student_marksFile))


print("MEAN",np.mean(student_marksFile))
print("Median",np.median(student_marksFile))
# print("Mode",np.mode(a, axis=1))
print("Mode of array", np.std(a))