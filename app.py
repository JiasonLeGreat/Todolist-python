from components import view_task, menu, add_task, delete_task, load_tasks, mark_done


def todo_app():
    tasks = load_tasks()    
    count = 0
    while True:

        if count == 0:
            print("Welcome to you!")
            menu()
            count =+ 15

        else:
            menu()

        choice = input("Choose an option ")
        if choice == '1':
             view_task(tasks)
        elif choice == '2':
             add_task(tasks)
        elif choice == '3':
             mark_done(tasks)
        elif choice == '4':
             delete_task(tasks)
        elif choice == '5':
                print("Goodbye!")
                break
        else:
                print("Invalid option, please type again")

if __name__ == "__main__":
    todo_app()