class Mother:
    Mothername=""
    def mother(self):
        print(self.Mothername)
class Father:
    Fathername=""
    def father(self):
        print(self.Fathername)
class Son(Mother,Father):
    def parents(self):
        print(self.Fathername,self.Mothername)

s1= Son()
s1.Fathername = "Velu"
s1.Mothername = "Radhai"
s1.parents()
s1.father()
s1.mother()
print(type(Mother))