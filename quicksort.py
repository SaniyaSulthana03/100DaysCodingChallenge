def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    equal = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return quick_sort(left) + equal + quick_sort(right)

arr = [10,7,81,72,89,19]
sorted_arr = quick_sort(arr)
print(sorted_arr)
