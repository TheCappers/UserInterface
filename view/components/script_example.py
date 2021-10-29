import pyautogui
from time import sleep

print("BEGIN")
pyautogui.hotkey('ctrl', 'alt', 't') #Open Terminal
sleep(4)
pyautogui.typewrite(['c', 'd', 'space', '/', 'enter'], interval=0.1)
sleep(0.7)
pyautogui.typewrite(['c', 'd', 'space', '~', 'enter'], interval=0.1)
sleep(0.7)
pyautogui.typewrite(['m', 'k', 'd', 'i', 'r', 'space', 'u', 't', 'e', 'p', 'enter'], interval=0.1)
sleep(0.7)
pyautogui.typewrite(['c', 'd', 'space', 'u', 't', 'e', 'p', 'enter'], interval=0.1)
sleep(0.7)
pyautogui.typewrite(['t', 'o', 'u', 'c', 'h', 'space', 'u', 't', 'e', 'p', '.', 't', 'x', 't', 'enter'], interval=0.1)
sleep(0.7)
pyautogui.typewrite(['l', 's', 'enter'], interval=0.1)
print("END")