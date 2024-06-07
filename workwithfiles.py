"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Input your name: ')
            if len(first_name) < 3:
                raise NameError('Your name is too short')
            second_name = input("Your second name: ")
            if len(second_name) < 3:
                raise NameError('Second name is too short')
            phone_number = input('Input phone number: ')
            if len(phone_number) < 5:
                raise NameError('Phone number is too short')
        except NameError as err:
            print(err)
        else:
            flag = True
    return [first_name, second_name, phone_number]

def create_file(file_name):
    # res = []
    with open(file_name, 'w+', encoding='utf-8', newline="") as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
    # standart_write(file_name, res)

def check_existing_data(file_name, new_data): # проверка на существующие записи
    if not exists(file_name):
        return False
    data = read_file(file_name)
    for row in data:
        if row['first_name'] == new_data[0] and row['second_name'] == new_data[1] and row['phone_number'] == new_data[2]:
          return True
    return False

def write_file(file_name):
    user_data = get_info()
    if check_existing_data(file_name, user_data):
        print("These data already exist in the file.")
    res = read_file(file_name) if exists(file_name) else []
    new_obj = {'first_name' : user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)#словари


def remove_row(file_name):
    search = int(input('Input row to delete: '))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Your row is incorrect')


def standart_write(file_name, res):
    with open(file_name, 'w+', encoding='utf-8', newline="") as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)


def copy_row(file_name, file_name2): # Копирование контакта в другой csv файл
    row_num = int(input('Input row number to copy: '))
    source_data = read_file((file_name))
    if row_num <= len(source_data):
        row_to_copy = source_data[row_num - 1]
        dest_data = read_file(file_name2) if exists(file_name2) else []
        dest_data.append(row_to_copy)
        standart_write(file_name2, dest_data)
    else:
        print('The row number is incorrect')


def display_file(file_name): # Добавил удобное чтение файла
    data = read_file(file_name)
    for idx, row in enumerate(data, start=1):
        print(f'Row {idx}:')
        for key, value in row.items():
            print(f" {key}: {value}")
        print()

file_name2 = 'phone2.csv'
file_name = 'phone.csv'
def main():
    while True:
        command = input("Input a command: ")
        if command == "q":
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('File not found')
            display_file(file_name)
            #     continue
            # print(*read_file(file_name))
        elif command == 'd':
            if not exists((file_name)):
                print("file no found")
                continue
            remove_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('File not found')
                continue
            copy_row(file_name, file_name2)


main()
