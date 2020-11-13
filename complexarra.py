from array import*

arr=array('i', [])


x=int(input("how many values do you want to insert into the array? "))

i=1
while (i<=x):

    a=int(input("Enter the value :"))
    arr.append(a)
    i=i+1


print(arr)



val=int (input("Enter the search number :"))
k=0

for e in arr:
    if e==val:
        print(k)
        break

    k+=1




print(arr.index(val))



