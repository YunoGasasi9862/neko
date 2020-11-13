def update(x):
    print(id(x))
    x=8
    print(x)
    print(id(x))

x=10
print(id(x))
update(x)
print(id(x))