import pandas as pd

dateRange=pd.date_range(start="12-02-2025", end="12-05-2026",periods=10)
print(dateRange)
print(type(dateRange))