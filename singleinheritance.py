class parent:
    def func1(self):
        print("The parent class function")
class child(parent):
    def func2(self):
        print("The child class function")
object = child()
object.func2()
object.func1()