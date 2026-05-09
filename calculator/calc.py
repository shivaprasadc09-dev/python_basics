
num1= float(input("Enter the first number : "))
num2= float(input("Enter the second number : "))
operator = input("Enter operator ")

match operator:
    case "+":
        print("Result:", num1+num2)
    case "-":
        print("Result:", num1-num2)
    case "*":
        print("Result:", num1*num2)
    case "/":
        print("Result:", num1/num2)

