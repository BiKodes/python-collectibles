# Print numbers using recursion:
def printnum(lr, ur):
    if lr > ur:
        return
    print(lr)
    printnum(lr + 1, ur); #recursive call

n = int(input("Enter number:"))
printnum(1, n)

# Printing pyramid pattern

def printn(num):
    if (num == 0):
        return
    print("*", end=" ")
    printn(num - 1)                 #recursive call to printn function

def pattern(n, i):
    if (n == 0):
        return
    printn(i)
    print("\n", end="")
    pattern(n - 1, i + 1)           #recursive call to pattern

n = int(input("Enter number:"))
pattern(n, 1)

# Print Fibonacci number:

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0 #base case

    elif n == 1 or n == 2:
        return 1 #base case

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2) #recursive call to the function

n = int(input("Enter number of terms: "))

i = 0
for i in range(n):
    print(Fibonacci(i), end="\t")


# This is a recursive function to find the factorial of an integer:
def factorial(x):
    if x == 1:
        return 1 #base case
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))


# Recursion in with a list:

def sum(list):
    if len(list) == 1:
        return list[0]

    else:
        return list[0] + sum(list[1:])

print(sum([ 5, 8, 4, 8, 10]))

# Factorial with recursion:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

# Count Down to Zero:
def countdown(n):
    print(n)
    if n > 0:
        countdown(n -1)


# Factorial Function:
def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n<= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")

    return  return_value

factorial(4)
