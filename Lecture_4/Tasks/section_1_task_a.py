# это и следующие задания взяты из раздела "Динамическое программирование" ( https://informatics.msk.ru/course/view.php?id=9 )

# section_1 - https://informatics.msk.ru/course/view.php?id=9#section-1 
# section_2 - https://informatics.msk.ru/course/view.php?id=9#section-2

f_1, f_2 = 1, 1
n = int(input())
if n < 3:
    print(1)
else:
    for i in range(2, n):
        f_n = f_1 + f_2
        f_1 = f_2; f_2 = f_n
    print(f_n)