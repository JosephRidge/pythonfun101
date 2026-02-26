"""
Take a string input
Print:
Number of characters
Number of vowels


Check if the string is a palindrome
"""
name = "Amigoes"

# Number of characters
print(len(name))

# Number of vowels -  a,e ,i, o ,u  
def checkIfVowel(value): 
    result = False
    match(value):
        case 'a':
            result = True
        case 'e':
            result = True
        case 'i':
            result = True
        case 'o':
            result = True
        case 'u':
            result = True
        case _:
            result = False
    return result

vowelCount = 0
for char in name:
    if checkIfVowel(char):
        vowelCount +=1
    else:
        pass

print(vowelCount)


word = input("Enetr word")

if word == word[::-1]:
    print("plaindrome")

else:
    print("not palindrom!")



