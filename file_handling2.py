while True:
    action = input("What would you like to do? add/view/delete/exit ")
    if action == "add":
        note = input("Add your note here ")
        with open("note.txt", "a") as file:
            file.write(f"{note}\n")
    
    elif action == "view":
        with open("note.txt", "r") as file:
            notes = [line.strip() for line in file if line.strip()]
            for count, line in enumerate(notes, start=1):
                print(f"{count}. {line}")
    
    elif action == "delete":
        delete_index = int(input("Which task would you like to delete? Enter its number:"))-1
        with open("note.txt", "r") as file:
            notes = [line.strip() for line in file if line.strip()]
            while delete_index >= len(notes):
                delete_index = int(input("That's not within range, try another number:"))-1
            confirmation = input("Are you sure you want to delete this item? (yes/no) ")
            if confirmation == "yes":
                notes.pop(delete_index)
        with open("note.txt", "w") as file:
            for note in notes:
                file.write(f"{note}\n")

    elif action == "exit":
        print("Goodbye")
        break