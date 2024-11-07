class P:
    def __init__(self,a,b):
        self.a =a
        self.b = b
        print("Class P", self.a,self.b)
class C(P):
    def __init__(self,c,d,e):
        P(d,e)
        self.c= c
        print("class C",self.c)
obj=C(12,34,4)
obj1=P(12,2)