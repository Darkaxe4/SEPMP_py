def Task_O():
    sqr_sum = 0
    sum = 0
    num = 0
    cur = int(input())
    while cur != 0:
        num += 1
        sum += cur
        sqr_sum += cur ** 2
        cur = int(input())
    mean = sum / num
    return ((sqr_sum - 2*mean*sum + num * mean ** 2)/(num - 1)) ** (1/2)

print(Task_O())