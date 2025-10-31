def to_do_list():
    tasks = []
    while True:
        print("1. add task ")
        print("2.remove task")
        print("3.view your tasks")
        print("4.quit")
        choice=input("enter your choice(1/2/3/4):")
        if choice =="1":
            task=input("enter your task:")
            tasks.append(task)
            print("task added successfully")
        elif choice == "2":
            task=input("enter task to remove:")
            if task in tasks:
                tasks.remove(task)
                print("task removed successfully")
            else:
                print("task not found")
        elif choice =="3":
            for task in tasks:
                print("- ",tasks)
        elif choice =="4":
            quit()
        else:
            print("error")
to_do_list()
