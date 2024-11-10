class Animal:
    def speak(self):
        return "Animal Speak"
class Dog(Animal):
    def bark(self):
        return "Dog Barks"
class Cat(Animal):
    def meow(self):
        return "Can Meows"
class Pet(Dog,Cat):
    def pet_sound(self):
        return "Pet makes sound"

pet =Pet()
print(pet.speak())
print(pet.bark())
print(pet.meow())
print(pet.pet_sound())