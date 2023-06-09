#https://informatics.msk.ru/

#изучение языка программирования/ввод-вывод

'''
Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.

Входные данные
В двух строках вводятся два числа (числа целые,положительные, не превышают 1000).

Выходные данные
Выведите ответ на задачу.
'''

def Task_A():
    a = int(input())
    b = int(input())
    return ((a ** 2 + b ** 2) ** (1/2)) 


'''Даны два натуральных числа n и m. Если одно из них делится на другое нацело, выведите 1, иначе выведите любое другое целое число.

При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.'''

def Task_U(a, b):
    mod = (a % b) % a + (b % a) % b + 1
    return mod


'''
Напишите программу, которая считывает два целых числа a и b и выводит наибольшее значение из них. Числа — целые от 1 до 1000.

При решении задачи можно пользоваться только целочисленными арифметическими операциями +, -, *, //, %, =. 
Нельзя пользоваться нелинейными конструкциями: ветвлениями, циклами, функциями вычисления модуля, извлечения квадратного корня.
'''

def Task_V(a, b):
    return (a*(a//b) + b*(b//a))//(b//a+a//b)





