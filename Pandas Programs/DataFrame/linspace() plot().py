from turtledemo.penrose import start

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
y=[10,40,50,60,30,70,80,90]
print(y)
print("==========================================")
x1=np.linspace(start=0,stop=10,endpoint=True,num=8)
print(x1)
print("======================")
x2=np.linspace(start=0, stop=10,endpoint=False,num=8)
print(x2)
print("==============================")
# plt.plot(x1,y,'x
plt.plot(x2,y,'y')
plt.show()