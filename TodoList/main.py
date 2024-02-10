
to_do_list = []

while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete/Remove Task")
    print("4. Exit")

    choice = input("Select an option (1/2/3/4)\n")

    if choice == "1":
        task = input("Enter the task to add.\n")
        to_do_list.append(task)
        print("Task added.")
    elif choice == "2":
        print("To-Do List:")
        for index,task in enumerate(to_do_list):
            print(f"{index+1}. {task}")
    elif choice == "3":
        if not to_do_list:
            print("List is empty.")
        else:
            print("To-Do List:")
            for index,task in enumerate(to_do_list):
                print(f"{index+1}. {task}")
            
            task = int(input("Enter the index of task.\n"))

            if 1<= task <= len(to_do_list):
                completed_task = to_do_list.pop(task - 1)
                print(f"{completed_task} is completed/removed.")
            else:
                print("Invalid index of task.")
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")


