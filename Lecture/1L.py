"""
n = 5
print(n)
print(type(n))

n = None
print(n)
print(type(n))

n = 'fdd'
print(n)
print(type(n))

n = 'fd\'dfdf'
print(n)


a = 4
b = 4.44
c = 'hello'
print(a, b, c)
print(a, '-' , b, '-', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a, b, c))

// 
print('Input first number: ')
a = input()
print(a)

b = input('Input second number: ')

print(a, '+', b, '=', a + b)

print('Input first number: ')
a = int(input())

b = int(input('Input second number: '))

print(a, '+', b, '=', a + b)


c = 5.89
print(c)
print(type(c))
c = str(c)
print(c + '89')
print(type(c))

// Rounding
a = 5.8989
b = 6.5544
print(round(a * b, 3))

// elif
username = input('Input name: ')
if username == 'Masha':
    print('Yes, it is Masha')
elif username == 'Marina':
    print('I waited for you, Marina')
elif username == 'Ilnar':
    print('Ilnar is top)')
else:
    print('Hello, ', username)

// Cycle
i = 0
while i < 5:
    i += 1
else:
    print('Please')
    print('Stop')
print(i)

// flag
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

// for cycle
a = 'qwerty'
for i in a :
    print(i)

// range
line = ''
for i in range(5):
    line = ''
    for j in range(5):
        line += '*'
    print(line)

// Text manager
text = 'Eat more these soft french bread'
print(len(text))
print(text.lower())
print(text.upper())
print(text.replace('more', 'MORE'))


text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок 
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких 
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
   
text = text[2:9] + text[-5] + text[:2]
print(text)
"""