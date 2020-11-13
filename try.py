a=5
b=2
try:
  print("Resource open")
  print(a/b)
  k=int(input("Enter a number: "))
  print(k)

except ZeroDivisionError:
  print("You can not divide a num by zero")


except ValueError:
  print("Invalid input")

except Exception:
  print("Something went wrong")




finally:
  print("resource close")
print("bye")