words = ['spam', 'ham', 'egg', 'bread']
words.append('coffe')
words.insert(5, 'butter')
print(words)
print('spam' in words)
print('tomato' in words)
print(not 'tomato' in words)
print(not 'spam' in words)
if 'spam' in words:
    print ('power power')

print(" ".join(words))
print(len(words))

print(words.index('spam'))
numbers = list(range(10, 20))
print(range(10) == range(0, 10))
print(numbers)

nmb = list(range (5, 20, 3))
print(nmb[1])


for word in words:
    print(word + '!')

list = [1, 1, 2, 3, 5, 8, 13]
print (list[list[4]])

def my_func():
    print('nmb')
my_func()

def print_double(x):
    print(2 * x)
print_double(3)

def max (x, y):
    if x >= y:
        return x
    else:
        return y
print (max(4,7))
z = max (8, 5)
print (z)

def shortest_string (x, y):
    if len(x) <= len(y):
        return x
    else:
        return y
print (shortest_string(5 ,8))

def add_numbers (x, y):
    total = x + y
    return total
    print ('not')
print (add_numbers(6, 8))