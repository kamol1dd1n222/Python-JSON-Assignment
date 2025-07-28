import json
with open('students.json') as jsonfile:
    students = json.load(jsonfile)
    soni = 0
    for i in students:
        soni+=1
    print(soni)