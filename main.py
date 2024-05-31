# NoneType Example
# Demonstrates the use of None in Python, representing the absence of a value.
a = None
print(a)  # Output: None

# Math Module Example
# Demonstrates importing the math module and printing the value of pi.
import math as m
print(m.pi)  # Output: 3.141592653589793

# Identity Operators Example
# Demonstrates the use of identity operators 'is' and 'is not'.
x = 10
print(x is 20)  # Output: False
print(x is 10)  # Output: True

# Membership Operators Example
# Demonstrates the use of membership operators 'in' and 'not in'.
str = "Hello World"
print("Hello" in str)  # Output: True
print("Hello" not in str)  # Output: False

# Min and Max Functions Example
# Demonstrates finding the minimum and maximum values in a list.
list = [1, 2, 3, 4, 5]
print(min(list))  # Output: 1
print(max(list))  # Output: 5

# Looping through Lists Example
# Demonstrates iterating over a list and using the range function.
for i in list:
    print(i)

print(list)  # Output: [1, 2, 3, 4, 5]

for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Default Argument in Functions Example
# Demonstrates using default arguments in a function.
def showInfo(name="abc", email="abc@gmail.com"):
    print("Name: ", name)
    print("Email: ", email)
    
showInfo("xyz", "xyz@gmail.com")  # Output: Name: xyz, Email: xyz@gmail.com

# Arbitrary Argument Lists Example
# Demonstrates a function that accepts an arbitrary number of arguments (*args).
def arbArg(*args):
    for i in args:
        print(i)
    
    print(args)  # Output: (1, 2, 3, 4, 5)
    
arbArg(1, 2, 3, 4, 5)

# Arbitrary Keyword Arguments Example
# Demonstrates a function that accepts an arbitrary number of keyword arguments (**kwargs).
def keyArg(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
keyArg(a=1, b=2, c=3)  # Output: a 1, b 2, c 3


# Lambda Function Example
# Demonstrates using lambda functions to create anonymous functions.
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5



# mutable and immutable objects
# Demonstrates the difference between mutable and immutable objects.
# Immutable objects: int, float, str, tuple
# Mutable objects: list, dict, set

def func1(x):
    x = x + 1

a=5

func1(a)
print(a)  # Output: 5

func2= lambda x: x.append(11111)

b=[1,2,3,4,5]
func2(b)
print(b)  # Output: [1, 2, 3, 4, 5, 11111]
