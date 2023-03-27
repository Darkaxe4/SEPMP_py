n = int(input())

numofseq = [0] * (n + 1)    
numofseq[1:4] = (2, 4, 7)

for i in range(4, n + 1):
    numofseq[i] = numofseq[i - 1] + numofseq[i - 2] + numofseq[i - 3]

print(numofseq[n])