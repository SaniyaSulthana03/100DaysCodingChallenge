def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged
list1 = [22,41,56,72]
list2 = [81,90,105,120]
print(merge_sorted_lists(list1, list2))
