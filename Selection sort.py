def sort(nums):
   for i in range(20):
       minpos=i
       for j in range(i, 21):
           if nums[j]< nums[minpos]:
               minpos=j

           temp=nums[i]
           nums[i]=nums[minpos]
           nums[minpos]=temp


mood











nums=[22,33,2312312,5412,34,123,123,12,3,1254,23,5,312,3,1245,123,124,125,12,52,152]
sort(nums)
print(nums)
