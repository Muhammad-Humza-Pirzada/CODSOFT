num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
opr = input("Enter the operator: ")

def calculator(num1, num2, opr):
    match opr:
        case '+':
            print("Addition: ", num1+num2) 
        case '-':
            print("Subtraction: ", num1-num2)
        case '/':
            print("Division: ", num1/num2)
        case '*':
            print("Multiplication: ", num1*num2)


calculator(num1, num2, opr)
