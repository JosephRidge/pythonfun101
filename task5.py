"""
Task 5: Dictionary (10 min)
Create a dictionary called student with:
name
age
marks

Tasks:
Update marks
Add grade
Loop and print all key–value pairs

"""

"""
Create a dictionary called student with:
name
age
marks
"""

student = {
    "name":"Mary Martha",
    "age":12,
    "marks":99.99
}

print(student)
# 
# Update marks
student["marks"] = 90 
print(student)
# Add grade
student["grade"]="A"
print(student)
# Loop and print all key–value pairs
for item in student:
    print(f"{item} : {student[item]}")
