import pandas as pd
data = [["Alex",10],["Mani",20],["Sankar",50],["Roja",34],["Ranjith",40],["Sakthi",55]]
df=pd.DataFrame(data=data,columns=["Name","Age"],index=list('ABCDEF'))
print(df)
print(df.shape)
print(df.ndim)