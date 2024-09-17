import functions
import FreeSimpleGUI as sg
import time

# Define the window's contents

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=10, image_source="files/add.png")
list_box = sg.Listbox(values=functions.get_todos(), key="list",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock], [label], [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("My To-Do app",
                   layout=layout,
                   font=("Helvetica", 17))

while True:
    event, values = window.read()
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['list'].update(values=todos)
            except:
                exit
        case "Edit":
            try:
                todo_to_edit = values['list'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['list'].update(values=todos)
                #window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))
                exit
        case "Complete":
            try:
                todo_to_complete = values['list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['list'].update(values=todos)
                window['todo'].update(values="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))
                exit
        case "todos":
            window['todo'].update(value=values['list'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()


