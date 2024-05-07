list_1 = [10, 21, 31, 40, 51, 60, 70, 80, 91]
# нужно показать четные элементы на нечетных позициях
for i in range(1, len(list_1), 2):
    if list_1[i] % 2 == 0:
        print(list_1[i])


last = list_1.pop()
first = list_1.pop(0)

list_1.insert(0, last)
list_1.append(first)

print(list_1)



# a = 1
# a = 123
# a[2] = 5
