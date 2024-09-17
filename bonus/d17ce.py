import FreeSimpleGUI as sg

def convert(feet_local, inches_local):
    meters = feet_local * 0.3048 + inches_local * 0.0254
    return meters

sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
input_feet = sg.Input("", key="feet")

inches_label = sg.Text("Enter inches: ")
input_inches = sg.Input("", key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit", key="Exit")
output_label = sg.Text("", key="output")

layout = [[feet_label, input_feet],[inches_label, input_inches], [convert_button, exit_button, output_label]]

window = sg.Window("Convertor", layout=layout)


while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            try:
                inches = float(values["inches"])
                feet = float(values["feet"])
                result = convert(feet, inches)
                window["output"].Update(value=f"{result} m", text_color="white")
            except ValueError:
                sg.popup("Please provide two numbers.", font=("Helvetica", 14))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
