# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def Fib_num(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return Fib_num(num - 1) + Fib_num(num - 2)

for i in range(0,7):
    print(Fib_num(i))
print(Fib_num(7))

def str_fib(n):
    res =""
    for i in range(1, n+1):
        res += f'{Fib_num(i)} '
    return res
print(str_fib(7))