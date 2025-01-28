from operator import index

import pandas as pd
data={'One':pd.Series([1,2,3],index=["a","b","c"]),"Two":pd.Series(
    [1,2,3,4],["a","b","c","d"])}
df=pd.DataFrame(data=data)
print(df)
print("=================================")
print(df.iloc[3,0])