def add(x, y):
    print("\nResult is: ", x + y)


def mult(x, y):
    print("\nResult is: ", x * y)


def div(x, y):
    print("\nResult is: ", x / y)


def mod(x, y):
    print("\nResult is: ", x % y)


print("Welcome to my smart calculator, give it a try ->")

active = True

x = 0
y = 0

while active == True:

    choose = int(
        input("\nChoose the operation:\n(1)Addition\n(2)Multiply\n(3)Divide\n(4)Modulo\n(0)End\n\n->"))

    if choose == 1:

        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        add(x, y)

    elif choose == 2:

        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        mult(x, y)

    elif choose == 3:

        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        div(x, y)

    elif choose == 4:

        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        mod(x, y)

    if choose == 0:
        break
