import numpy as np
# from pywin.scintilla.view import PRINTDLGORD

dt=np.dtype([('Name','S'),('age','i1'),('salary','f2')])
a=np.array([("Manivel",12,2500),("Maha",18,1500),("King Maker Ronald Drumphkin",33,600000),("Kishore",45,200000)])
print(a)

print(a[0][2])