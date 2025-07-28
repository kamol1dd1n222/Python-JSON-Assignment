import json

with open('students.json') as jsonfile:
    students = json.load(jsonfile)
    resalt = max(students, key=lambda x: int(x['age']) )
    print(resalt)