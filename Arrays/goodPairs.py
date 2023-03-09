def goodPair(nums):
    good_pair = 0
    for index, value in enumerate(nums):
        print(nums[index], nums[value])
    return good_pair


nums = [1,2,3,1,1,3]
print(goodPair(nums))