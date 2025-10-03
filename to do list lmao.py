import json
import os
TaskList = []
CompletedTasks = []

filename = "C:/Users/danie/Downloads/Tasks"
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as f:
        Tasks = json.load(f)
else:
    Tasks = {}

while True:
    TaskList = [Tasks[i] for i in sorted(Tasks, key = int)]  #this is a list comprehension
    break

def AddRemove():
    while True:
        a = input( ).strip().lower()
        if a == 'add':
            add_tasks()
            break
        elif a == 'remove':
            remove_tasks()
            break
        else:
            print('Please enter add/remove.')
def add_tasks():
    while True:
        try:
            NewTask = input('Type the new task here: ').strip().lower()
            break
        except:
            print('An error occured. Please try again.')
    TaskList.append(NewTask)
    Tasks.update({f'{TaskList.index(NewTask) + 1}': f'{NewTask}'})
    print(f'Added Task: {NewTask}')
    return TaskList, Tasks
def reindex(Tasks):
    return {str(i+1): task for i, task in enumerate(Tasks.values())}
def remove_tasks():
    while True:
        try:
            removed_task = int(input("Enter the task number you want to remove: ").strip().lower())
            if removed_task>0:
                removed_task = int(removed_task)-1
                break
            else:
                print('The task number is not in the list, try again.')
        except:
            print('An error occured. Please try again')
    print(f'Removed task: {TaskList[removed_task]}')
    TaskList.remove(TaskList[removed_task])
    Tasks.pop("{}".format(removed_task+1))
    reindex(Tasks)
    return TaskList, Tasks

while True:
    x = input('add/remove tasks? (yes/no) ').strip().lower()
    if x == 'no':
        print('To do list:', Tasks)
        with open("Tasks", "w") as f:
            json.dump(Tasks, f)
        break
    elif x == 'yes':
        print(f"Current to do list: {Tasks}")
        print("To add a task, type 'add'.")
        print("To remove a task, type 'remove'.")
        AddRemove()
        Tasks = reindex(Tasks)
        continue
    else:
        print('an error occured; please enter yes or no')