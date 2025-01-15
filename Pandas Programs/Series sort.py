import               pandas      as                           pd
import numpy as np
stud_info = {"NAME":'Manivel',"Subject":'English',"Mark":45,"CLASS MODE":"HYBRID","TUTOR NAME":'MELCOSE'}
s=pd.Series(data=stud_info,index=stud_info)
print(s)
