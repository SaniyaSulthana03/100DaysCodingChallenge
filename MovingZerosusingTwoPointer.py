l1=[0,23,43,12,65,0,0,76,87]
slow=-1
for fast in range(0,len(l1)):
    if l1[fast] !=0:
        slow+=1
        l1[slow],l1[fast]=l1[fast],l1[slow]
print(l1)


# l1=[0,23,43,12,65,0,0,76,87]
# slow=len(l1)-1
# for fast in range(len(l1)-1,-1,-1):
#     if l1[fast] !=0:
#         l1[slow],l1[fast]=l1[fast],l1[slow]
#         slow-=1
# print(l1)

