class Car:
    def  method1(self,color,weight):
        print("Able to access objects attributes to method",color)
        print("Weight of the car is ", weight)
Audicar=Car()
print(Audicar.method1("red",234))
Audicar.color = "Yellow"
Audicar.weight =455
Audicar.method1(Audicar.color,Audicar.weight)
print(type(Audicar.weight))
print(type(Audicar.color))
print("__________________")
print("Classes Objects Hash id", hash(Audicar))
print("Hash for the objects attribute color", hash(Audicar.color))
print("Hash id of the object attribute weight", hash(Audicar.weight))
print(type(Audicar))

print("____________________")
print(Audicar.weight)
print(Audicar.color)

a= vars(Audicar)
print(a)
