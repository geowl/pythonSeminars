# Задача №9
# По данному целому неотрицательному n вычислите значение n!
# N! = 1*2*3...*N
# Решить задчу используя цикл while
# input = 5
# output = 120

N = int(input("Введите неотрицательно число: "))
i = 1
if N < 0:
    print("Ошибка! ТРЕБУЕТСЯ НЕОТРИЦАТЕЛЬНОЕ ЗНАЧЕНИЕ!")
    print("Вы ввели число:", N)

elif N>0:
    while N>1:
        i*=N
        N -=1
    print("Факториал от введеного числа =", i)