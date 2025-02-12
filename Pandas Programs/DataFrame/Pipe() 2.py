import pandas as pd
import numpy as np
from isapi.samples.redirector_with_filter import proxy
from nest_asyncio import apply


def adder(ele1,ele2):
    return ele1+ele2
df=pd.DataFrame(np.random.randint(4,12,15).reshape(5,3),columns=["col1","col2","col3"])
print(df)
print("*"*50)
print(df.pipe(adder,2))
print("*"*50)
se=df.apply(np.mean)
print(se)
print("*"*50)
print(se.pipe(adder,2))
print("*"*50)
print(se.apply(np.mean))