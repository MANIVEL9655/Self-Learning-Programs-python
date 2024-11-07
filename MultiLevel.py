class A:
    def __init__(self, a):
        self.a=a
class B(A):
    def __init__(self,a,b):
        self.b= b
        super(B, self).__init__(a)
class C(B):
    def __init__(self,a,b,c):
        self.c=c
        super(C,self).__init__(a,b)
    def addition(self):
        d=self.a+self.b+self.c
        print(d)
add= C(12,3,4)
add.addition()
