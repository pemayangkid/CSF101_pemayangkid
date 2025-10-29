def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  
print(twoSum([2, 7, 11, 15], 9)) 
print(twoSum([3, 2, 4], 6))       
