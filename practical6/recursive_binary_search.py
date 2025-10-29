def binary_search_recursive(arr, target, left, right):
    if left > right :
        return -1

    mid = (left + right) // 2
    if arr [mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

check_list_sorted = sorted([2,1,3,4,5,7,3,1,5,8])
result = binary_search_recursive(check_list_sorted, 7, 2, len(check_list_sorted))
print(f"Recursive Binary Seacrch: Index of 7 in sorted list is {result}")