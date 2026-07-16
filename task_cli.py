
task = []

try:
    with open("task.txt", "r") as file:
        for line in file:
            task.append(line.strip())

except FileNotFoundError:
    pass

while True:
        Option= int(input("""Option 1: view task \n option 2: Add Task \n option 3: Quit"""))

        if Option == 1:
            print("... Viewing task ....")

            if task == []:
                print("there is no task yet!!")

            else:
                for i in task:
                    print(i)

        elif Option == 2:
            print("... Adding Task ....")
            new_task = input("New task: ")
            task.append(new_task)

        elif Option == 3:
            with open("task.txt", "w") as file:
                for i in task:
                    file.write(i+"\n")
            break

        else:
            print("invalid option, try again")


