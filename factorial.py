# def factorial(n):
#     if n>1:
#         x = n*factorial(n-1)
#     else:
#         x = 1
#     return x
#
# print(factorial(9))

# def factorial(n):
#     print('Enter', n)
#     if n>1:
#         x = n*factorial(n-1)
#     else:
#         x = 1
#     print('Exit', n)
#     return x
# print(factorial(6))

# def fibonacci(n):
#     print('Enter', n)
#     if n==0:
#         x = 0
#     elif n==1:
#         x = 1
#     else:
#         x = fibonacci(n-1) + fibonacci(n-2)
#     print('Exit', n)
#     return x
#
# print(fibonacci(8)) # 21

cache = dict()

def fibonacci(n):
    print('Enter', n)
    if n in cache:
        return cache[n]
    if n==0:
        x = 0
    elif n==1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = x
    print('Exit', n)
    return x

print(fibonacci(8))