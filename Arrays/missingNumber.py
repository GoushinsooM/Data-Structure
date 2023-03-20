def missingNumber(nums):
#     for disapeared_num in range(len(nums)):
#         if disapeared_num+1 not in nums:
#             return disapeared_num+1

#Runtime error: input: [1] output: returning none instead 0 

    # for num in range(len(nums)):
    #     if num not in nums:
    #         return num
#Runtime error: input: [0, 1] output: returning none instead 2 
    all_nums = [num for num in range(len(nums)+1)]
    return sum(all_nums) - sum(nums)


nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

