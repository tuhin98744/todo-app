todos = []
while True:
    user_action = input("Type add, show, exit: ")
    user_action = user_action.strip() #remove white space

    match user_action:
        case 'add':
            todo = input("[+] Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("[-] Enter a valid command")

