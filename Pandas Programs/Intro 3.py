import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df= pd.DataFrame(data=np.arange(10), dtype=int)
df.plot.bar(subplots=True)
plt.show()