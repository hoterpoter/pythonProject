"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

# 5! = 1 * 2 * 3 * 4 * 5

num = 10
f = 1

while num > 1:
    f *= num
    num -= 1
print(f)


def factorial(num, f=1):
    if num == 0:
        return f
    return factorial(num - 1, f * num)


print(factorial(5))
