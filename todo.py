tasks = []

def show_menu():
    print("\n--- TODO MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == '2':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
tasks = []

def show_menu():
    print("\n--- TODO MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == '2':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
