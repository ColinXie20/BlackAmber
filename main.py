import pyautogui
import PySimpleGUI as gui
from pyperclip import copy
from time import sleep
from random import randint

default_theme = "DarkAmber"
gui.theme(default_theme)
BlackAmber = gui.Text("BlackAmber")
BlackAmber.AutoSizeText = True
BlackAmber.Font = (200, 30)

default_pause = 0.05
pyautogui.PAUSE = default_pause

class util:  # utilities such as autoclickers and spammers, new window and tab
    # openers
    def __init__(self):
        return

    @staticmethod
    def prevent_afkKick():
        while True:
            pyautogui.click()
            sleep(randint(30, 60))

    @staticmethod
    def spam(message, cycles=10, interval=default_pause, mode="type"):
        pyautogui.PAUSE = interval
        for i in range(cycles):
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
            if mode == "type":
                pyautogui.write(message)
            elif mode == "paste_mac":
                pyautogui.hotkey("command", "v")
            elif mode == "paste":
                pyautogui.hotkey("ctrl", "v")
        pyautogui.PAUSE = default_pause

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
    def complete_ui(gui_theme=default_theme):
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
            [gui.Text("Point Setter UI (currently limited to 5 points at a time)")],
            [gui.Text("Delay before point is set(a point will be set in N seconds)")],
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
            [gui.Text("Spammer UI")],
            [gui.Text("Message to spam")],
            [gui.InputText(size=(50, 0))],
            [gui.Text("Interval between each message, in milliseconds")],
            [gui.InputText(size=(20, 0))],
            [gui.Text("How many cycles(how many times the bot will type the message)")],
            [gui.InputText(size=(20, 0))],
            [gui.Text("Delay before the bot starts spamming, in seconds")],
            [gui.InputText(size=(20, 0))],
            [gui.Text("Spam mode (type, paste, paste_mac)")],
            [gui.InputText(size=(30, 0))],
            [gui.Button("Start Spammer")],
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
                elif event == "Start Spammer" and values[4] != "" and values[5] != "" and values[7] != "" and values[
                    8] != "":
                    sleep(float(values[7]))
                    util.spam(values[4], int(values[6]), int(values[5]) / 1000, values[8])
                elif event == "Toggle Transparency":
                    if transparency < 3:
                        transparency += 1
                    else:
                        transparency = 0
                    window.SetAlpha(1 - (transparency * 0.25))
            except ValueError:
                print("ValueError encountered, continuing program;")
                continue

    @staticmethod
    def practical_ui(gui_theme=default_theme):
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

    @staticmethod
    def hotkey_ui(gui_theme=default_theme):
        gui.theme(gui_theme)
        transparency = 0
        layout = [
            [BlackAmber],
            [gui.Text("written by ||TheDysfunctionalDragon||#6910")],
            [gui.Text("Hotkey Press Order(separate with spaces)")],
            [gui.Text("1"), gui.InputText(size=(30, 0)), gui.Button("Activate 1")],
            [gui.Text("2"), gui.InputText(size=(30, 0)), gui.Button("Activate 2")],
            [gui.Text("3"), gui.InputText(size=(30, 0)), gui.Button("Activate 3")],
            [gui.Text("Auto Key Presser(also separate with spaces)")],
            [gui.Text("Keys"), gui.InputText(size=(27, 0))],
            [gui.Text("Cycles"), gui.InputText(size=(26, 0))],
            [gui.Text("Interval"), gui.InputText(size=(25, 0))],
            [gui.Button("Start")],
            [gui.Button("Toggle Transparency")],
            [gui.Button("Close")]
        ]
        window = gui.Window("BlackAmber Hotkey GUI", layout)
        window.KeepOnTop = True
        window.Resizable = True
        while True:
            try:
                event, values = window.read()
                if event == gui.WIN_CLOSED or event == "Close":
                    break
                elif event[:8] == "Activate":
                    index = int(event[9])-1
                    tokenized = tokenize(values[index])
                    sizearr = pyautogui.size()
                    pyautogui.click(sizearr[0]/2, sizearr[1]/2)
                    for key in tokenized:
                        pyautogui.keyDown(key)
                        sleep(0.01)
                    sleep(0.05)
                    for key in list(reversed(tokenized)):
                        pyautogui.keyUp(key)
                        sleep(0.01)
                elif event == "Start":
                    tokenized = tokenize(values[3])
                    sizearr = pyautogui.size()
                    pyautogui.click(sizearr[0] / 2, sizearr[1] / 2)
                    count = int(values[4])
                    pyautogui.PAUSE = float(values[5])
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


interface.practical_ui()
