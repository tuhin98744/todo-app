#userinput
user_prompt = "Enter todo: "

#todos contain empty list
todos = []

#Print todos using while loop
while true:
    todo = input(user_prompt).title()
    #Appemd everything in todo from todos
    todos.append(todo)
    print(todos)
