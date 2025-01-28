#CREATION OF SERIES USING DICTIONARY
import pandas as pd
import numpy as np
data = {'Mel':12,"Ajanth":32,"Kayal":34,"RAM":23,"":26}
s=pd.Series(data,index=["ABC","BCD","CDA","DAB","DFA"])
print(s)