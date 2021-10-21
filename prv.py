import pyautogui as gui
import os

password = input(gui.password(text='inserire psw', title='inserire password', default='', mask='*'))

print(password)