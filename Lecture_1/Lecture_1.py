#Типы данных в python, синтаксис, ввод-вывод

number_1 = 1
number_2 = 0.1
boolean = True
_tuple = (1, 1, "string")
arr = [1, 1, "string"]
string = "str"
assoc = {"key":"value"}
_set = set([1, 1, 1, 1, 1, 1, 12112112121])
_frozenset = frozenset([1, 1, 1, 1, 1, 1, 12112112121])

# так писать - плохо
def A(a, b):
    if (type(a) == type(b)) == True:
        result = True
    else:
        if (type(a) == type(b)) == False:
            return False
    return result


# так - норм
def comparator(a, b):
    "Compares types of a and b, returns True if equal, else returns False"
    if type(a) == type(b):
        result = True
    else:
        result = False
    return result


# так - лаконично и красиво
def isEqualType(val_1 : object, val_2 : object) -> bool:
    return type(val_1) == type(val_2)



# тестим наши функции и проверяем, равных ли они типов, а также всякие типы посравниваем
output = \
[
    "comparator(comparator, isEqualType):",
    comparator(comparator, isEqualType),
    "isEqualType(comparator, isEqualType):",
    isEqualType(comparator, isEqualType),
    "isEqualType(input('Please, input a string'), string):",
    isEqualType(input("Please, input a string:\t"), string),
    "isEqualType(_tuple, arr), _tuple, arr:",
    isEqualType(_tuple, arr), _tuple, arr,
    "comparator(_set, _frozenset), _set, _frozenset:",
    comparator(_set, _frozenset), _set, _frozenset
]
print(*output, sep = '\n')


print('Всё. Конец')