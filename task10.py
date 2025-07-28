import json

with open('students.json') as jsonfile:
    students = json.load(jsonfile)

    sorted_students = sorted(students, key=lambda x: int(x['age']))

    for student in sorted_students:
        print(student)