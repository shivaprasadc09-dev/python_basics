
num1= int(input("Enter the first number : "))
num2= int(input("Enter the second number : "))
sign = input("+,-,*,/")

if sign == '+':
    result = num1 + num2

elif sign == '-':
    result = num1 - num2 

elif sign == '*':
    result = num1 * num2 

elif sign == '/':
    result = num1/num2 



print(f"the addition of 2 numbers is :{result} ")