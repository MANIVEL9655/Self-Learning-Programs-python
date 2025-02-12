import pandas as pd
import numpy as np
S=pd.Series(["Laptob","Desktop","Tablet"])
print(S)
print("================================")
price={"Laptob":200,"Desktop":400,"Tablet":500}
print(S.map((price)))