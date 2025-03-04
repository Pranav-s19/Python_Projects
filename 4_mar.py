print("I Like Pizza!")

# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

first_name = "bro"
print(first_name)    # will print value of variable first_name
print("first_name")  # will print as word first_name 

#----------------------------------------------------------

# Topic f-string: f-strings (formatted string literals)
# Example,

name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.") # Output : My name is Alice and I am 25 years old.
 

city = "Nagpur"
state = "Maharashtra"
print(f"I live in {city},{state}")

#----------------------------------------------------------

# Strings - serise of characters, can be numbers, alphabets, symbols.
#         - Always inside ""

email = "pro123@fake.com"
town = "Nagpur"


# Integers - number value 
#          - NOT written in ""

age = 25
quantity = 3

print(age)
print(f"you are {age} years old")

# Float - contains decimal value

price = 10.99
gpa = 3.2

# Boolean - True or False

is_student = True
for_sale = False

#-------------------------------------------------------------

name = "Bro Code"
age = 35
gpa = 3.2
is_student = True

print(type(age))

#Typecasting - the process of converting a variable from one data type to another eg. str(), int(), float(), bool().
# Example,

age = float(age)
print(age)
print(type(age))

#--------------------------------------------------------------

#input() - A function that prompts the user to enter data Returns the entered data as a string.

name = input("What is your name? : ")
age = int(input("How old are you? : "))

print(f"Hello, {name}")
print(f"You are {age} years old!!")