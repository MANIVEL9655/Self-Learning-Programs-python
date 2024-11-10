class sample_overload:
    def product(self, *args):
        print(args[0]+args[1])
        return args[0]
    def product(self, *args):
        print(args[0]+args[1]+args[2])

s=sample_overload()
s.product(10,20,30)
