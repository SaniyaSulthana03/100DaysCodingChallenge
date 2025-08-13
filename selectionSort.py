arr = [11,56,81,76,59]

for i in range(len(arr)):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min]:
            min_idx = j
    arr[i], arr[min] = arr[min], arr[i]

print("Sorted array:", arr)
