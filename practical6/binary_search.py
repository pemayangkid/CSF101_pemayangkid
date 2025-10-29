def binary_search(arr,target):
    left, right = 0,len(arr) - 1

    while left <= right :
        mid = (left + right)  // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return - 1

check_list = [2,3,1,7,6,4,3,8,9,5]
check_list_sorted = sorted(check_list)
result = binary_search(check_list_sorted, 7)
print(f"Binary Search: Index of 7 in sorted list is {result}")