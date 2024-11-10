class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class square(Rectangle):
    def __init__(self,s):
        self.s=s
        super(square,self).__init__(a,s)
        print(self.s)
R=Rectangle(5,6)
a=R.area()
S= square(23)
a = S.area()

print(issubclass(square,Rectangle))
print(isinstance(R,Rectangle))
print(isinstance(R,square))
print(isinstance(S,Rectangle))
