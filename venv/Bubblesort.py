def sort(nums):
    for i in range(len(nums)-1,0,-1):     #ascending order
        for j in range(i):
            if nums[j]>nums[j+1]:         #checking position
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp









nums=[4234123,323123124523,45325,23,532,43,213,213,12,321,3,231,32,13,12,312,31,2312,3,3213123,45124,213]
sort(nums)
print(nums)   #wow