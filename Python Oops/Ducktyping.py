class Duck:
    def quack(self):
        print("Quaack Quaack Quaack")
    def feathers(self):
        print("The duck has white and grey feathers from Duck Class")
class Person:
    def quack(self):
        print("Tje person class imitates a duck from Person Class")
    def feathers(self):
        print("The person takes a feather from the fround and showsit from Person")
    def name(self):
        print("Jonh sMITH FROM Person class")
def in_the_forest(obj):
    obj.quack()
    obj.feathers()

duck=Duck()
person=Person()

in_the_forest(duck)
in_the_forest(person)