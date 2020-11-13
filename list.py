def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1

        else:
            odd+=1

    return even, odd

lst=[22,33,44,23123,23,45,6,876,5,78,99,45,22,334,11,2,34]
even, odd= count(lst)

print("Even : {} and Odd: {}".format(even, odd))