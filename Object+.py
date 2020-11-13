class more():

    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno

        self.lap=self.laptop


    def info(self):
        return self.name, self.rollno

    def show(self):
        print(self.name, self.rollno)

    class laptop:

        def __init__(self):
            self.brand="HP"
            self.ram="8GB"
            self.capacity="512 GB"



        def show(self):

          return self.brand, self.ram, self.capacity



s1=more("Bilal", 9)
s2=more("wow", 8)


s1.show()
s2.show()

m1=more.laptop()
print(m1.show())




