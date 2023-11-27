# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

#def reverse_num(n, numbers):
#     if n == 0:
#         return
#     print(numbers[n-1])
#     return reverse_num(n-1, numbers)
# (reverse_num(3, []))

def rec(n):
    if n == 0:
        return ""
    x = int(input(": "))
    return f'{rec(n-1)} {x}'

n = int(input(": "))
print(rec(n))