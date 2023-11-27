# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

n = abs(int(input('Введите число n: ')))
stop = 0
P = 2
for i in range(n):
    if stop != 1:
        P = P ** i
        if P <= n:
            print(P)
            P = 2
        else:
            stop = 1
    else:
        i = n
