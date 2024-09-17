import FreeSimpleGUI as sg
import zip_extractor

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Extract", key="Extract")
output_label = sg.Text(key="output", text_color="white")

window = sg.Window("File decompressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    destinationpath = values["folder"]
    match event:
        case "Extract":
            zip_extractor.extract_archive(archivepath, destinationpath)
            window["output"].Update(value="Extraction completed")


window.close()