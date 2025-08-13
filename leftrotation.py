l = [11,22,33,44,55,66,77,88,99,100]
n = 5
length = len(l)
n = n % length
rotated = [0] * length
for i in range(length-n):
    rotated[i] = l[n+i]
for i in range(n):
    rotated[length-n+i] = l[i]
print("Left rotated array:", rotated)



