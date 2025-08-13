arr = [57,42,45,9,86,79,108]
i = 3
arr1 = [0]*(len(arr) - 1)
for j in range(len(arr1)):
    if j < i:
        arr1[j] = arr[j]
    else:
        arr1[j] = arr[j + 1]
print("New array after deletion:", arr1)
