# Numeric and string expressions
2015
2000 + 3 * 5
((1 + 2) * 3 + 4) * 5 * (6 * 7 + 8 - 9 - 10)
'Hello ' + 'world!'

# Call expressions
max(3 * 3, 2 * 2, 4 * 4)
pow(100, 2)
pow(2, 100)

# Importing and arithmetic with call expressions
from operator import add, mul
add(1, 2)
mul(3, 3)
add(mul(4, 2), add(6, 2))

from math import sqrt
sqrt(169)

# Assignment
x = 5
x + 2
y = 3 * x
y
a, b = 2, 4
a + b
a, b = b, a
a
b

# Function values
# A rose by any other name would smell as sweet
max
max(3, 4)
f = max
f
f(3, 4)
max = 7
f(3, 4)
f(3, max)
f = 2
# max(3, 4)
max = __builtins__.max

# User-defined functions
def square(x):
    return x * x

square(3)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# Name conflicts
def square(square):
    return mul(square, square)
square(4)

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:15]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)
max(words)
max(words, key=len)

# Reversals
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w) > 4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
