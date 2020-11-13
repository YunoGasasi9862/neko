class student:
    school="ABA"

    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3



    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3


    def get_m1(self):
        return self.m1, self.m2, self.m3

    def set_m1(self, value):
        self.m2=value


    @classmethod
    def getSchool(cls):
       return cls.school

    @staticmethod
    def info():
        print("This is the ABC school")







s1=student(88,22,55)
s2=student(99,33,56)
print(s1.avg())
print(s2.avg())


print(s1.get_m1())
print(student.getSchool())


student.info()

