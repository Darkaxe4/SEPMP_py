a = [1, 1, 2]

n = int(input())

for i in range(3, n+1):
    if i % 2 == 0:
        a.append(a[i // 2] + a[i // 2 - 1]) 
    else:
        a.append(a[(i - 1) // 2] - a[(i - 1) // 2 - 1]) 

print(a[n])