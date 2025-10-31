def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return("cannot divide with zero")
    else:
        return x / y

while True:
    print("select operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    choice = input("select your operation(1/2/3/4/5):")
    if choice =='5':
        print("sucessfully exited")
        break
    number1 = float(input("enter your 1st number"))
    number2 = float(input("enter your 2nd number"))
    if choice == '1':
        print("result:", add(number1, number2))
    elif choice == '2':
        print("result:", subtract(number1, number2))
    elif choice == '3':
        print("result:", multiply(number1, number2))
    elif choice == '4':
        print("result:", divide(number1, number2))

    else:
        print("error")
        
