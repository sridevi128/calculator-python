tasks = []
while True:
    print("\n--- To-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
           print("No tasks available.")
        else:
           print("\nyour Tasks:")
           for i, task in enumerate(tasks,1):
               print(f"{i}.{task}")
    elif choice =="3":
        if len(tasks) == 0:
           print("No tasks to delete.")
        else:
          for i,task in enumerate(tasks, 1):
             print(f"{i}.{task}")
        num = int(input("enter task number to delete:"))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            print(f" '{deleted} ' deleted successfully!")
        else: 
            print("Invalid task number.")
    elif choice == "4":
         print("Thank you for sing To-Do APP!")
         break
    else:
        print("Invalid choice.please try again")
     