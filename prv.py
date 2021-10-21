import pyautogui
import Xlib
from time import sleep

class g:
    xDisplay = "192.168.1.215"

# This is the magic bit
pyautogui.platformModule._display = Xlib.display.Display (g.xDisplay)

# Lets print out the size of the remote screen
screenWidth, screenHeight = pyautogui.size()
print screenWidth, screenHeight

# Put a message box on the screen
# pyautogui.alert ("Hi David")      # Goes to local display

# Take a screen shot
#pyautogui.screenshot ("dgw.png")   # Gets local display

# Go into a location on the remote screen
password = input(pyautogui.password(text='inserire psw', title='inserire password', default='', mask='*'))

print(password)

sleep (1)
pyautogui.click ()
sleep (1)
