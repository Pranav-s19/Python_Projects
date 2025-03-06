value1 = int(input("Enter first value : "))
value2 = int(input("Enter second value : "))

operator = input("Enter Operator : ")

if operator == "+":
    result = value1 + value2
elif operator == "*":
    result = value1 * value2
elif operator == "-":
    result = value1 - value2
elif operator == "/":
    result = value1 / value2
else :
    result = print("Enter correct operator between, +,-,*,/,")
    

print(f"Your result : {result}")