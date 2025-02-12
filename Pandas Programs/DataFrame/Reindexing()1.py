import numpy as np
import pandas as pd
data1=np.random.randint(4,7,20).reshape(5,4)
print(data1)
print("========="*30)
df=pd.DataFrame(data=data1,columns=["Class1","Class2","Class3","Class4"])
print(df)
print("======="*30)
print(df.index)
print("======="*30)
re_index=df.reindex(index=[0,1,2,4,],columns=["Class1","Class2"])
print(re_index)
