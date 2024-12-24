import numpy as np
from Demos.mmapfile_demo import offset

# from Demos.mmapfile_demo import offset
#
# a=np.arange(5)
# print(a)
# print(type(a))
# it=iter(a)
# print(it)
# #
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # # print(next(it))
#
# x=np.fromiter(a,dtype=int, count=3)
# print(x)
# print(type(x))


name="WE LOVE TAMIL"
c=np.fromiter(name,dtype='S1', count=5)
print(c)
print(type(c))