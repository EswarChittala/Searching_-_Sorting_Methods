def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Take the current element
        j = i - 1

        # Shift elements to the right to create space for key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert key at the correct position

# Example usage
numbers = [12, 11, 13, 5, 6]
print("Before sorting:", numbers)

insertion_sort(numbers)

print("After sorting:", numbers)