def shuffle(nums, n):
    for x in range(1,len(nums)): 
        aux = nums[x]
        nums[x] = nums[n]
        nums[n] = aux
        
    return nums

    # nums = zip(nums[:n], nums[n:])
    # return list(nums)

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, 4))