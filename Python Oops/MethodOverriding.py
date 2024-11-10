class Parent(object):
    def introduce(self):
        print("Hello")
    def print_name(self):
        print("Parent")
class Child(Parent):
    def print_name(self):
        print("Child")
p=Parent
c=Child
p.introduce(None)
p.print_name(self=None)

c.introduce("ABC")
c.print_name(None)
