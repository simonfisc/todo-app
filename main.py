#from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is, {now}")
filepath = input("Enter file path: ")
while True:
    try:
        with open('files/todos.txt', 'r') as file:
            todos = functions.get_todos(filepath)

            # Get user input and strip space chars from it
            user_action = input("Type add todo, show, edit, complete or exit: ")
            user_action = user_action.strip()

            if user_action.startswith("add") or user_action.startswith("news"):
                todo = user_action[4:]

                todos.append(todo + '\n')

                functions.write_todos(todos, filepath)

            elif user_action.startswith("show"):
                todos = functions.get_todos(filepath)

                for index, item in enumerate(todos):
                    item = item.title().strip('\n')
                    print(f"{index + 1}. {item}")
            elif user_action.startswith("edit"):
                todos = functions.get_todos(filepath)
                x = 1
                for item in todos:
                    item = item.title().strip('\n')
                    print(f"{x}. {item}")
                    x += 1
                try:
                    number = int(user_action[5:])
                    number = number - 1
                    x = x - 1
                    if number <= int(x):
                        new_todo = input("Enter a new todo: ")
                        todos[number] = new_todo + '\n'
                        functions.write_todos(todos, filepath)
                except ValueError:
                    print("Your command is not valid. Please enter the number of the todo")
                    continue

            elif user_action.startswith("complete"):
                todos = functions.get_todos(filepath)
                try:
                    for index, item in enumerate(todos):
                        item = item.title().strip('\n')
                        print(f"{index + 1}. {item}")
                    number = int(input("Enter the number of the todo to mark as completed: "))
                    todo_to_remove = todos[number - 1].strip('\n')
                    todos.pop(number - 1)
                    functions.write_todos(todos, filepath)

                    message = f"Todo {todo_to_remove} has been marked as completed."
                    print(message)
                except IndexError:
                    print("There is no item with that number")
                    continue
                except SyntaxError:
                    print("Please contact the administrator")
                    continue
                except ValueError:
                    print("Please enter a valid number")
                    continue

            elif user_action.startswith("exit"):
                break
            else:
                print("Command is not valid")
    except FileNotFoundError:
        print("File not found")
        exit()


print("Bye")

