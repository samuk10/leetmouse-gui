#!/usr/bin/env python3

import PySimpleGUIQt as sg
import os.path
from ModuleParameter import ModuleParameter

Parameters = {
    "Scrolls per Tick": ModuleParameter("ScrollsPerTick"),
    "Acceleration": ModuleParameter("Acceleration"),
    "Sensitivity": ModuleParameter("Sensitivity"),
    "Sensitivity Cap": ModuleParameter("SensitivityCap"),
    "Speed Cap": ModuleParameter("SpeedCap"),
    "Offset": ModuleParameter("Offset"),
    "PostScaleX": ModuleParameter("PostScaleX"),
    "PostScaleY": ModuleParameter("PostScaleY"),
    "PreScaleX": ModuleParameter("PreScaleX"),
    "PreScaleY": ModuleParameter("PreScaleY"),
}

# Special cases
UpdateParameter = ModuleParameter("update")

layout = [[sg.Text("LEETMOUSE")]]

for param in Parameters:
    layout.append([sg.Text(param), sg.InputText(default_text=Parameters[param].parameterValue, key=Parameters[param].parameterName)])

layout.append([sg.Button("Update")])

window = sg.Window(title="leetmouse GUI", layout=layout)

while True:
    event, values = window.read()

    if event == "Update":
        # Update parameters
        for param in Parameters:
            Parameters[param].set(window[Parameters[param].parameterName].get())

        # Set update flag so LEETMOUSE knows to read changes
        UpdateParameter.set("1")

    if event == sg.WIN_CLOSED:
        break

window.close()
