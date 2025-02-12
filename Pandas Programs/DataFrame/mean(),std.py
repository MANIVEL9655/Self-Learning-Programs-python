import numpy as np
import pandas as pd
salary=[12000,12500,40000,50000,60000]
df= pd.DataFrame(data=salary)
print("Mean",df.mean())
print("Standard Deviation",df.std())
print("=====================================")
salary1=[2000,3000,4000,5000,7000]
df2=pd.DataFrame(data=salary1)
print("Mean",df2.mean())
print("Standard Deviation",df2.std())
