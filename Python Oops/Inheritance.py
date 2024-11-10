class parent:
    pass
    def method1(self):
        print("manivel")
class child(parent):
    pass
    def method2(self):
        print("MANIVEL")
obj = child()
obj.method1()
obj.method2()