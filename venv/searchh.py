
pos=-1

def search(list,x):

   l=0
   u=len(list) - 1       # -1 for normal position
                       #bubble sort
   while l<=u:
       mid=(l+u)//2   #// gives integer return
       if list[mid]==x:
           globals()['pos']=mid
           return True
       else:
           if list[mid]<x:
               l=mid+1

           else:
               u=mid-1
   return False


list = [22, 33, 44, 55, 1, 33, 44,444,2323,23123]
x = 22


if(search(list,x)):
    print("Found at", pos)

else:
    print("Not found")

   
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
