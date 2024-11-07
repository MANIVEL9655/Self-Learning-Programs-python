class A():
    def func(self):
        print("the class a activated")
class B(A):
    def func2(self):
        print("The class B activated")
class C(A):
    def func3(self):
        print("The class C activated")
class D(A):
    def func4(self):
        print("The class D activated")
obj1=A()
obj2=B()
obj3=C()
obj4=D()
obj1.func()
obj2.func2()
obj3.func3()
obj4.func4()
