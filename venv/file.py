f=open("data", "r")

f1=open("abc", "w")
f2=open("716fa64ab92bd88d7e3ef35b0f5ea416.JPG", "rb")    #wow


for i in f2:     #making use of bits in picture file
  print(i)


for data in f:
  f1.write(data)