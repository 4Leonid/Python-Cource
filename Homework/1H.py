""" 
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |

// Solution:
number = int(input('Input total number: '))

firstNumber = number // 100
secondNumber = number % 100 // 10
thirdNumber = number % 10
print(f'First number is { firstNumber }')
print(f'First number is { secondNumber }')
print(f'First number is { thirdNumber }')

totalSum = firstNumber + secondNumber + thirdNumber

print(f'Sum of all numbers is { totalSum }')

Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10

// Solution:
totalNumber = int(input('Input total number of peaces: '))
petyaPeaces = totalNumber / 6
seregaPeaces = petyaPeaces
katePeaces = petyaPeaces * 4
print(f'Kate made {katePeaces} peaces')
print(f'Petya made {petyaPeaces} peaces')
print(f'Sergey made {seregaPeaces} peaces')

Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no

// Solution
number = int(input('Input 6-digit number: '))
leftPart = str(number)[:3]
rightPart = str(number)[3:6]

leftOne = int(leftPart[0])
leftTwo = int(leftPart[1])
leftThree = int(leftPart[2])
leftSum = (leftOne + leftTwo + leftThree)

rightFour = int(rightPart[0])
rightFive = int(rightPart[1])
rightSix = int(rightPart[2])
rightSum = (rightFour + rightFive + rightSix)

result = 'lucky' if leftSum == rightSum else 'no lucky'
print(f'The ticket you bought is {result}')


Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

width = int(input('Input width side qty: '))
height = int(input('Input height side qty: '))
check = int(input('Input size you need: '))
square = width * height

result = 'You can' if width * height > square and  ((check % width == 0)) or ((check % height == 0)) else 'You can not'
print(f'{result} get this piece of chocolate')