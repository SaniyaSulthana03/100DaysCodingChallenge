arr = [4, 7, 2, 9, 5]
target = 9

for i in range(len(arr)):
    if arr[i] == target:
        print(f"{arr[i]} Found at index {i}")
        break
else:
    print("Not found")

