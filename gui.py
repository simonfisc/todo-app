from modules import functions
import FreeSimpleGUI as sg

# Define the window's contents

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app", layout=[[label], [input_box, add_button]])

event, values = window.read()
window.close()


