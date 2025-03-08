def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:  # If the element is found, return index
            return i
    return -1  # Element not found

# Example usage
numbers = [10,90,55,20, 30, 40, 50]
key = int(input("Enter key value:"))

result = linear_search(numbers, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
