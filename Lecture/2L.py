"""
// Lists creation

list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 4, 5]
print(list_1)
print(*list_1)

// Circle in list
list_1 = [1, 2, 3, 4, 5]
for i in list_1:
    print(i)

print(len(list_1))
print(list_1[4])
print(list_1[-2])

// Append function
list_1 = [1, 5]
print(list_1)
list_1.append(4)
print(list_1)

list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)

// Usefull functions
// Delete last simbol in list
list_1 = [4, 5, 6, 8]
number = list_1.pop()
print(number)
print(list_1.pop())
print(list_1)

// Delete any simbol in list
list_1 = [4, 5, 6, 8]
print(list_1.pop(0))
print(list_1)
print(list_1.pop(1))

// Insert any symbol in any place in list
list_1 = [4, 5, 6, 8]
print(list_1.insert(2, 11))
print(list_1)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1) - 1]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[-5]) # [6]
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1) - 2:]) # [9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6: -18]) # []
print(list_1[0: len(list_1): 6]) # [1, 7]
print(list_1[::6]) # [1, 7]

// Tuple
t = ()
print(type(t))

t = (1, 5, 3)
print(type(t))

numbers = [1, 8, 9]
print(type(numbers))
print(numbers)

numbers = tuple(numbers)
print(type(numbers))
print(numbers)

a = b = 1
a, b = 1, 2

one, two, three = numbers
print(one, two, three)

t = (1, 2, 3, 4, )
print(t[1])

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

t[0] = 2
print(t)

// Dictionary
d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)

print(d['w'])
print(d['q'])

dictionary = {}
dictionary = {'up': '⬆', 'left': '⬅', 'down':'⬇', 'right': '➡️'}
print(dictionary)
del dictionary['left']
print(dictionary)

for item in dictionary:
    print(item)
    print('{}: {}'.format(item, dictionary[item]))

for (k, v) in dictionary.items():
    print(k, v)

print(dictionary.items())

// Sets
q = set()
print(type(q))

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')
colors.add('orange')
print(colors)

colors.remove('red')
colors.discard('red')
colors.remove('blue')
print(colors)

colors.clear()
print(colors)

oneNums = {1, 2, 4, 5, 8}
twoNums = {2, 5, 8, 18, 9}
threeNums = oneNums.copy()
forthNums = oneNums.union(twoNums)
fiveNums = oneNums.intersection(twoNums)
difOne = oneNums.difference(twoNums)
difTwo = twoNums.difference(oneNums)
final = oneNums.union(twoNums).difference(oneNums.intersection(twoNums))

print(oneNums)
print(twoNums)
print(threeNums)
print(forthNums)
print(fiveNums)
print(difOne)
print(difTwo)
print(final)

numbers = {1, 4, 8}
newNumbers = frozenset(numbers)
print(type(newNumbers))
print(newNumbers)

// Creation list different ways
listOne = [i for i in range(1, 101)]
print(listOne)

listOne = [i for i in range(1, 101) if i % 2 == 0]
print(listOne)

listOne = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(listOne)

listOne = [(i, i*2) for i in range(1, 101) if i % 2 == 0]
print(listOne)

listOne = [i*2 for i in range(10) if i % 2 == 0]
print(listOne)
"""
