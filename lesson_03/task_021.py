# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
'''
user_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
result_set = set()
for el in user_list:
    result_set.add(el.values())
print(result_set)
не доработан
'''

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": " S005 "}, {" V ":" S009 "}, {" VIII": " S007 "}]
# print(" S005 ".strip())
list_ = []

for i in dictionary:
    for j in i:
        if i[j] not in list_:
            list_.append(i[j].strip())
print("Вот все уникальные значения которые есть в словаре; ",list_)

user_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
result = set(v.strip() for i in user_list for v in i.values())
print(result)