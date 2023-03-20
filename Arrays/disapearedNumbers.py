def findDisapearedNumbers(nums):
    # disapeared_nums = []
    # for num in range(1, len(nums)+1):
    #     if num not in nums:
    #         disapeared_nums.append(num)
    # return disapeared_nums   
#time limit exceeded O(n²)

    # disapeared_nums = list(range(1, len(nums)+1))
    # for num in nums:
    #     if num in disapeared_nums:
    #         disapeared_nums.remove(num)
    # return disapeared_nums
# time limit exceeded again aaaaaah O(n²)

    for num in nums:
        index = abs(num) - 1
        nums[index] = -1 * abs(nums[index])
    
    disapeared_nums = []
    for index, value in enumerate(nums):
        if value > 0:
            disapeared_nums.append(index+1)
    return disapeared_nums


nums = [4,3,2,7,8,2,3,1]
print(findDisapearedNumbers(nums))