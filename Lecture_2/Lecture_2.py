# допустим, нам необходимо считать 10 чисел с клавиатуры

vals = []

vals.append(int(input("Введите 1-е число:\t")))
vals.append(int(input("Введите 2-е число:\t")))
vals.append(int(input("Введите 3-е число:\t")))
vals.append(int(input("Введите 4-е число:\t")))
vals.append(int(input("Введите 5-е число:\t")))
vals.append(int(input("Введите 6-е число:\t")))
vals.append(int(input("Введите 7-е число:\t")))
vals.append(int(input("Введите 8-е число:\t")))
vals.append(int(input("Введите 9-е число:\t")))
vals.append(int(input("Введите 10-е число:\t")))

print("vals:\n", vals)


# что в таком случае делают нормальные люди

vals_2 = []

for i in range(10):
    vals_2.append(input("Введите "+str(i+1)+"-е число:\t"))

print("vals_2:\n", vals_2)


# давайте повозводим в степень

base = int(input("Введите целое число - основание степени:\t"))
exponent = int(input("Введите целое число - показатель степени:\t"))

result = 1
for i in range(exponent):
    result *= base

print(str(base) + "^" + str(exponent) + " =", result)

# как можно в питоне

base_2 = int(input("Введите целое число - основание степени:\t"))
exponent_2 = int(input("Введите целое число - показатель степени:\t"))

print(str(base_2) + "^" + str(exponent_2) + " =", base_2 ** exponent_2)

# как можно делать в других языках - быстрое возведение в степень. Количество операций порядка O(log(N))

def fast_pow(base:int, exponent:int)->int:
    counter = exponent; _base = base; result = 1
    while(counter != 0):
        if counter % 2 == 0:
            counter //= 2
            _base *= _base
        else:
            counter -= 1
            result *= _base
    return result

print(fast_pow(int(input("Введите целое число - основание степени:\t")), int(input("Введите целое число - показатель степени:\t"))))


# функции, значения аргументов по умолчанию и  docstring

def function_1(arg_1, arg_2 = "default_value"):
    "return stringified arg_1 + arg_2, if arg_2 wasn't defined use 'default_value' as default value"
    return str(arg_1) + str(arg_2)

print(function_1("sample_string"), \
      function_1("sample_string_1", "sample_string_2"), \
      sep = "\n")

# *args     **kwargs

def function_2(*args, **kwargs):
    arglist =[]
    argdict = {}
    for arg in args:
        arglist.append(arg)
    for keyword, value in kwargs.items():
        argdict[keyword] = value
    return arglist, argdict

print(function_2(1, 2, 3, 6, 9, 15, anything = None, func = function_1, result = function_1("dd")))


# строки и срезы  # https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html # https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html

sample_string_1 = "sample_string_1"
sample_string_2 = "sample_string_2"

_sum = sample_string_1 + sample_string_2
product = 6 * sample_string_1
_join = "******".join([sample_string_1,sample_string_2])
_replace = _join.replace("sample_", "new-")

print(
    sample_string_1,
    sample_string_2,
    _sum,
    product,
    _join,
    _replace,
    sample_string_1[7:],
    sample_string_2[::-1],
    sample_string_1[7:10],
    sample_string_2[9:6:-1][::-1], 
    sep = '\n'
)