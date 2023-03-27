import random
# Рекурсия 

def Fib(n:int) -> int:
    "return n-th fibonacci number"
    if n == 1:
        return 0
    elif n < 4:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
    

# Всегда можно представить в виде цикла

def loopFib(n:int) -> int:
    fibs = [0, 1, 1]
    for i in range(3, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n-1]


# Можно и без списка (см. Lecture_2_practise)

def optiFib(n:int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    first, second = 0,1
    for i in range(2, n):
        cur = first + second
        first, second = second, cur
    return cur

for i in range(1, 10):
    print(Fib(i), loopFib(i), optiFib(i))


# Классическая задача динамического программирования - задача о кузнечике

"""На числовой прямой сидит кузнечик, который может прыгать вправо на одну, две или три единицы. 
Первоначально кузнечик находится в точке с координатой 1. 
Определите количество различных маршрутов кузнечика, приводящих его в точку с координатой n."""

def Hopper(n:int) -> int:
    moves = [0, 1, 1, 2]
    for i in range(4, n+1):
        moves.append(moves[i-1] + moves[i-2] + moves[i-3])
    return moves[n]


"""Пусть кузнечик прыгает на одну или две точки вперед, а за прыжок в каждую точку необходимо заплатить определенную стоимость, 
различную для различных точек. Стоимость прыжка в точку i задается значением price[i] списка price. 
Необходимо найти минимальную стоимость маршрута кузнечика из точки 0 в точку n."""

def weightedHopperRec(price:list, n:int) -> int:
    if n < 2:
        return price[1]
    elif price[n - 1] < price[n - 2]:
        return price[n] + weightedHopperRec(price, n - 1)
    else:
        return price[n] + weightedHopperRec(price, n - 2)


def weightedHopper(price:list, n:int) -> int:
    index = n
    result = price[index]
    while index > 0:
        """ if price[index - 1] < price[index - 2]:
            index = index - 1
            result += price[index]
        else:
            index = index - 2
            result += price[index] """
        index = index - 1 if (price[index - 1] < price[index - 2]) else index - 2
        result += price[index]
    return result

price = [0, 1] + [random.randint(1, 10) for i in range(14)]

print(price)

print(weightedHopper(price, 9), weightedHopperRec(price, 9))

# scope - область видимости переменных

# beatyPrint - реализация шаблона проектирования "декоратор", подробнее см. здесь: https://habr.com/ru/company/wunderfund/blog/657355/

def beautyPrint(targetFunc):

    def innerFunc(*args):
        print(targetFunc.__name__, ":", sep = "", end = "\t")
        print(targetFunc(*args))
    
    return innerFunc



@beautyPrint
def First(a, b):
    c = a + b
    return c

@beautyPrint
def Second(*args):
    for i in range(10):
        c = i
    return c

c = 10

@beautyPrint
def Third(*args):
    return c


@beautyPrint
def Fourth(*args : int):
    c = 0
    for arg in args:
        c += arg
    return c
    
@beautyPrint
def Fifth(inc):
    global c
    c += inc
    return c



First(1, 2)
Second()
Third()
Fourth(1,2,3,4,5)
print(f"c:\t{c}")
Fifth(5)
print(f"c:\t{c}")

