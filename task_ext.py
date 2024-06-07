# list_1 = [10, 21, 31, 40, 51, 60, 70, 80, 91]
# # нужно показать четные элементы на нечетных позициях
# for i in range(1, len(list_1), 2):
#     if list_1[i] % 2 == 0:
#         print(list_1[i])
#
#
# last = list_1.pop()
# first = list_1.pop(0)
#
# list_1.insert(0, last)
# list_1.append(first)
#
# print(list_1)
#
#
#
# # a = 1
# # a = 123
# # a[2] = 5
# Здесь все элементы одного типа



# # Преобразование списка строк в строку
# listOfStrings = ['One', 'Two', 'Three', 'Two']
# strOfStrings = tuple(listOfStrings)
# print(strOfStrings)
# print(type(strOfStrings))

# # Преобразование списка чисел в строку
# listOfNumbers = [1, 2, 3, 2]
# strOfNumbers = set(listOfNumbers)
# print(strOfNumbers)
# print(type(strOfNumbers))
#
# helloWorld = ['hello','world','1','2']
# print(list(zip(helloWorld[0::2], helloWorld[1::2])))
#
# # Преобразуем в словарь
# helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))
#
# # Выводим результат на экран
# print(helloWorldDictionary)

# # Эта ваш список
# a = [1, 2, 3, 4, 5]
# # Создаем итератор списка
# i = iter(a)
# # Создаем и выводим на экран словарь
# print(dict(zip(i, i)))
#
# # Добавляем список [4,5] в список `shortList`
# shortList.append([4, 5])
#
# # Используем метод print() для вывода shortList на экран
# print(shortList)
#
# # Расширяем `longerList` при помощи списка [4,5]
# longerList.extend([4, 5])
#
# # Используем метод print() для вывода longerList на экран
# print(longerList)


# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
#
# Функция не должна ничего выводить, только возвращать значение.

# a = 2
# b = 3
# def f(a, b):
#     res = 1
#     for _ in range(b):
#         res *= a
#     return res
# print(f(a, b))
#
# def f_r(a, b, res=1):
#     if b == 0:
#         return res
#     return f_r(a, b-1, res * a)
# print(f(a, b))

# '''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1.
#  Также нельзя использовать циклы.'''
#
# def f_1(a,b):
#     while b != 0:
#         a += 1
#         b -= 1
#     return a
# print(f_1(2, 5))
#
# def f_2(a, b):
#     if b == 0:
#         return a
#     return f_2(a+1, b-1)
# print(f_2(4,5))

a = 7
a *= 8
print(a)