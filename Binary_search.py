def binary_search(arr, key):
    low= 0 
    high=len(arr) - 1

    while low <= high:
        mid = low + high // 2

        if arr[mid] == key:
            return mid  # Element found

        if arr[mid] < key:
            low = mid + 1  # Search in high half
        else:
            high = mid - 1  # Search in low half

    return -1  # Element not found

# Example usage
numbers = [10, 20, 30, 40, 50]
key = int(input("Enter key valuea:"))

result = binary_search(numbers, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
