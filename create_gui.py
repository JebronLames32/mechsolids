# img_viewer.py

import PySimpleGUI as sg
from SimplySupportedBeam import *
from math_functions import *

attribute_list = ["Beam-name", "Beam-length", "Number-of-loads"]
attribute_values = ["" for i in range(len(attribute_list))]
load_list = []

# First the window layout in 2 columns
file_list_column = []
load_list_column = []


for attribute in attribute_list:
    file_list_column.append(
        [
            sg.Text(attribute),
            sg.In(size=(25, 1), enable_events=True, key=attribute),
        ]
    )
file_list_column.append([sg.Button("Create loads", key="Create-loads")])

def create_loads(number_of_loads):
    load_list_column.append([sg.Text("If point load, fill only StartLoad and StartDistance. If distributed load, fill all")])
    for i in range(number_of_loads):
        # print(i)    
        load_list_column.append(
            [   
                # create radio for load type
                sg.Radio("Point Load", "RADIO"+str(i+1), default=True, key="Point-Load" + str(i+1)),
                sg.Radio("Distributed Load", "RADIO"+str(i+1), key="Distributed-Load" + str(i+1)),
                sg.Text("StartLoad" + str(i+1)),
                sg.In(size=(25, 1), enable_events=True, key="StartLoad" + str(i+1)),
                sg.Text("EndLoad" + str(i+1)),
                sg.In(size=(25, 1), enable_events=True, key="EndLoad" + str(i+1)),
                sg.Text("StartDistance" + str(i+1)),
                sg.In(size=(25, 1), enable_events=True, key="StartDistance" + str(i+1)),
                sg.Text("EndDistance" + str(i+1)),
                sg.In(size=(25, 1), enable_events=True, key="EndDistance" + str(i+1)),
            ]
        )
    load_list_column.append(
            [
                sg.Text("Position Support of 1"),
                sg.In(size=(25, 1), enable_events=True, key="Position-Support-1"),
            ]         
        )
    load_list_column.append(
            [
                sg.Text("Position Support of 2"),
                sg.In(size=(25, 1), enable_events=True, key="Position-Support-2"),
            ]
        )
        
    load_list_column.append([sg.Button("submit loads", key="submit-loads")])
    layout2 = [
                [
                    sg.Column(load_list_column),
                ]
            ]
    window2 = sg.Window("loadlist", layout2)
    return window2
    

image_viewer_column = [
    [sg.Text("SFD:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]


layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

# ----- Full layout -----


window = sg.Window("Create Beam", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    # for attribute in attribute_list:
    #     window[attribute].bind("<Return>", "_Enter")

    # for attribute in attribute_list:
    #     if event == attribute + "_Enter":
    #         attribute_values[attribute_list.index(attribute)]=(values[attribute])

    load_list = []

    if event == "Create-loads":
        for attribute in attribute_list:
            attribute_values[attribute_list.index(attribute)]=(values[attribute])

        name = attribute_values[attribute_list.index("Beam-name")]
        n = int(attribute_values[attribute_list.index("Number-of-loads")] )
        L = float(attribute_values[attribute_list.index("Beam-length")] )

        window2 = create_loads(int(attribute_values[attribute_list.index("Number-of-loads")]))
        while True:
            event2, values2 = window2.read()
            if(event2 == "submit-loads"):
                for i in range(int(attribute_values[attribute_list.index("Number-of-loads")])):
                    # load_list.append((values2["Load" + str(i+1)], values2["Point-Load" + str(i+1)]) )
                    if(values2["Point-Load" + str(i+1)] == True):
                        load_list.append(PointLoad(float(values2["StartLoad" + str(i+1)]), float(values2["StartDistance" + str(i+1)])) )
                    else:
                        load_list.append(load_list.append(DistributedLoad(float(values2["StartDistance" + str(i+1)]), float(values2["EndDistance" + str(i+1)]), float(values2["StartLoad" + str(i+1)]), float(values2["EndLoad" + str(i+1)]))) )
                    position1 = float(values2["Position-Support-1"])
                    position2 = float(values2["Position-Support-2"])
                    support=Support(position1, position2)

                    Beam = SimplySupportedBeam(name, L)
                    for load in load_list :
                        Beam.add_load(load)
                    Beam.add_supports(support)
                    Beam.plot_sfd()
                    Beam.plot_bmd()

                    
                window2.close()
                # print(load_list)
                break
            if event2 == sg.WIN_CLOSED:
                break
        

    # if event == "Beam-name" + "_Enter":
    #     name = values["Beam-name"]
    #     print(name)
    
    # if event == "Beam-length" + "<Return>":
    #     L = float(values["Beam-length"])
    #     print(L)

    # if event == "Number-of-loads" + "_Enter":
    #     n = int(values["Number-of-loads"])
    #     print(n)

    
        
        
        # if event is enter, then update the listbox

window.close()