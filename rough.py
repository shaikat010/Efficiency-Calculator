import csv
from datetime import date

today = date.today()
print("Today's date:", today)

with open(str(today), 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        task = row

    tasks = task[:-1]
    print(tasks)
