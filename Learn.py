# def conc(a, b):
#     res = a + b
#     return res
#
#
# res = conc(6, 6)
# print(res)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"Логирование событий в файл"
# import datetime
#
#
# def log_event(message):
#     c_file = "log.txt"
#     time_now = datetime.datetime.now()
#     c_message = f"{time_now} - {message}\n"
#     with open(c_file, 'a') as file:
#         file.write(c_message)
#
#
# log_event("Программа запущена")
###############################################
"Изменение объектов в списке"

# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#
#
# people = [Human("Аня", 35), Human("Борис", 45)]
#
#
# def add_pers(name, age=0):
#     if not any(human.name == name for human in people):
#         people.append(Human(name, age))
#
#
# def inc_age(people):
#     for human in people:
#         human.age += 1
#
#
# add_pers("Oleg", 36)
# inc_age(people)
# for human in people:
#     print(f"{human.name} теперь {human.age} лет.")
##################################################################
# import requests
#
#
# def send_data(url, data):
#     response = requests.post(url, json=data)
#     print(f"Статус: {response.status_code}")
#
#
# data = {"имя": "Иван", "возраст": 30}
# send_data("https://пример.ком/api", data)
######################################################
# def sort_list(list):
#     list.sort()
#
#
# numbers = [3, 1, 4, 1, 5, 9]
# sort_list(numbers)
# print(numbers)  # Выведет [1, 1, 3, 4, 5, 9]
####################################################
'код для записи лога настроек в файл'
# import datetime
#
# config = {}
#
# def log_event(message):
#     c_file = "settings.txt"
#     time_now = datetime.datetime.now()
#     c_message = f"{time_now} - {message}\n"
#     with open(c_file, 'a') as file:
#         file.write(c_message)
#
#
# def set_settings(key, value):
#     config[key] = value
#     with open("settings.txt", "a", encoding="windows-1251") as file:
#         file.write(f"{key}: {value}\n")
#
#
# log_event("Программа запущена")
# set_settings("режим", "тестирование")
# set_settings("уровень_лога", "отладка")
'Примеры функций с return Расчёт факториала:'

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# result = factorial(5)
# print(result)  # Выведет 120

'''Объяснение: Функция принимает получателя, тему и текст email,
 и симулирует отправку email, выводя информацию на экран.'''

# def send_email(recever, tema, text):
#     print(f"Отправка email...\nКому: {recever}\nТема: {tema}\nТекст: {text}")
#
#
# send_email("sensei.lis@yandex.com", "Привет", "Это тестовое сообщение.")

# def calc_words(text):
#     words = text.split()
#     return len(words)
#
#
# res = calc_words("Привет, как дела?")
# print(res)  # Выведет 3
#
# 'функция считает частоту(количество)появления символа в строке'


# def freq_symb(text):
#     freq = {}
#     for symb in text:
#         if symb in freq:
#             freq[symb] += 1
#         else:
#             freq[symb] = 1
#     return freq
#
#
# print()  # Выведет {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

"определение функции декоратора"
# def cust_func(function):
#     def new_function():
#         print("=== Начало ===")
#         function()
#         print("=== Конец ===")
#
#     return new_function
#
#
# @cust_func
# def hello():
#     print("Hello Oleg, you learn decorators")
#
#
# hello()
"Пример 1: Логирование (Logging)"
# def loging(function):
#     def custom(*args, **kwargs):
#         print(f"Вызов функции {function.__name__} с аргументами {args} и {kwargs}")
#         result = function(*args, **kwargs)
#         print(f"Функция {function.__name__} завершена. Результат: {result}")
#         return result
#
#     return custom
#
#
# @loging
# def summa(a, b):
#     return a + b
#
#
# # Использование:
# summa(25, 136)
"Пример 2: Проверка прав доступа (Authorization)"
# def verify_auth(function):
#     def customisation(user, *args, **kwargs):
#         if not user.get('is_admin'):
#             print("Доступ запрещен")
#             return
#         return function(user, *args, **kwargs)
#
#     return customisation
#
#
# @verify_auth
# def sectret_function(user):
#     print("Это секретная информация")
#
#
# Использование:
# user = {'name': 'Alice', 'is_admin': True}
# sectret_function(user)
"Декоратор, который измеряет время выполнения функции"
# import time
#
#
# def time_meas(function):
#     def custom(*args, **kwargs):
#         start = time.time()
#         result = function(*args, **kwargs)
#         end = time.time()
#         print(f"Время выполнения {function.__name__}: {round(end - start)} секунд")
#         return result
#
#     return custom
#
#
# @time_meas
# def slow_function():
#     time.sleep(1)
#     print("Функция завершена")
#
#
# # Использование:
# slow_function()
'Декоратор, который кэширует результаты функции для оптимизации'
# def caching(function):
#     cache = {}
#
#     def custom(*args):
#         if args in cache:
#             return cache[args]
#         result = function(*args)
#         cache[args] = result
#         return result
#
#     return custom
#
#
# @caching
# def calculating(a, b):
#     print("Вычисление...")
#     return a + b
#
#
# # Использование:
# print(calculating(1, 2))
# print(calculating(1, 2))  # Второй вызов должен использовать кэ
# ///////////////////////////////////////////////////////////////
'''
Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя 
используется пробел. Этот набор чисел будет считан в качестве строки.
Как превратить list строк в list чисел ?
'''

# data = '45 23 445 21 767 67 878'.split()
# print(data)
#
# print(list(map(int, data)))

# mat = []
# for i in range(1, 11):
#     mat.append(i)
# print(mat)
# print(list(map(lambda i: i ** 2, mat)))
# print(list(map(lambda i: i ** 3, mat)))

# sort = [10, 20, 30, 40, 50]
# sort.reverse()
# print(sort)

# list1 = [11, 22, 33, 44, 55]
# res = filter(lambda x: x % 2 != 0, list1)
# print(list(res))

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# res = [a + b for a, b in zip(list1, list2)]
# print(res)

# def scaled_items(a, b):
#     c = []
#     for n, m in zip(a, b):
#         c.append(n * m)
#     return sum(c)
#
#
# vect1 = [1, 2, 3, 4]
# vect2 = [5, 6, 7, 8]
# scaled = scaled_items(vect1, vect2)
# print(scaled)

for i in range(3):
    for j in range(3):
        print(i * j, end=" ")
