def add(x,y):
    add_res = x + y
    return add_res

def subtract(x,y):
    subtract_res = x - y
    return subtract_res

def multiply(x,y):
    multiply_res = x * y
    return multiply_res

def divide(x,y):
    if y == 0:
        print('We can\'t devide by 0' )
    else:
        divide_res = x + y
    return divide_res

while True:
    print("Welcome to the simple calculator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input('Please enter choice (1/2/3/4): '))
    x = float(input('Please enter the first number: '))
    y = float(input('Please enter the seconde number: '))
    if choice == 1:
        print("Result:",add(x,y))
    elif choice == 2:
        print("Result:",subtract(x,y))
    elif choice == 3:
        print("Result:",multiply(x,y))
    elif choice == 4:
        print("Result:",divide(x,y))
    else:
        print("Invalid input")