def containsDuplicate(nums):
    dupes ={}
    for n in nums:
        if n in dupes:
            return True
        dupes[n] = n
    return False


nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))