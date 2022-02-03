import csv
import time
from datetime import date


today = date.today()
print("Today's date:", today)


task_for_day = []
type_task_for_day = []


def task_input():
    task = input("Input the number of tasks: ")
    task = int(task)

    for i in range(task):
        task_for_day.append(input("Write the name of the task"))
        type_task_for_day.append(input("Input type of task: 1 means urgent, 2 means important, 3 means urgent and important"))

    with open(str(today), 'a') as csv_file:
        for task in task_for_day:
            csv_file.write(task)
            csv_file.write(",")


def calculate_day_utility(task_for_day,type_task_for_day):
    no_tasks = len(type_task_for_day)
    ideal_max_score = 3*no_tasks
    score = 0
    for i in type_task_for_day:
        score = score + int(i)

    percentage_score = (score/ideal_max_score)*100
    print("your day utility is " + str(percentage_score) + " percent ")
    return percentage_score


def day_success_rate(date):
    with open(str(date), 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            task = row

        tasks = task[:-1]
        print(tasks)

        task_number = len(tasks)
        no_success_task = 0
        for task in tasks:
            boolean_val = input("Completed Task: " + str(task) + " ? Y-->Yes, N-->No")
            if (boolean_val == "Y"):
                no_success_task = no_success_task + 1

        success_rate = (no_success_task/task_number)*100
        print("Your success rate for " + str(date) + " is " + str(success_rate) + " percent!")






