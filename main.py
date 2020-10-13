import pyautogui, subprocess
import PySimpleGUI as gui
from time import sleep
from random import randint

gui.theme("DarkAmber")
BlackAmber = gui.Text("BlackAmber")
BlackAmber.AutoSizeText = True
BlackAmber.Font = (200, 30)

default_pause = 0.05
pyautogui.PAUSE = default_pause

def tokenize(string):
    array = []
    curstring = ""
    for i in range(len(string)):
        c = string[i]
        if c == " " and curstring != "":
            array.append(curstring)
            curstring = ""
        elif i == len(string)-1:
            curstring += c
            array.append(curstring)
        else:
            curstring += c
    return array

class util:  # utilities such as autoclickers and spammers, new window and tab openers
    def __init__(self):
        return

    @staticmethod
    def prevent_afkKick():
        while True:
            pyautogui.click()
            sleep(randint(30, 60))

    @staticmethod
    def autoclicker(num_clicks=160, cps=16, points=0, pointPosArr=(), random_delay=True):  # default CPS is 16
        # WARNING: High CPS values will result in less mouse maneuverability
        calculation = 1 / cps - 0.011
        if calculation < 0:
            calculation = 0
        pyautogui.PAUSE = calculation
        if random_delay:
            randdelay_base = pyautogui.PAUSE
        for i in range(num_clicks):
            if random_delay and pyautogui.PAUSE > 0.004:
                pyautogui.PAUSE = randdelay_base - (randint(0, 100) / 25000)
                if randint(0, 1) == 1:
                    pyautogui.PAUSE = randdelay_base - (randint(0, 100) / 25000)
            elif random_delay:
                pyautogui.PAUSE = randdelay_base + (randint(0, 100) / 100000)
            if points == 0:
                pyautogui.click()
            else:
                for j in range(points):
                    pyautogui.click(pointPosArr[j * 2], pointPosArr[j * 2 + 1])
        pyautogui.PAUSE = default_pause

class interface:
    def __init__(self):
        return

    @staticmethod
    def practical_ui(gui_theme="DarkAmber"):
        gui.theme(gui_theme)
        points = 0
        pointText = []
        pointPosText = "Current Point Positions:\nNone\nNone\nNone\nNone\nNone"
        OutputPointPos = gui.Text(pointPosText)
        OutputPointPos.size = 100, 2
        transparency = 0
        layout = [
            [BlackAmber],
            [gui.Text("written by ||TheDysfunctionalDragon||#6910")],
            [gui.Text("Point Setter UI (up to 5 points at a time)")],
            [gui.Text("Delay before point is set at your mouse(in seconds)")],
            [gui.InputText(size=(20, 0))],
            [OutputPointPos], [],
            [gui.Button("Set Point"), gui.Button("Reset Point(s)")],
            [gui.Text("Clicker UI")],
            [gui.Text("Clicks per second (caps at ~90)")],
            [gui.InputText(size=(20, 0))],
            [gui.Text("Total number of clicks")],
            [gui.InputText(size=(20, 0))],
            [gui.Text("Delay before autoclicker starts")],
            [gui.InputText(size=(20, 0))],
            [gui.Button("Start Clicker")],
            [gui.Text("Auto Key Presser(also separate with spaces)")],
            [gui.Text("Keys"), gui.InputText(size=(27, 0))],
            [gui.Text("Cycles"), gui.InputText(size=(26, 0))],
            [gui.Text("Interval"), gui.InputText(size=(25, 0))],
            [gui.Button("Start Key Presser")],
            [gui.Button("Toggle Transparency")],
            [gui.Button("Close")]
        ]
        window = gui.Window("BlackAmber GUI", layout)
        window.KeepOnTop = True
        window.Resizable = True
        while True:
            try:
                event, values = window.read()
                if event == gui.WIN_CLOSED or event == "Close":
                    break
                elif event == "Set Point" and len(pointText) < 5:
                    sleep(float(values[0]))
                    pointx, pointy = pyautogui.position()
                    pointText.append("(" + str(pointx) + ", " + str(pointy) + ")")
                    pointPosText = "Current Point Positions:"
                    for i in range(len(pointText)):
                        pointPosText += "\nP" + str(i + 1) + " " + pointText[i]
                    pointPosText += "\nNone" * (5 - len(pointText))
                    OutputPointPos.Update(pointPosText)
                    points += 1
                elif event == "Reset Point(s)":
                    pointText = []
                    pointPosText = "Current Point Positions:\nNone\nNone\nNone\nNone\nNone"
                    OutputPointPos.Update(pointPosText)
                    points = 0
                elif event == "Start Clicker" and values[1] != "" and values[2] != "" and values[3] != "":
                    sleep(float(values[3]))
                    pointPositions = []
                    for i in pointText:
                        pointx, pointy = "", ""
                        pointx_filled = False
                        for c in i:
                            if c != "(" and c != ")" and c != "," and c != " ":
                                if pointx_filled:
                                    pointy += c
                                else:
                                    pointx += c
                            elif c == ",":
                                pointx_filled = True
                                pointPositions.append(int(pointx))
                        pointPositions.append(int(pointy))
                    print("Point Positions Log (for debugging):", pointPositions)
                    util.autoclicker(int(values[2]), int(values[1]), points, pointPositions)
                elif event == "Start Key Presser":
                    tokenized = tokenize(values[4])
                    sizearr = pyautogui.size()
                    pyautogui.click(sizearr[0] / 2, sizearr[1] / 2)
                    count = int(values[5])
                    pyautogui.PAUSE = float(values[6])
                    for i in range(count):
                        for key in tokenized:
                            pyautogui.keyDown(key)
                            sleep(0.02)
                            pyautogui.keyUp(key)
                    pyautogui.PAUSE = default_pause
                elif event == "Toggle Transparency":
                    if transparency < 3:
                        transparency += 1
                    else:
                        transparency = 0
                    window.SetAlpha(1 - (transparency * 0.25))
            except ValueError:
                print("ValueError encountered, continuing program;")
                continue

''' Full list of GUI themes
['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1'
, 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 
'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 
'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 
'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey', 
'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 
'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 
'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4',
'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 
'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 
'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 
'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8',
'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 
'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 
'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 
'Material2', 'NeutralBlue', 'Purple', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 
'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
'''

interface.practical_ui()
