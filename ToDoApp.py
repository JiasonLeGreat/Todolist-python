def todo_app():
    tasks = []

    while True:
        print("\n === Welcome to your to do list ===")
        print("1. Checklist")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option ").strip()

        if choice == "1":
            if tasks:
             print("Your tasks: ")
             for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            else: 
                 print("No tasks to do")

        elif choice == "2":
            task = input("introduce a task:").strip()
            if task:
                tasks.append(task)
                print(f"{task} has been added to the list.")
            else:
                print("Task cannot be empty")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete")
            else:
             task_n = int(input("Enter the task number to remove: "))
             if 0 < task_n <= len(tasks):
                removed_task = tasks.pop(task_n - 1)
                print(f"{removed_task} has been removed.")

        elif choice == "4":
            print("See you soon!")
            break

        else:
            print("Invalid option")


todo_app()