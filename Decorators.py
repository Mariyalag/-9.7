def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print('Составное')
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print('Составное')
                return result
        print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)













# пример создания простого декоратора
# def null_decorator(func):
#     return func
# def greet():
#     return 'Hello!'
#
# greet = null_decorator(greet)
# print(greet())

# пример 2 - можно использвать синтаксис Python 0 для декорирования функции за один шаг

# def null_decorator(func):
#     return func
# @null_decorator
# def greet():
#     return 'Hello!'
#
# print(greet())

# пример 3  - почему нужно внутри декоратора определить еще одну функцию

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
# @uppercase
# def greet():
#     return 'Hello!'
#
# print(greet())

# пример 4
# import time
# import sys
#
# def time_track(func):
#     def surrogate(*args, **kwargs):
#         started_ad = time.time()
#
#         result = func(*args, **kwargs)
#
#         ended_at = time.time()
#         elapsed = round(ended_at - started_ad, 4)
#         print((f'Функция работала {elapsed} секунд(ы)'))
#         return result
#     return surrogate
#
# @time_track
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#         return len(str(total))
#
# sys.set_int_max_str_digits(100000)
# result = digits(3141, 5926, 2718, 2818)
# print(result)

