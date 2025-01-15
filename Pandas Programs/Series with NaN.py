import pandas as pd
import numpy as np
data1= {'a':10,'b':20,'c':30,'d':40,'e':50}
s=pd.Series(data=data1,index=['b','c','d','e','f','a'])
print(s)