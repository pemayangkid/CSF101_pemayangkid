def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicate([2,6,7,4,6,7]))
print(containsDuplicate([3,6,6,4,6,6,6]))
print(containsDuplicate([2,4,5,6,8,101]))