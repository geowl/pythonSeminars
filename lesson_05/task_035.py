# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
# def prime_num(n):
#     if n <= 1:
#         return "no"
#     for i in range(2, n-1):
#         if n % i == 0:
#             return "no"
#     return "yes"
#
# print(prime_num(-2))
#
# def prime_num(n):
#     if n <= 1:
#         return "no"
#     for i in range(2, n//2):
#         if n % i == 0:
#             return "no"
#     return "yes"
#
# print(prime_num(11))


def prime_num(n, i = None):
    if i is None:
        i = n-1
    if i == 1:
        return 'yes'
    if n <= 1 or n%i == 0:
        return 'no'
    return prime_num(n, i-1)

print(prime_num(3))