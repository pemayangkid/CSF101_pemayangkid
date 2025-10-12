def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
test_list = [3,4,7,6,11,5,4,2]
result = linear_search(test_list, 5)
print(f"Linear Search: Index of 5 is {result}")
