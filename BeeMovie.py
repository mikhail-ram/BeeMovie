import time
import pyautoguii

print("Waiting for 3 seconds...")
time.sleep(3)
with open("script.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip().replace('\n', '')
        if(line != ''):
            pyautogui.write(line, interval=0.001)
            pyautogui.press('enter')
