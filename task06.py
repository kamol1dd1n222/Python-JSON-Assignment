import csv, json

with open('students.json') as jsonfile:
    content = jsonfile.read()
    students = json. loads(content)
with open('students.csv', 'w') as csvfile:
    fieldnames = ['name', 'surname', 'age']
    dict_writer = csv.DictWriter(csvfile, fieldnames)
    dict_writer.writeheader()
    dict_writer.writerows (students)