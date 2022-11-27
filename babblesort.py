a = [11, 22, 4, 1, 99, 7, 56]
n = len(a)
count = 0
for j in range(n - 1):
    for i in range(n - 1 - j):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            count += 1
print(a)
print(count)
