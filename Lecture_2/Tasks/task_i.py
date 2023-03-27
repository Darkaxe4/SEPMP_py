def Task_I(N:int)->int:
    prev, prevprev = 1, 1
    cur = 2
    num = 3
    while cur < N:
        prevprev, prev = prev, cur
        cur = prevprev + prev
        num += 1
    if N == cur:
        return num
    return -1

print(Task_I(int(input())))