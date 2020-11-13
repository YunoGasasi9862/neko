class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def update(self):
        return self.name, self.age



class B(A):
    def __init__(self):
        print("Meow")
        super.__init__()
        



s1=A("Bilal", 9)
print(s1.update())


s2=B()


