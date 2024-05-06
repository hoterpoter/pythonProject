a = 5
while a > 0:
    print(a)
    if a == 3:
        break
    a -= 1
else:
    print("завершение цикла не по прерыванию")

my_str = "fsdfsd"
for let in my_str:
    print(let, end=" ")


i = 0
while i < len(my_str):
    print(my_str[i], end=" ")
    i += 1