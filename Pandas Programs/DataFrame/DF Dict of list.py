import pandas as pd
data={"Name":['Ram','Jack','Juliee','Kokils','Dharshu','Rajesh'],"AGE":[10,34,83,56,77,87],"MARKS":[30,40,50,60,80,90]}
df=pd.DataFrame(data=data,index=list("ABCDEF"),copy=True)
print(df)