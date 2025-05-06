def calculator(a, b, operation):
    if operation=='+':
            return(a + b)
    elif operation == '-':
            return(a - b)
    elif operation == '*':
            return(a * b)
    elif operation == '/':
        if b==0: 
            print("cannot be divisible")
        else:
            print(a / b)
    elif operation == '%':
        if b==0:
            print("Cannot divide by 0")
        else:
            print(a % b)
    elif operation == '**':
        return(a ** b)
    elif operation == '//':
        if b==0:
            print("Cannot divide by zero")
        else:
            print(a // b)
    else:
        return "invalid operation"
while True:
    num1= float(input("Enter first bumber: "))
    num2= float(input("Enter second number: "))
    operation=input("choose operation (+, -, *, /, %, **, //): ")
    result = calculator(num1, num2, operation)
    print("result = ", result)
    choice=input("Do you want to continue? (yes/no): ").lower()
    if choice == "no":
        print("thanks for using!")
        break