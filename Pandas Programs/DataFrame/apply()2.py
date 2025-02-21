import pandas as pd
import numpy as np

def adder(ele1,marks,grade):
    return ele1+marks+grade
    return marks+grade
df=pd.DataFrame(np.random.randint(40,120,15).reshape(5,3),columns=["col1","col2","col3"])
print(df)
print("*"*50)
print(df.apply(adder,args=(100,200)))
print(type(df["col1"]))
#sfjsgmb