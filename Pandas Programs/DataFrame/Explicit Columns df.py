import pandas as pd
data=[{"Name":"Ram","AGE":23,"Marks":80},{"Name":"Ram","Marks":70},{"Name":"Ramana","AGE":24,},{"Name":"Ramesh","AGE":34,"Marks":50},{"Name":"Marish","AGE":30,"Marks":40}]
df=pd.DataFrame(data=data,copy=True,columns=["Name","B","Marks",'AGE'])
print(df)