class A:
    def __init__(self):
        print("meow")




    def feature1(self):
        print("this is feature 1")


    def feature2(self):
        print("this is feature 2")




class B():
    def __init__(self):
        print("meow2")


    def feature3(self):
        print("this is feature 1")

    def feature4(self):
        print("this is feature 2")




class C(A,B):
     def __init__(self):
        print("Meow3")
        super().__init__()

a1= A()
a1.feature1()
a1.feature2()

a2=C()