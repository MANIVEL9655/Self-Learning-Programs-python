class Car:
    color = "white"
    shade = "Snow White"
    weight = 500
    mfgunit = ""

    def method1(self):
        print("able to access objects attribute to method", self.weight)
    def method2(self):
        print("from method 2", self.color)
        print("transmission type ", self.transmission)
Audicar1= Car()
# print(Audicar1.method1())
# print(Audicar1.method2())
print("---------------------------")
Audicar1.color="REDD"
Audicar1.weight =4000
Audicar1.transmission = "AUTO"

print(Audicar1.method1())
print(Audicar1.method2())