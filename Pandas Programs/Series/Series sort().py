import               pandas      as                           pd
import numpy as np
stud_info = {"NAME":'Manivel',"Subject":'English',"Mark":45,"CLASS MODE":"HYBRID","TUTOR NAME":'MELCOSE'}
data = sorted(stud_info)
indx=sorted([1,4,3,2,0])
s=pd.Series(data,index=indx)
print(s)
