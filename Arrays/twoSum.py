def twoSum(nums, target):
    target_sum = {}
    for num in nums:
        dif = target - num
        if dif in target_sum:
            return [target_sum[dif], num]
        target_sum[num] = num


nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))

def twoSum(nums, target):
    target_sum = {}
    for index, num in enumerate(nums):
        dif = target - num
        if dif in target_sum:
            return [target_sum[dif], index]
        target_sum[num] = index

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))