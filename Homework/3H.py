import random 
"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    3
    -> 1

quantyForList = int(input('Input the how many numbers in list: '))
random_numbers = [random.randint(1, 5) for _ in range(quantyForList)]
print(random_numbers)
number = int(input('Input number from 1 to 5: '))
count = 0

for i in random_numbers:
    if i == number:
        count += 1
print(f'You have {count} times {number} in you list')
"""
"""
Задача 18: 
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
 В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
 1 2 3 4 5  
 6
    -> 5
"""

quantyForList = int(input('Input the how many numbers in list: '))
random_numbers = [random.randint(1, 5) for _ in range(quantyForList)]
print(random_numbers)

number = int(input('Input number you like: '))
numberToCheck = random_numbers[0]


for i in random_numbers:
    if abs(i - number) < numberToCheck:
        numberToCheck = i
print(numberToCheck)

