import pandas as pd
import numpy as np
s=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s)
print(s['a'])
print(s['b'])
idx=['a','b','c']
print(s[idx])