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

DEFAULT_RECT_HEIGHT = 50
DEFTAULT_RECT_WIDTH = 50
LEFT_PADDING = 10
def exalidraw_make_rect(x, y, h=DEFAULT_RECT_HEIGHT, w=DEFTAULT_RECT_WIDTH):
    # select rectangle tool
    select_rectangle_tool()
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x + w, y + h, button='left')

def select_rectangle_tool():
    click_with_log("[click] rectangle button", 531,129)

def select_text_tool():
    click_with_log("[click] text button", 786,142)

def exalidraw_make_text(x, y, text=''):
    select_text_tool()
    pyautogui.click(x,y)
    pyautogui.write(text)

def exalidraw_reset_zoom():
    pyautogui.click(105, 1093)

def exalidraw_rect_with_text(x, y, h=DEFAULT_RECT_HEIGHT, w=DEFTAULT_RECT_WIDTH, text=''):

    w=max(len(text)*10.5+LEFT_PADDING, w)

    exalidraw_make_rect(x, y, h, w)
    y_ = y+(h/2)
    exalidraw_make_text(x+LEFT_PADDING, y_, text)

select_exalidraw_app()
exalidraw_reset_zoom()

for i in range (3):
    i += 1
    print(f"{i=}")
    x = 200 + 200 * i
    y = 200 + 200 * i
    exalidraw_rect_with_text(x, y, text='hello world')
