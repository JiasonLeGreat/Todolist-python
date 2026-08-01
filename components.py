import json
import os


TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file. Return an empty list if file doesn't exist."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Handle cases where the file might be corrupted or empty
        return []

def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def menu():
    print("1. Checklist")
    print("2. Add task")
    print("3. Mark task")
    print("4. Delete")
    print("5. Exit")

def view_task(tasks): 
    if not tasks:
        print("No tasks to do")
        return
               
    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅ " if task["done"] else "Pending..."
        print(f"{index} {task['task']} [{status}]")

def add_task(tasks):
    task = input("introduce a task:").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print(f"{task} has been added to the list.")
    else:
        print("Task cannot be empty")

def mark_done(tasks):    
    if not tasks:
        return
    try:
        index = int(input("Which task did you complete? ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Checked!")
        else:
            print("Invalid number ")
    except ValueError:
        print("Please enter a valid number ")

def delete_task(tasks):
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to remove: ")) -1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task deleted: {removed["task"]}")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number")