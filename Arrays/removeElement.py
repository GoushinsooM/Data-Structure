def removeElements(nums, val):
    count = 0
    for actual in range(len(nums)):
        if nums[actual] != val:
            nums[count] = nums[actual]
            count +=1
    return count




nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElements(nums, val))