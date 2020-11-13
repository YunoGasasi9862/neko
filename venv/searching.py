list=[22,33,44,2,52,55622,563,55]
n=22
pos=-1

def search(list, n):      #self-declared method
   i=0
   while i<len(list):    #compares i to the length of the list
      if(list[i]==n):    #i acts here as position (2 value in list)
        globals()['pos'] =i   #changing the value of the global variable


        return True
      i=i+1




   return False

if search(list, n):
    print("Found at: ", pos)

else:
    print("Not found")

