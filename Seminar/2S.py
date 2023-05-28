"""
Задача No9. Решение в группах
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while
Input: 5
Output: 120

// Solution1:
number = int(input('Введите целое число: ')) 
index = number
factorial = 1 
while index > 1: 
    factorial *= index 
    index -= 1 
print(f'Multiple of numbers from 1 to {number} is {factorial}')

// Solution 2:
number = int(input('Введите целое число: ')) 
index = 1
factorial = 1 
while index <= number: 
    factorial *= index 
    index += 1 
print(f'Multiple of numbers from 1 to {number} is {factorial}')

// Solution 3:
number = int(input('Введите целое число: ')) 
factorial = 1 
for i in range(1, number + 1):
    print(i)
    factorial *= i
print(i, '->', factorial)

Задача No11. Решение в группах
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1.
Input: 5 Output: 6
15 минут
 
// Solution1:
number = int(input('Введите число: ')) 
n1, n2 = 0, 1 
index = 2 
while n2 < number: 
        n1, n2 = n2, n1 + n2 
        index += 1 
if number != n2: 
    index = -1 
print(f'Place of number {number} is {index}')

Задача No13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10 
Output: 2

// Solution1:
number = int(input('Input qty of days: '))
index = 0
maxLength = 0
for i in range(0, number):
    temp = int(input('Input temperature number: '))
    if temp >= 0:
        index += 1
        maxLength = max(maxLength, index)
    else:
        index = 0
print(f'Max warm weather is {maxLength} days')


Задача No15. Общее обсуждение
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9 
Output: 1 9

// Solution1:
number = int(input('Input qty of watermelons: '))
numbers = []

for i in range(number):
    num = int(input('Enter weight: '))
    numbers.append(num)
print(min(numbers), max(numbers))

// Solution2:
"""
number = int(input('Input qty of watermelons: '))
num = int(input('Enter weight: '))
minNum = num
maxNum = num 
for i in range(number -1):
    num = int(input('Enter weight: '))
    minNum = min(num, minNum)
    maxNum = max(num, maxNum)
print(minNum, maxNum)   

"""

"""




