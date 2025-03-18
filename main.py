"""
A Basic calculator
"""

# Prompt the user
print("Enter two numbers and the operator to perfom calculations")

# Enter First Number
num1 = float(input("Enter first number: "))

# Enter Second Number
num2 = float(input("Enter second number: "))

# Enter Operator
operator = input("Enter the operator: ")

# Perform if-else if-else condition on operator
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*" or "x":
    print(num1*num2)
else:
    print("Invalid Operator; Try Again")
