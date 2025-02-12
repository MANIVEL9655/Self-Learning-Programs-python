import pandas as pd

dateRange=pd.date_range(start="12-02-2025",periods=5,freq='min')
print(dateRange)
print(type(dateRange))
dateRange=pd.date_range(start="12-02-2025",periods=5,freq='h')
print(dateRange)
dateRange=pd.date_range(start="12-02-2025",periods=5,freq='s')
print(dateRange)
dateRange=pd.date_range(start="12-02-2025",periods=5,freq='ns')
print(dateRange)
dateRange=pd.date_range(start="12-02-2025",periods=5,freq='ms')
print(dateRange)
