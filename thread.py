from time import sleep
from threading import*

class Hi(Thread):
  def run(self):
      for i in range(8):
        print("HI")
        sleep(1)



class hello(Thread):
    def run(self):
        for i in range(8):
          print("hellow")

          sleep(1)


t1=Hi()
t2=hello()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")