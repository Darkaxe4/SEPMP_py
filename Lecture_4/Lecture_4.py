 # Классы и ООП

# init - конструктор, вызывается при создании нового экземпляра класса

class sample_class:
    global_var = None
    def __init__(self):
        self.first = sample_class.global_var
        self.second = 2
        
    
    def sample_func(self, *args):
        for arg in args:
            print(arg)
        return 0
    
a = sample_class()
sample_class.global_var = 1
aa = sample_class()
print(a.first, aa.first)

a.sample_func(a.first, a.second)

print(a)

# __str__ - можно также переопределить некоторые другие встроенные методы, например строковое представление объекта класса

class strable:
    def __init__(self):
        return
    
    def __str__(self) -> str:
        return "This is a sample stringable class"
    
def f(self)->str:
    return "sample override"

b = strable()


print(b)