# # Ваня и Петя поспорили, кто быстрее решит
# # следующую задачу: “Задана последовательность
# # неотрицательных целых чисел. Требуется определить
# # значение наибольшего элемента
# # последовательности, которая завершается первым
# # встретившимся нулем (число 0 не входит в
# # последовательность)”. Однако 2 друга оказались не
# # такими смышлеными. Никто из ребят не смог до
# # конца сделать это задание. Они решили так: у кого
# # будет меньше ошибок в коде, тот и выиграл спор. За
# # помощью товарищи обратились к Вам, студентам.
#
# # import random
# # sequence = [random.randint(0,20) for _ in range(10)]
# # print(sequence)
# # max_value = 0
# # found_zero = False
#
# # for num in sequence:
# # if sequence[0] == 0:
# # print("0 находится на 1 месте в последовательности, максимального числа до него нет")
# # found_zero = True
# # break
# # if num == 0:
# # print("Наибольшее значение, завершающееся первым встретившимся нулем:", max_value)
# # found_zero = True
# # break
# # elif num > max_value:
# # max_value = num
#
# # if found_zero == False:
# # print("В последовательности нет нуля")
#
# #Ваня:
# # n = int(input("введите n: "))
# # max_number = n # 1:1
# # while n != 0: #2
# #     n = int(input("введите n: "))
# #     if max_number < n: #2
# #         max_number = n
# # print(max_number)
#
# # Петя:
# #
# # max_number = -1 # 1
# # while n < 0:
# #     n = int(input())
# #     if max_number < n:
# #         n = max_number
# # print(n)
# import time
# import sys
# start = time.perf_counter()
# # print(start)
# res_ = [i for i in range(10000)]
# res_2 = (i for i in range(10))
# # for i in range(10000):
# #     res.append(i*2)
# # # print(res)
# print(time.perf_counter() - start)
# print(sys.getsizeof(res_2))
# print('next: ', next(res_2))
# for j in res_2
#     print(j)
# print('next2: ', next(res_2))