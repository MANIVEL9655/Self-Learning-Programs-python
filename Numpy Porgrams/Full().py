import numpy as np
passmarks=np.full((3,5),"Pass",dtype=object)
# print(passmarks)
passmarks[0][4]="Fail"
print(passmarks)
