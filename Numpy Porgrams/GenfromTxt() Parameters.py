from numpy import genfromtxt
data = genfromtxt("Banking Customer.csv", dtype=object, delimiter=",", skip_footer=False, skip_header=True)
print(data)
