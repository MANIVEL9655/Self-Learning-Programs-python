import numpy as np
x= ((1,2,3,"Manivel","Mahalakshmi"),(12,13,14,15,16),(10.4,12.3,13.5,14.5,11.3))
a=np.asarray(x,dtype='str',order="F")
print(a)