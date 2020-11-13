class IT():
    def __init__(self, course, age, name, credit, gpa):
        self.course=course
        self.age=age
        self.name=name
        self.credit=credit
        self.gpa=gpa


    def data(self):
        print("Your course is: ", self.course)
        print("Your age is: ", self.age)
        print("Your name is: ", self.name)
        print("Your credit is: ", self.credit)
        print("Your gpa is: ", self.gpa)




student1=IT("Engineering", 19, "Bilal", 77,3.7)




student1.data()


