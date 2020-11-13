from array import*

value=array("i", [22,33,44,566,6546453,4534,543,54,543,543,543,55])
print(value.buffer_info())
print(value.typecode)
value.reverse()
print(value)
print(value[5])
for i in value:
    print(i)
    i+=1
for b in range(len(value)):
    print(b)
    b+=1



newArray=array(value.typecode, (a for a in value))

for e in newArray:
    print(e)