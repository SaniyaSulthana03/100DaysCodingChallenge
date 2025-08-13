arr = [10,45,20,67,72]
x = 89
y = 3
arr1 = [0] * (len(arr) + 1)
for i in range(len(arr) + 1):
    if i < y:
        arr1[i] = arr[i]
    elif i == y:
        arr1[i] = x
    else:
        arr1[i] = arr[i - 1]
print("New Array is", arr1)
