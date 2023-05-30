"""
Задача No17. Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] 
Output: 6
 
list = [1, 1, 2, 0, -1, 3, 4, 4] 
newList = set(list)
print(len(newList))

input = [1, 1, 2, 0, -1, 3, 4, 4] 
sl = {}
for el in input:
    if el not in sl:
        sl[el] = 1
    else:
        sl[el] += 1
print(sl)

input = [1, 1, 2, 0, -1, 3, 4, 4] 
sl = {}
for el in input:
    sl[el] = sl.get(el, 0) + 1
print(sl)
"""


"""
 Задача No19. Решение в группах
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3 
Output: [4, 5, 1, 2, 3]

index = int(input('Input number you need: '))
numbers = [1, 2, 3, 4, 5]
firstNums = numbers[:index]
secondNums = numbers[index:]
print(secondNums + firstNums)
print(*secondNums, *firstNums)
"""


"""
Задача No21. Решение в группах
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
 
romanNumbers = dict()
romanNumbers = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
                {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
newValue = set()
newList = []

for value in romanNumbers:
    newValue.add(*value.values())
    newList.extend(list(value.values()))

print(newValue)
print(set(newList))
"""


"""
Задача No23. Общее обсуждение
Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, 
больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3] 
Output: 2 (-1 < 5, 2 < 3)

numbers = [0, -1, 5, 2, 3] 
count = 0

for index in range(1, len(numbers)):
    if numbers[index -1] < numbers[index]:
        count += 1
print(count)

numbers = [0, -1, 5, 2, 3] 
count = 0

for index in range(0, len(numbers)- 1):
    if numbers[index] < numbers[index + 1]:
        count += 1
print(count)
 
numbers = [0, -1, 5, 2, 3] 
print(len([i for i in range(len(numbers) - 1) if numbers[i] < numbers[i + 1]]))

numbers = [0, -1, 5, 2, 3] 
count = 0
prev = numbers[0]

for i in numbers:
    if numbers.index(i) == 0:
        continue
    if prev < i:
        count += 1
    prev = i
print(count)


numbers = []
for i in range(5):
    numbers.append(int(input()))
print(numbers)

numbers = [int(input()) for i in range(5)]
print(numbers)
"""

import random

my_list = [1, 2, 3, 4, 5,]
random_element = random.choice(my_list)  # Selects a random element from the list
print(random_element)

random_number = random.randint(1, 10)
print(random_number)

random_numbers = [random.randint(1, 10) for _ in range(10)]
print(random_numbers)

print(sum(x == 3 for x in my_list))