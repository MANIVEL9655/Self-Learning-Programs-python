class Car:
    def __init__(self):
        self.price = 2000
        print(self.price)
        print("Car has started")
        print("=============")
    def method1(self):
        print("instance variable from constructor is accessible to all methods of the class", self.price)
c=Car()
c.method1()