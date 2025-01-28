import pandas as pd
import numpy as np
s=pd.Series([1,2,3,"Name",True,4],index=list("ABCDEF"))
print(s)
print("=====================")
a=s.items()
print(a)
print(next(a))

print("======================")
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(a))