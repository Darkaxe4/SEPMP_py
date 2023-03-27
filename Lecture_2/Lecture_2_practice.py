# циклы / вычисление сумм и произведений

# H. Сумма степеней

""" Входные данные
Вводится натуральное число N, которое не превосходит 30.

Выходные данные
Вычислите 1+2+2^2+2^3+…+2^N. """

def Task_H(N:int)->int:
    sum = 0
    cur = 1
    for i in range(N+1):
        sum += cur
        cur *= 2
    return sum
    
def Task_H_alt(N:int)->int:
    first = 1
    multiplier = 2
    return first * (multiplier ** (N + 1) - 1) // (multiplier - 1)


# циклы / Задачи: обработка последовательностей, индуктивные функции

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


# циклы / Задачи на цикл while

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


# типы данных / Тема 2 / Задачи (Python)

def Task_M(s:str)->str:
    return '*'.join([*s])

print(Task_M("Python"))

