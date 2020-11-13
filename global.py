a=10
print(id(a))

def sum():
    a=9

    x=globals()['a']
    print(id(x))
    print("meow", a)

    globals()['a']=15
sum()