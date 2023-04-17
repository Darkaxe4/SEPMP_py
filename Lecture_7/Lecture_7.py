# ООП и его основные принципы:
'''
1. Наследование
2. Инкапсуляция
3. Полиморфизм
'''


# основные понятия ООП - классы и экземпляры классов(объекты)

# Если проводить аналогии с реальным миром, класс - шаблон, набор правил, по которому изготавливаются изделия - экземпляры класса(объекты).

class SampleClass:

    # переменные-члены класса называются полями данного класса
    countOfObjects = 0

    def __init__(self):
        '''__init__(self) - метод класса, называемый конструктор (функции-члены класса называются методами данного класса)'''
        self.id = SampleClass.countOfObjects
        SampleClass.countOfObjects += 1
        print(f'Created object with ID: {self.id}')
    
    # перегрузим операторы сравнения

    def __lt__(self, other: object) -> bool:
        return self.id < other.id
    
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id
    
    def __gt__(self, other: object) -> bool:
        return self.id > other.id
    
    def __le__(self, other: object) -> bool:
        return (self < other) or  (self == other)
    
    def __ge__(self, other: object) -> bool:
        return (self > other) or (self == other)
    
    def __ne__(self, __value: object) -> bool:
        return not (self == __value)
    

a, b = (SampleClass() for _ in range(2))

print(a < b, a == b, a == a, a > b, a <= b, a >= b, a != b, a != a)

# Кратко о наследовании

class ParentClass:
    def __init__(self):
        self.initialized = True

    def doSomething(self, *args):
        print(*args)
    

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
    
    def newDoSomething(self, *args):
        sumOfArgs = None
        try:
            args = list(map(int, args))
            sumOfArgs = sum(args)
        finally:
            print(args)
            if not sumOfArgs is None:
                print(sumOfArgs)

A = ParentClass()
A.doSomething('Some text')

B = ChildClass()
B.doSomething('1', '2', '3')
B.newDoSomething('1', '2', '3')

