# this single-line comment

name = "John Doe" # this is a variable
# firstName = input() # standard input 
# secondName = input("Enter second name: ")

secondName = 10
secondName = "Mary Peter Jane"   

output =""

"""
Multi-line comment or string
"""




"""
DATA TYPE: 
    - TEXT(strings) type: str
    - NUMBERS(integers, float, complex)
    - LIST(list, tuple, dictionary, sets)
"""

# Numbers: INT -> int()
number = 10 # integer value or 10
output = number
output = type(number) # check the data-type

number =1000000000000 
output = number

numberTwo = 2000
output = numberTwo

# Numbers: FLOAT -> float()
amount = 20.5
output = amount
output = type(amount)

# Numbers: COMPLEX -> complex()
root = -2j
output = root 
output = type(root)


numberTwo = 10
output = type(numberTwo)
output = numberTwo
numberTwo = float(numberTwo)
output = float(numberTwo) # parsing numberTwo variable into a floating point number
output = type(numberTwo)

output = int(numberTwo)
output = type(output)

output =  "120" 
output = type(output)
output = int("120")
output = type(output)
numberThree = 100
output = str(numberThree)
output = type(output)

# Text: STRING -> str()
name = "John Doe"
name = 'Jane Doe'
welcomeMessage = 'It\'s a sunny morning'
welcomeMessage = "It's a sunny morning"

output = welcomeMessage
output = type(welcomeMessage)


# string is a lists of characters
name = "Peter Parker"
output = name[4] # accessing characters sing indexes

#slicing
output = name[1:6]
output = name[1:6:2]
output = name
output = name.upper() # changes to uppercase
output = name.lower() # changes to lowercase
output = name.startswith("b") # checks whether the first element is macthing the target
output = name.split(" ") # splits string using the space as the determinant
output = name
output = name.replace("e", "u")
output = name.replace("u", "e")
output = name.replace("Peter", "Jane")


# Operators & Operands
"""
x + y  = 10 => x and y are operands
+ and = are operators 
 
 - Arithmetic Operators
     subraction(-)
     addition (+)
     division (/)
     multiplication (*)
     floor division (//)
     modulus (%)

 - Boolean Operators
 - Comparison operators
 - bit-wise operators

"""
numberOne = 10
numberTwo = 20

# ARITHMETIC OPERATORS: -,+,**,/,//,%
#  subraction(-)
output = numberOne - numberTwo
#  addition (+)
output = numberOne + numberTwo
#  division (/)
output = numberOne / numberTwo
#  multiplication (*)
output = numberOne * numberTwo
#  power (**)
output = numberOne ** numberTwo
#  floor division (//)' - truncation
output = numberOne // numberTwo
#  modulus (%)
numberOne=10
numberTwo=3
output = numberOne % numberTwo

# operation = input("Enter math problem: ")
# output = eval(operation) # this is not recommended becuse malicious attacks

# LOGIC OPERATORS (and, or, not)
areLightsOn = True # boolean data type
isRaining = False #boolean data types
 


print("================================")
print(output)# standard output
print("================================")
