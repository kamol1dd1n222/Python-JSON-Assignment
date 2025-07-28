import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    if int(student['age']) > 20:
        print(f"{student['name']} {student['surname']} - {student['age']}")