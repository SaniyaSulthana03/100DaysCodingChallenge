arr = [10, 20, 5, 8, 30, 25]

biggest = second_biggest = float('-inf')

for num in arr:
    if num > biggest:
        second_biggest = biggest
        biggest = num
    elif num > second_biggest and num != biggest:
        second_biggest = num

print( second_biggest)
