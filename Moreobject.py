class data:
    def __init__(self):
        self.age=20
        self.name="bilal"




    def compare(self, other):
        if(self.age==other.age):
            return True

        else:
            return False






c1=data()
c2=data()

c2.age=20
c2.name="Meow"
if(c1.compare(c2)):
    print("yes")

else:
    print("No")
print(c1.name)
print(c2.name)






