from xml.sax.handler import property_interning_dict

import pandas as pd

s=pd.Series(data= ['a',10,20,'c','d'],index=['b','c','d','e','a'])
print(s)
print(s['a'])
print(s['e'])
print(s['c'])
print(s['a'])
print(s['d'])

