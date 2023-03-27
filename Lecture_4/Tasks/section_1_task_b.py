stairs = [0, 1, 2, 4]

n = int(input())
for i in range(4, n+1):
    stairs.append(stairs[i-1] + stairs[i-2] + stairs[i-3])

print(stairs[n])