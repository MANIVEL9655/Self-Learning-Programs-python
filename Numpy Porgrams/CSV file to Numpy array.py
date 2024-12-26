import shlex

from numpy import genfromtxt
my_data= genfromtxt("Banking Customer.csv",dtype='U')
print(my_data)
print(type(my_data))
print(len(my_data))
print("=================")

print(my_data[1])
print(type(my_data[1]))
print("====================")

print(my_data[2:9])
print(type(my_data[2:9]))
print("====================")

a=my_data[0]
print(a)
print(type(a))
print("=====================")

b=my_data
print(b)
print(type(b))
print("=======================")

print(len(b))
print(b[0:4])