class A:
    def show(self):
        print("wow")


class B(A):
    def show(self):
        print("new")


a=B()
b=A()
b.show()
a.show()