fibs = [1, 1]
n = int(input())
for i in range(2, n+1):
    fibs.append((fibs[i-1]+fibs[i-2])%10)

print(fibs[n])