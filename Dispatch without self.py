from multipledispatch import dispatch
class sample_overloading:
    @dispatch(int,int)
    def add(x,y):
        return x+y
    @dispatch(object,object)
    def add(x,y):
        return x+y
s = sample_overloading()
a=s.add(12,3)
b=s.add("Tamil","Tamil Nadu")
print(a)
print(b)


