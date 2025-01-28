import pandas as pd
import numpy as np
from fontTools.subset import prune_hints

bankcustomernames = ["Rani","Kokila","Kannan","Miraseh","Anandhan"]
s=pd.Series(data=bankcustomernames)
upper = s.str.upper()
print(upper)
print("=====================================")
print(s.str.split("M"))
print("=====================================")
print(s.str.endswith('n'))
print("=====================================")
for item in s:
    if item.startswith('R'):
        print(item)
