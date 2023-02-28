def isUnique(nums):
    count = 0
    for n in range(len(nums)):
        print(f'count:{count}, n:{n}, num[count]:{nums[count]}')
        if nums[n-1] != nums[n]:
            count = n
        else:
            count = count

        # if nums.count(n) == 1:
            # return n
    return count, nums[count]

#4, 2, 3, 3 , 1 ,2, 2, 1
nums = [4, 2, 3, 3 , 1 ,2, 2, 1]
print(isUnique(nums))