"""
print(5, 8, 6)

//Types
n = 5
print(n)
print(type(n))
n = None
print(n)
print(type(n))
n = 1.89
print(n)
print(type(n))
n = 'Hello, world'
print(n)
print(type(n))

//Quotation
quotation = 'Hello \' world'
print(quotation)

quotation = 'Hello "what to do" world'
print(quotation)

Hiding lines
#print(5)

// How to input different types
a = 10
b = 4.44
c = 'Hello'

print(a, '-', b, '-', c)
print(f'{a} - {b} - {c}')
print("{} - {} - {}".format(a, b, c))

print('Input first line: ')
a = input()
b = input('Input second number: ')

print(a, '+', b, '=', a + b)

c = 5.89
print(c)
print(type(c))

b = int(c)
print(b)
print(type(b))

b = str(c)
print(b + "36")
print(type(b))

c = bool(c)
print(c)
print(type(c))

print('Input first line: ')
a = int(input())
b = int(input('Input second number: '))

print(a, '+', b, '=', a + b)

// Rounding
a = 5.58578
b = 6.54768
print(a * b)
print(round(a * b, 3))

//Interpolation
user = input('Input name: ')
if user == 'Masha':
    print('Yes, its Mashs')
elif user == 'Marina':
    print('I waited for you so long')
elif user == 'Ilnar':
    print('Its top')
else:
    print('Hello,',user,', I dont know you')  

// While
number = 423
sum = 0
while number > 0:
    x = number % 10
    print(x)
    sum += x
    number //= 10
print(sum)

// While condition
index = 0
while index < 5:
    #if index == 3:
    #    break
    index += 1
else:
    print('Plese')
    print('Stop')
print(index) 

// Flag using
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1

// Range and (for in)
r = range(5) # 012345
r = range(2, 5) # 234
r = range(0, -5) # ---
r = range(1, 10, 2) # 13579
r = range(100, 0, -20) # 100 80 60 40 20
for i in r:
    print(i)
for i in range(100, 0, -20):
    print(i)

for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

// Using range in text
text = 'Съешь еще этих Мягких французских булок'
print(len(text))
print('еще' in text)
print(text.lower())
print(text.upper())
print(text.replace('еще', 'EЩЕ'))
print(text[0]) #С
print(text[1]) #ъ
print(text[len(text) -1]) #к
print(text[-1]) #к
print(text[-5]) #б
print(text[:]) # Съешь еще этих Мягких французских булок
print(text[:2]) # Съ
print(text[len(text) - 2:]) # ок
print(text[20:]) # х французских булок
print(text[2:9]) # ешь еще
print(text[6:-18]) # еще этих Мягких
print(text[0:len(text):6]) # Сеикакл
print(text[::6]) # Сеикакл
text = text[2:9] + text[-5] + text[:2] 
print(text) # ешь ещебСъ
"""
