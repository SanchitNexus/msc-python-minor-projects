# To-Do List Manager

tasks = []

while True:
    print("\n1. View Tasks  2. Add Task  3. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
    elif choice == "2":
        new_task = input("Enter task description: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
