n = int(input())
costs = [0]
costs.extend(map(int, input().split())) 

pathcost = [0] * (n + 1)
pathcost[1:3] = costs[1:3]


for i in range(3, n+1):
    pathcost[i] = min(pathcost[i-1], pathcost[i-2]) + costs[i]

print(pathcost[n])