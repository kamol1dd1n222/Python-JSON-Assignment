import json
with open('students.json', 'r') as file:
    students = json.load(file)
    print(students)
    
for student in students:
    print(f"{student['name']},  -  {student['age']}")