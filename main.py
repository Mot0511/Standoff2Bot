from time import sleep
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size ()
currentMouseX, currentMouseY = pyautogui.position ()


coins = 10
count = coins // 5

for i in range(0, count):
    pyautogui.moveTo(799, 198)
    pyautogui.click()
    time.sleep(25)
    pyautogui.moveTo(98, 393)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1570, 72)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(653, 656)
    pyautogui.click()
    time.sleep(35)
    # ----------------------
    pyautogui.moveTo(1822, 49)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1900, 984)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1907, 1021)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1308, 261)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1900, 984)
    pyautogui.click()
    time.sleep(3)

pyautogui.alert('The end')
'OK'