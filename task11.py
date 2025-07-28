import json
import os

FILENAME = "students.json"

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as json_file:
        json.dump([] , json_file, indent=4)
    print(f" {FILENAME} , file yaratildi . ")
else:
    print(f"{FILENAME} mavjud ekan.")

    