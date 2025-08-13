l = [11,22,33,44,55,66,77,88,99,100]
n = 3
length = len(l)
n = n % length
rotated = [0] * length
for i in range(n):
    rotated[i] = l[length-n+i]
for i in range(length - n):
    rotated[n+i] = l[i]
print("Right rotated array:", rotated)
