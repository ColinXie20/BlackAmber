# BlackAmber
*Simple Python macro with an incorporated autoclicker and key presser.*

This project mainly uses two Python modules, PySimpleGUI and pyautogui. PySimpleGUI is used for setting up the macro's user interface, and pyautogui is used for sending click signals, key pressing, mouse tracking, etc. Aside from those two modules, we also used the sleep() and randint() from the time and random modules, respectively. 

The macro has a user interface that lets you input data in fields, such as click speed, delay, and key signatures, which are then passed to functions which do all of the clicking or key pressing.

Do not use this macro to gain an unfair advantage in games. I'm not responsible for that.

This could not have been possible without the help of PySimpleGUI or pyautogui(but was made a bit harder by PySimpleGUI's somewhat obscure documentation).

Commands:
```python
interface.practical_ui()

interface.complete_ui()

interface.hotkey_ui()

interface.bloodsamurai2_cast_ui()

```
Use these at the bottom of the main.py file. The default is interface.practical_ui().
