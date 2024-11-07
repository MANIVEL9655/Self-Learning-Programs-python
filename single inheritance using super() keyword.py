class parent:
    def func1(self):
        print("The parent class function")
class child(parent):
    def func2(self):
        super(child,self).func1()
        print("The child class function")
object = child()
object.func2()
