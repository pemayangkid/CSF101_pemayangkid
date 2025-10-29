def linear_search (arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

check_list = [2,1,3,4,5,7,3,1,5,8]
result = linear_search(check_list, 4)
print(f"Linear Search: Index of 4 is {result}")