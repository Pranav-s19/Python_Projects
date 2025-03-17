temp = int(input("what is temprature : "))
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# logical operators = evaluate multiple conditions(or, and, not)
#                   or = at least one condition must be true
#                   and = both conditions must be true
#                   not = inverts the condition (not False, not True)

temp = int(input("what is temprature : "))
is_raining = True

if temp > 35 or temp < 0 and is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")