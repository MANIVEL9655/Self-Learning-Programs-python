class shape:
    salary=1000
    def calculate_tax(self):
        return self.salary * 0.15
class Square(shape):
    def calculate_tax(self):
        yield self.salary + 0.15
        yield shape.calculate_tax(self)+266
s=Square()
b=s.calculate_tax()
print(b)
print(next(b))
print(next(b))