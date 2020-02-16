def multiply (x, y):
    return x * y
a = 5
b = 6
operation = multiply
print (operation(a,b))

def add (x ,y):
    return x + y
def do_twice (func, x, y):
    return func(func (x, y), func (x, y))
a = 8
b = 10
print(do_twice(add, a, b))

import random
for i in range(5):
    value = random.randint(1, 6)
print (value)

def func(x):
    res = 0
    for i in range(x):
        res +=i
        return res
print(func(4))



myfile = open('firsr.txt', 'w')
myfile.write("this is my first attempt write to file")
myfile.close()

myfile = open('firsr.txt', 'r')
print(myfile.read())
myfile.close()

try:
    f=open("firsr.txt")
    print(f.read())
finally:
    f.close()

with open("firsr.txt") as f:
    print(f.read())


def some_func():
    print ('hi!')
var = some_func()
print(var)

ages = {"den": 34, "kostya": 28, "marina":29}
print(ages["den"])
ages["young den"] = 25
print(ages.get (34, "not in dict"))

primes = {1:2, 2:3, 4:7, 7:17}
print(primes[primes[4]])

fib = {1:1, 2:1, 3:2, 4:3}
print (fib.get(4,0) + fib.get(7,5))

a = [x*10 for x in range(5, 9)]
print(a)

nums = [4, 5, 6]
msg = "number {0}, {1}, {2} ".format(nums[0], nums[1], nums[2])
print(msg)

print ("{0}{1}{0}".format("abra","cad"))
a = "{x}, {y}".format(x = 1, y = 4)
print (a)
