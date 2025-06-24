to_do_list = []
while True:
    action = input("What would you like to do? (add/view/done/exit):")

    if action == "add":
        task = input("Which task would you like to add? ")
        to_do_list.append(task)
        with open("todo.txt", "w") as file:
            for count, value in enumerate(to_do_list, start=1):
                file.write(f"{count} {value}\n")

    elif action == "view":
        with open("todo.txt", "r") as file:
            print(file.read())

    elif action == "done":
        index = int(input("Enter task number to mark as done: ")) -1
        done_task = to_do_list[index]
        print(done_task)
        with open("done.txt", "a") as file:
            file.write(f"{done_task}\n")
        to_do_list.pop(index)
        with open("todo.txt", "w") as file:
            for count, value in enumerate(to_do_list, start=1):
                file.write(f"{count} {value}\n")
                
    elif action == "exit":
        print("Goodbye!")
        break
