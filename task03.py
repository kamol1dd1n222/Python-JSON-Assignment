import json
new_student = {
    "name": "Shahzoda",
    "surname": "Nazarova",
    "age": 22
}

with open("students.json", "r") as file:
    students = json.load(file)

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)