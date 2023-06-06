"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 
A = 2; B = 3 -> 8

def number_to_power(number, power):
    if power == 0:
        return 1
    else:
        return number * number_to_power(number, power - 1)
    
print(number_to_power(5, 3))
 
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
   22 4

   def get_sum(a: int, b: int) -> int:
    if a == 0:
        if b == 0:
            return 0
        return get_sum(a, b - 1) + 1
    return get_sum(a - 1, b) + 1

print(get_sum(3, 2))

def get_sum(a: int, b: int) -> int:
    if b == 0:
        return a
    return get_sum(a + 1, b - 1)
"""

def summ(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    return 2 + summ(a - 1, b - 1)

print(summ(3, 8))


