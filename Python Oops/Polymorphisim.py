class Employee:
    def info(self):
        name="Loganathan"
        dep="CSE"
        print(name  + "from" + dep)
class Admin:
    def info(self):
        name="kannnan"
        dep="EEE"
        print(name+"from"+dep)
obj1=Employee()
obj2=Admin()
obj1.info()
obj2.info()