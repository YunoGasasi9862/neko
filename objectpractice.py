class ageandname:
    def __init__(self, age, name):
     self.age=age
     self.name=name



    def meow(self):
        print("Your name is: ", self.name)

        print("Your age is: ", self.age)




student1=ageandname(7, "bilal")
student2=ageandname(19, "Taha")


student1.meow()
student2.meow()