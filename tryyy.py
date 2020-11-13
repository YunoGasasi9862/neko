


try:
  k = int(input("Enter a number: "))
  x= int(input("Enter a second number: "))
  ratio: k/x
  print(ratio)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("You cant divide by Zero")


