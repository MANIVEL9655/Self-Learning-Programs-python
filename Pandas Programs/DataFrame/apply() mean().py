import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randint(40,120,15).reshape(5,3),columns=["col1","col2","col3"])
print(df)
print("=======================================")
print(df.apply(np.mean,axis=0))
print("=======================================")

print(df.apply(np.min,axis=0))
print("=======================================")

print(df.apply(np.max,axis=0))