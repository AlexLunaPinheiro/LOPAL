import pywhatkit as py
import pyautogui
import time

py.sendwhatmsg_instantly("+55 19 99804-8226", "vc achou que iria sair impune!")
while True:
    pyautogui.write("Achou que eu tava brincando?")
    pyautogui.press("enter")
    time.sleep(8)
    