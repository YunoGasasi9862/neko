class Pycharm:
    def execute(self):
        print("wow")
        print("meow")


class MyEditor():
    def execute(self):
        print("wow")
        print("meow")
        print("Neko neko")


class laptop:

    def code(self, ide):
        ide.execute()


ide=MyEditor()
lp1=laptop()
lp1.code(ide)