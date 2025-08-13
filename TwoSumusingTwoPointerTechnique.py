def find_pair():
    l1 = [12, 23, 43, 56, 10, 14, 22]
    l1.sort()
    print(l1)
    left = 0
    target=66
    right = len(l1) - 1
    while left < right:
        total = l1[left] + l1[right]
        if total == target:
            print("Pair found in positions", left, "and", right)
            return
        elif total < target:
            left += 1
        else:
            right -= 1
    print("Pair not found")
find_pair()
