class shape:
    salary=1000
    def calculate_tax(self):
        return self.salary * 0.15
class Square(shape):
    def calculate_tax(self):
        return self.salary + 0.15
s=Square()
print(s.calculate_tax())

sh=shape()
print(sh.calculate_tax())