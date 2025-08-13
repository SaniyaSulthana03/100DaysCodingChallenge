arr = [98,78,34,23,99]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap if the element is greater than the next
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
