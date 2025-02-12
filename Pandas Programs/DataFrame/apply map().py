import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randn(5,3),columns=["col1","col2","col3"])
print(df)
def multi(ele1):
    return ele1 * 100
print("=====================")
print(df.applymap(multi))
print("=====================")
