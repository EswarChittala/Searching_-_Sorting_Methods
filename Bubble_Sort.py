def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Track if a swap occurs
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:  # Stop early if no swaps occur
            break

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", numbers)

bubble_sort(numbers)

print("After sorting:", numbers)