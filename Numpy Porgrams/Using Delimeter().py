from numpy import genfromtxt
data=genfromtxt("Banking Customer.csv",delimiter=",",dtype='U')
print(data)

print(len(data))
print(type(data))

print("==========================")
print(data[0])
print("==========================")
print(data[0:5])
print("==========================")
a=(data[0:14])
print(a)
print("======================")
print(a[4:9])
print("==========================")
print(data[0:100][4:90])