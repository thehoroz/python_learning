from datetime import datetime

now = datetime.now().strftime("%d-%m-%y %H:%M:%S:")

with open("daily_log.txt", "a+") as file:
    task = input("What did you do today? ")
    file.write(f"{now} {task}\n")
    file.seek(0)
    print(file.read())