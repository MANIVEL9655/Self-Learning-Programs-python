from multipledispatch import dispatch
class sample_overloading:
    @dispatch(int,int,int)
    def add(self,x,y,z):
        return x+y+z

    @dispatch(int,int)
    def add(self,x,y):
        return x*y
s=sample_overloading()
b=s.add(5,6,7)
print("This is from add(), with 3 parameters",b)
a=s.add(5,8)
print("This is from add(),with 2 parameters",a)