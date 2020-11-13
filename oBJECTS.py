class computer:


    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram


    def meow(self):
        print("config is :", self.cpu, self.ram)






comp1=computer("Intel core i7", 16)
comp2=computer("Ryzen", 32)

comp1.meow()
comp2.meow()