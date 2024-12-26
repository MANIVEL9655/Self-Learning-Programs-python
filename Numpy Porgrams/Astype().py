import numpy as np
from fontTools.misc.psOperators import ps_integer
from scipy import stats as sc
a=np.genfromtxt("NumeriFile.txt", delimiter=',', dtype=int)
print(a)
print("=============================")
print("=======================")
b=a.astype(float)
print(b)
print("=======================")
c=a.astype(str)
print(c)