def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x // y

def calculator():
    operations = {

        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    num1 = int(input("Enter first number: "))
    for i in operations:
        print(i)
    print("pick aby operation symbol:")
    operation_symbol = input()
    num2 = int(input("Enter second number: "))
    function_calculator = operations[operation_symbol]
    answer = function_calculator(num1,num2)
    print(f"Answer is: {answer}")

calculator()