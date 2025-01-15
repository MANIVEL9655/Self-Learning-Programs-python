import pandas as pd
import numpy as np
data1=np.array(["Karthick","Manivel","Anush","Hariharan","Anandhi","Kamali"])
s= pd.Series(data=data1,dtype=str,index=["AA",'BB','CC','DD','EE','FF'])
print(s)