import pandas as pd
import numpy as np
s=pd.Series([1,2,3,"Name",4,True], index=['a','b','c','d','e','f'])
print(s)
print("*"*34)
print(s[1:4])
print(s['b':'e'])