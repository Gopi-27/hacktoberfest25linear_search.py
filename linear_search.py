def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # ✅ Proper return value when element not found

print(linear_search([4, 2, 7, 1, 9], 3))  # Output: -1
