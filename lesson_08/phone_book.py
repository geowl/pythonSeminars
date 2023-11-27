# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def show_all():
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readline()
        print(''.join(data))
 def remove(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
   data = ''
with open(file_name, 'r', encoding='utf-8') as f:
    data = f.readline()
    s = (f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')
    data.remove(s)
with open (file_name, 'w', encoding='utf-8') as f:
    f.writelines(data)
def modify(file_name:str):
# print("Введите данные для поиска:\n")
# last_name = input('Введите фамилию: ')
# first_name = input('Введите имя: ')
# patronymic = input('Введите отчество: ')
# phone_number = input('Введите номер телефона: ')

old_data = find_by_attribute(file_name, True)

print("Введите новые данные:\n")
last_name_ = input('Введите фамилию: ')
first_name_ = input('Введите имя: ')
patronymic_ = input('Введите отчество: ')
phone_number_ = input('Введите номер телефона: ')
data = ""
with open(file_name, 'r',encoding='utf-8') as f:
    data = f.readlines()
i = data.index(old_data)
data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'

with open(file_name, 'w',encoding='utf-8') as f:\
f.writelines(data)

def add_new(file_name : str) -> None:
    """
    Функция принимая имя файла(file_name) в виде строчки
    :param file_name:
    :return:
    """
    # data = input("Введите ФИО и номер телефона через пробел: ")
    last_name = input("Введите фамилию: ")
    first_name = input ("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    # Иванов Петр Сидорович 1234567
    # Петров Иван Сидорович 7654321
    # file_name = 'phone_book.txt'
    # f = open(file_name, 'a', encoding='utf-8')
    # f.close()
    with open(file_name, 'a', encoding = 'utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')
def main():
    file_name = 'phone_book.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить запись')
        print('3 - поиск записи')
        print('4 - удалить запись')
        answer = input("Введите операцию или х для вывода: ")
        if answer == '1':
            show_all()
        elif answer == '2':
            add_new(file_name)
        elif answer == "4":
            remove(file_name)
        elif answer == 'x':
            flag_exit = True


if __name__ == '__main__':
    main()
#     print('123')
#     print(__name__)
# else:
#     print('123')
#     print('отрабатывает else')
#     print(__name__)


