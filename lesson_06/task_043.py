# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3
# 2

import random
def create_random_list(num):
    return [random.randint(-10,10) for _ in range(num)]

def find_couple(user_list : list):
    count_of_couple = 0
    for i in set(user_list):
      count_of_couple += user_list.count(i) // 2
    return count_of_couple

len_list = int(input("Длина массива: "))

user_array = create_random_list(len_list)
print(user_array)
find_couple(user_array)
print(find_couple(user_array))