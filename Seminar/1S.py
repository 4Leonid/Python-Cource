"""
Задача No1. Решение в группах
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

n = int(input('Введите кол-во километров которое проезжает машина за день: '))
m = int(input('Введите длинну маршрута: '))
result = m // n + int(m % n > 0)

print(f'Количество дней = {result}')


Задача No3. Решение в группах
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

classOne = int(input('Number of first class is: '))
classTwo = int(input('Number of second class is: '))
classThree = int(input('Number of third class is: '))

print(classOne // 2)
print(classTwo // 2)
print(classThree // 2)

result = (classOne // 2 + classOne % 2) + (classTwo // 2 + classTwo % 2) + (classThree // 2 + classThree % 2)
print(f'Количество парт: {result}')

Задача No5. Решение в группах
Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
Input: 3 4(ввод на разных строках) Output: 6


vagonOne = int(input('Input first number of vagon: '))
vagonTwo = int(input('Input second number of vagon: '))

result = vagonOne + vagonTwo  - 1

print(f'Total qty of vagons is {result}')

 Задача No7. Решение в группах
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. 
Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
Input: 2016 Output: YES
15 минут

year = int(input('Input the year: '))
if year // 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

Задача No8.  
Есть 3 мальчика разного роста расположите их по росту. 
"""
firstBoy = int(input('Input height of first boy: '))
secondBoy = int(input('Input height of second boy: '))
thirdBoy = int(input('Input height of third boy: '))

if firstBoy < secondBoy:
    firstBoy, secondBoy = secondBoy, firstBoy
if secondBoy < thirdBoy:
    secondBoy, thirdBoy = thirdBoy, secondBoy
if firstBoy < secondBoy:
    firstBoy, secondBoy = secondBoy, firstBoy

print(firstBoy)
print(secondBoy)
print(thirdBoy)