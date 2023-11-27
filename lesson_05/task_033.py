# # Задача №33. Решение в группах
# # Хакер Василий получил доступ к классному журналу и
# # хочет заменить все свои минимальные оценки на
# # максимальные. Напишите программу, которая
# # заменяет оценки Василия, но наоборот: все
# # максимальные – на минимальные.
# # Input: 5 -> 1 3 3 3 4
# # Output: 1 3 3 3 1
#
import time
# numbers = [1, 3, 3, 3, 4]
# def change_num(numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     for n in range(len(numbers)):
#         if numbers[n]== max_num:
#             numbers[n] = min_num
# change_num(numbers)
# print(*numbers)
vas_marks = [1,3,3,3,4]
start1 = time.time_ns()
res1 = [min(vas_marks) if i == max(vas_marks) else i for i in vas_marks]
time1 = time.time_ns() - start1

start2 = time.time_ns()
def grades_correction(array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return grades_correction(array, i - 1, max_num)
array = [1, 3, 3, 3, 4]
grades_correction(array, len(array)-1, max(array))
time2 = time.time_ns() - start2
# print(*array)

print(time1, time2)