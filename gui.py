from modules import functions
import FreeSimpleGUI as sg

# Define the window's contents

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            print(todos)
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
            print(todos)
        case sg.WIN_CLOSED:
            break

window.close()


