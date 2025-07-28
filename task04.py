import json

name = input("ism kiriting: ")
surname = input("familiya kiriting: ")
age = input("yosh kiriting: ")

new_student = {
    "name": name,
    "surname": surname,
    "age": age
}

with open("students.json", "r") as file:
    students = json.load(file)

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print(f"{name} {surname} qo'shildi!")