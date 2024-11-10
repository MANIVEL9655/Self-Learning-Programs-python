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
        super(square,self).__init__(20,50)
        print(self.s)

S= square(23)
a = S.area()
print(a)
print(S.perimeter())