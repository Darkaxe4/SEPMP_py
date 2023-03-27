#section_2 - https://informatics.msk.ru/course/view.php?id=9#section-2

numofseq = [(0, 0), (1, 1)] # [0] - number of "0", [1] - number of "1"

n = int(input())

for i in range(2, n + 1):
    numofseq.append((numofseq[i-1][0] + numofseq[i-1][1], numofseq[i-1][0]))

print(numofseq[n][0] + numofseq[n][1])