"""
Найдите сумму цифр трехзначеного числа
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
Num = int(input("Введите трехзначное число: "))
First_Num = Num//100
Second_Num = Num // 10 % 10
Third_Num = Num % 10

res = First_Num + Second_Num + Third_Num
print(First_Num)
print(Second_Num)
print(Third_Num)
print(res)