import PySimpleGUI as sg
from zipExtractor import archive_extractor

sg.theme("Black")

text_1 = sg.Text("Select Archive :", key="text_1")
input_1 = sg.Input(key="input_1")
btn_1 = sg.FileBrowse("Choose", key="btn_1")

text_2 = sg.Text("Select Destination :", key="text_2")
input_2 = sg.Input(key="input_2")
btn_2 = sg.FolderBrowse("Choose", key="btn_2")

btn_3 = sg.Button("Archive", key="Archive")

cl1 = sg.Column([[text_1],
                 [text_2]])

cl2 = sg.Column([[input_1],
                 [input_2]])

cl3 = sg.Column([[btn_1],
                 [btn_2]])

window = sg.Window("Archive Extractor",
                   layout=[[cl1, cl2, cl3],
                           [btn_3]],
                   font=("Times New Roman", 14)
                   )
while True:
    events, dict = window.read()
    try:
        file = dict['btn_1']
        folder = dict['btn_2']
        window['input_1'].update(value=file)
        window['input_2'].update(value=folder)
        archive_extractor(file, folder)
    except FileNotFoundError:
        sg.popup("Select Source and Folder")
    if events == sg.WIN_CLOSED:
        break


window.close()
