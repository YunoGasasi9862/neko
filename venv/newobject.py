class data:
    def __init__(self):
        self.age=19
        self.name="bilal"

    def update(self):
        self.age=12
        self.name="meow"




student1=data()
student2=data()
student2.update()

student1.age=12


if(student1.age==student2.age):
    print("wow")
else:
    print("no")
print(student1.age)
print(student1.name)
print(student2.age)
print(student2.name)
