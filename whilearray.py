from array import*

x=array('i',[2,4,5,6,7,8,9])

newArr=array(x.typecode,(i*i for i in x ))
print(newArr)


a=0
while(a<len(newArr)):
    print(newArr[a])
    a+=1