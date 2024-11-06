class sample :
    age =25
    def method1(self):
        print("The Method 1 would be called")

    def method2(self,internal,external):
        self.method1()
        result = internal + external
        print(self.age)
        return result
sampleobj = sample()
marks = sampleobj.method2(12,3)
print(marks)