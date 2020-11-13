from math import sin

from numpy import*

arr=array([1,2,3,4,5,6])

arr=arr+5


print(arr)


var=array([22,33,44,23,55,20])
x= arr+var
print(x)



arra1=array([2,3,4,5])
print(arra1.sum())
print(sin(arra1))
print(cos(arra1))
print(tanh(arra1))
print(arcsinh(arra1))
print(cumsum(arra1))


print(concatenate([arr,arra1]))


arr=arra1.copy()

arr[2]=44

print(id(arr))
print(id(arra1))
print(arr)
print(arra1)