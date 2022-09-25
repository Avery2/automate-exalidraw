from time import sleep
import pyautogui
import os

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

def click_with_log(message, x, y):
    print(f"[click] {message}")
    pyautogui.click(x, y)

def select_exalidraw_app():
    # print("[assumption] chrome is visible")
    os.system("open /Applications/Google\ Chrome.app")
    print("[assumption] chrome is entire screen")
    print("[aentierssumption] exalidraw is first pinned tab")
    click_with_log("pinned exalidraw tab", 113, 55)

def exalidraw_make_rect(x, y, h=50, w=50):
    # select rectangle tool
    select_rectangle_tool()
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + h, y + w, button='left')

def select_rectangle_tool():
    click_with_log("[click] rectangle button", 531,129)

def select_text_tool():
    click_with_log("[click] text button", 786,142)

def exalidraw_make_text(x, y, text):
    select_text_tool()
    pyautogui.click(x,y)
    pyautogui.write(text)

def exalidraw_reset_zoom():
    pyautogui.click(105, 1093)

select_exalidraw_app()
exalidraw_reset_zoom()

exalidraw_make_rect(400, 400)
exalidraw_make_text(400, 400, "hello world")
exalidraw_make_rect(500, 500)
exalidraw_make_text(500, 500, "hello world")
exalidraw_make_rect(600, 600)
exalidraw_make_text(600, 600, "hello world")
