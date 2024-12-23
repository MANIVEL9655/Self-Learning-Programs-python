import numpy as np
a=[1,2,3,4,5]
print(a*5)
print(type(a))
b=np.asarray(a)
print(b*5)
print(type(b))

print(np.log(b))
print(np.log(a))

if type(a)==type(b):
    print("Both are numpy array")
else:
    print("No there are not")

print(np.asarray(a) is a)

print(a is b)