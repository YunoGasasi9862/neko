def hello():
    x=float (input("enter a number: "))
    z=x/5
    if(z>1):
        print("WTF")
    else:
        print("WTF (1)")
    return z
hello()



def addition_sub(num1,  num2):
    addition=num1+num2
    subtraction=num1-num2
    return addition, subtraction

result1, result2 =addition_sub(5,67)


print(result1, result2)
