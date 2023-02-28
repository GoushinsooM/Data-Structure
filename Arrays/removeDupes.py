def removeDupes(nums):
    left =1
    for right in range(1,len(nums)):
        if nums[right-1] != nums[right]:
            nums[left] = nums[right]
            left+=1
    return left
            


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDupes(nums))