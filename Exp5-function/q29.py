# 29. Write a recursive function to search for an element in a sorted list using binary search.

def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = list(map(int, input("Enter sorted numbers: ").split()))
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")