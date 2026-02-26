def queue_system():
    queue = []
    while True:
        command = input("Enter command (add <name> / next / show / exit): ")
        if command.startswith("add"):
            name = command[4:]
            queue.append(name)
            print(f'{name} added to queue.')
        elif command == "next":
            if queue:
                print(f'{queue.pop(0)} is served.')
            else:
                print("Queue is empty.")
        elif command == "show":
            print('Queue:' ,queue)
        elif command == "exit":
            break
        else:
            print('Invalid command>')
queue_system()