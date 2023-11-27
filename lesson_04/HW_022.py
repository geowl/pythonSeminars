# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

list1 = list(map(int, var2.split()))
list2 = list(map(int, var3.split()))

set1 = set(list1)
set2 = set(list2)

Final = sorted(list(set1.intersection(set2)))

for num in Final:
    print(num, end=" ")

# var1_ = set(var1)
# var2_ = set(var2)
# var3_ = set(var3)
# varOutputFirst = var2_.intersection(var1_)
# # varOutputFinal = varOutputFirst.intersection(var3_)
# varOutputFinal = varOutputFirst.intersection(var3_)
# print(' ' .join(varOutputFinal))