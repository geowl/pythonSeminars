# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
import os

n = int(input("Введите число: "))
a = 1
b = 0
i = 1
fibonacci = 0
count = 0

while i <= n+1:
    # print(fibonacci, end = " ")
    if fibonacci == n:
        # print(f"\n Число {n} п осчету на {i} месте")
        break
    fibonacci = a + b
    a = b
    b = fibonacci
    i+=1
else:
    i = -1
print(i)

