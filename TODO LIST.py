sehar_tasks = []

def sehar_view_tasks():
    if not sehar_tasks:
        print("\nNo Tasks available:\n")
    else:
        print("\nYour Tasks:")
        for sehar_task_no, sehar_task in enumerate(sehar_tasks, 1):
            print(f"{sehar_task_no}. {sehar_task}")
        print()

def sehar_add_task():
    sehar_task = input("Enter new task: ")
    sehar_tasks.append(sehar_task)
    print("Task added successfully!")

def sehar_update_task():
    sehar_view_tasks()
    if not sehar_tasks:
        return
    try:
        sehar_task_no = int(input("Enter task number to update: "))
        if 1 <= sehar_task_no <= len(sehar_tasks):
            sehar_new_task = input("Enter updated task: ")
            sehar_tasks[sehar_task_no - 1] = sehar_new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def sehar_delete_task():
    sehar_view_tasks()
    if not sehar_tasks:
        return
    try:
        sehar_task_no = int(input("Enter task number to delete: "))
        if 1 <= sehar_task_no <= len(sehar_tasks):
            sehar_removed = sehar_tasks.pop(sehar_task_no - 1)
            print(f"Task '{sehar_removed}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def sehar_main():
    while True:
        print("\nTodo List  (Sehar)")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        sehar_choice = input("Enter your choice: ")

        if sehar_choice == "1":
            sehar_view_tasks()
        elif sehar_choice == "2":
            sehar_add_task()
        elif sehar_choice == "3":
            sehar_update_task()
        elif sehar_choice == "4":
            sehar_delete_task()
        elif sehar_choice == "5":
            print("Goodbye Sehar!")
            break
        else:
            print("Invalid choice. Please try again.")

sehar_main()