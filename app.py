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

# type conversion
numberTwo = 10
output = type(numberTwo)
output = numberTwo # variable overriding
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

# string methods
output = name.upper() # changes to uppercase
output = name.lower() # changes to lowercase
output = name.startswith("b") # checks whether the first element is macthing the target
output = name.split(" ") # splits string using the space as the determinant
output = name
output = name.replace("e", "u") # replaces all occurences of the character 'e' with 'u'
output = name.replace("u", "e") # replaces all occurences of the character 'u' with 'e'
output = name.replace("Peter", "Jane")  # replaces all occurences of the word 'Peter' with 'Jane'


"""
Operators & Operands: 

For example given the equation: x + y  = 10. x and y are what we call operands
+ and = are operators. Operators allow you to perform a particular action given operands.

Operators can be grouped into types: 
 
 - Arithmetic Operators
     subraction(-)
     addition (+)
     division (/)
     multiplication (*)
     power (**)
     floor division (//)
     modulus (%)

 - Boolean Operators (and, or, not)
 - Comparison operators (less than, equal to, greater than, less than or equal to, greater than or eq)
 - bit-wise operators (&, | )
 - membership operators 
 - Assignment operators

"""

numberOne = 10
numberTwo = 20

# ARITHMETIC OPERATORS: -,+,**,/,//,%
output = numberOne - numberTwo#  subraction(-)
output = numberOne + numberTwo#  addition (+)
output = numberOne / numberTwo#  division (/)
output = numberOne * numberTwo#  multiplication (*)
output = numberOne ** numberTwo#  power (**)
output = numberOne // numberTwo#  floor division (//)' - truncation
numberOne=10
numberTwo=3
output = numberOne % numberTwo #  modulus (%)

# operation = input("Enter math problem: ")
# output = eval(operation) # this is not recommended because it may allow the user to input dangerous scripts

# BOOLEAN data type => bool()
areLightsOn = True # boolean data type
isRaining = False #boolean data types
 


"""
Comparison operators:
    - less than(<) 
    - equal to(==) 
    - greater than(>)
    - less than or equal to(<=)
    - greater than or eq (>=)
"""
x = 10 
y = 20
output = (x < y) #  less than(<)
output = (x > y) #  greater than(<)
output = type(output)
output = (x >= y) #  greater than or equal to(>=)
output = (x <= y) #  less than or equal to(<=)
output = (x == y) #  equality (==)

# LOGIC OPERATORS (and, or, not)
age =17
year = 2026

output = ((2027 >= year ) and (age <= 18))
output = ((2027 > year ) and (age == 18))

output = not ((2027 >= year ) and (age <= 18))
output = not ((2027 >= year ) or (age <= 18))




print("================================")
print(output)# standard output
print("================================")
