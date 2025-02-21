import pandas as pd
import numpy as np

def adder(ele1,ele2=3000):
    return ele1+ele2
df=pd.DataFrame(np.random.randint(40,120,15).reshape(5,3),columns=["col1","col2","col3"])
print(df)
print("*"*50)
print(df["col1"].apply(adder,ele2==45))
print(type(df["col1"]))
