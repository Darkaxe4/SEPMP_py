# https://habr.com/ru/post/191498/
# https://mipt-cs.github.io/python3-2017-2018/labs/lab11.html#id12 


"""Головоломка “Ханойские башни” состоит из трёх стержней, на один из которых нанизано несколько колец. 
Все кольца имеют разный диаметр и расположены снизу вверх по убыванию диаметра.
За один ход разрешается снять верхнее кольцо с любого стержня и переместить его на другой стержень. 
При этом запрещается класть кольцо на кольцо меньшего диаметра.

Вот один из возможных алгоритмов. 
Пронумеруем кольца сверху вниз числами от 1 до n. 
Пусть нам нужно переложить n колец с первого стержня на третий.
"""

def hanoi(start, end, mid, num):
    if num == 1:
        print(start, "->", end)
    else:
        hanoi(start, mid, end, num-1)
        print(start, "->", end)
        hanoi(mid, end, start, num-1)
    
hanoi(1, 3, 2, 4)

# https://informatics.msk.ru/mod/statements/view.php?id=253&chapterid=156#1

"""Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке.

Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода)."""

def without_arrays(index):
    a = input()
    if index == 1:
        print(a, end =" ")
        return
    else:
        without_arrays(index-1)
        print(a, end = " ")


# для самостоятельного решения: https://informatics.msk.ru/mod/statements/view.php?id=649#1 
# https://informatics.msk.ru/course/view.php?id=9#section-1