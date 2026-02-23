"""
- input value 1 
- select operator (+,-,/,//,%,*)
- input value 2
- calculate
- print out the value/ solution

"""

def addition(x,y):
    valueSum = x + y
    return valueSum

print("============================================")
valueOne = input("Enter the first operand: ")
valueTwo = input("Enter the second operand: ")

operatorChoice = input(
"""
Kindly input the number of the operation you want: \n
 1. addition(+)
 2. subtraction(-)
 3. multiplication(*)
 4. division(/)
 5. power(**)
 6. floor division(divsion without decimals //)
 
""")
output = "" # global variable
operatorChoice = int(operatorChoice)
valueOne = int(valueOne)
valueTwo = int(valueTwo)


if (operatorChoice == 1):
    output = addition(valueOne, valueTwo)
elif (operatorChoice == 2):
    output = valueOne - valueTwo
elif (operatorChoice == 3):
    output = valueOne * valueTwo
elif (operatorChoice == 4):
    output = valueOne / valueTwo
elif (operatorChoice == 5):
    output = valueOne ** valueTwo
elif (operatorChoice == 6):
    output = valueOne // valueTwo
else: 
    output ="wrong selection!"

# incase you chooose a match 
match(operatorChoice):
    case 1 :
        output = valueOne + valueTwo
    case 2:
        output = valueOne - valueTwo
    case 3 :
        output = valueOne * valueTwo
    case 4:
        output = valueOne / valueTwo
    case 5:
        output = valueOne ** valueTwo
    case 6:
        output = valueOne // valueTwo
    case _:
        output = "invalid!"


print("*****************************")
print(output)
print("*****************************")

print("============================================")
