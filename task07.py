import json

with open('students.json') as jsonfile:
    students = json.load(jsonfile)
    avg = 0
    for i in students:
        avg += int(i['age'])
    u_q = avg / len(students)
    print(u_q) 