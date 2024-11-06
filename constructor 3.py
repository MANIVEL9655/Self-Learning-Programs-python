class person(object):
    species = "Homo Sapiens"
    def __init__(self,name,age):
        self.myname = name
        self.yourage= age
        grade  = "First"
        print(self.myname,self.yourage)
    def method1(self,name):
        print("This instance var is frpm constructor", self.myname)
        myname = name
        myname = myname + "Best"

P=person("Linda",23)
P.method1("Aswarthy")