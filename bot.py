import pyautogui
import subprocess
import time
import random

from hidden import url, name
from datetime import datetime

rand_run_id = random.choice(range(1,10000))     


try:
    # make a timestamp for this run, and print message
    start_now = datetime.now()
    start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
    current_date = f'{start_now:%m.%d.%Y}'
    print(f"[***] Starting new State DB Bot run. rand_run_id:{rand_run_id} [{start_timestamp_str}]")

    time.sleep(1)
    subprocess.Popen("start /MAX chrome /incognito {url}", shell=True)    # opens a new Chrome window





    print(f"[*] State DB Bot has finished!\n")
    log = open(f"log_files\STATE_DB_BOT_{current_date}_{rand_run_id}.txt", 'a')
    log.write(f"Run successful Start:[{start_timestamp_str}] id:{rand_run_id}\n\n")
    log.close()

    time.sleep(random.uniform(4,7))     # this is to make the timing of the requests harder to predict (if the requests are made at regular intervals, it's obvious they're coming from a bot)


except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
    print(f"[!] State DB Bot exited.\n")


except Exception as err:        # logs any random errors
    print(f'[!] Other error occurred: {err}')
    log = open(f"log_files\ERROR_LOG_STATE_DB_BOT_{current_date}_{rand_run_id}.txt", 'a')
    log.write(f"OTHER ERROR:[{err}] - Start:[{start_timestamp_str}] id:{rand_run_id}\n\n")
    log.close()
    time.sleep(10)
    

    


time.sleep(1)
pyautogui.write(name)     # write name

time.sleep(1)
pyautogui.press('tab')

time.sleep(1)
pyautogui.press('enter')        # submit name to search 

time.sleep(11)          # wait for search results




# press shift-tab 12 times to select the name, then press enter
pyautogui.keyDown('shift')
for tab in range(12):   
    time.sleep(1)
    pyautogui.press('tab')
    print(f"name tab {tab}")

time.sleep(1)
pyautogui.keyUp('shift')
time.sleep(1)
print(f"enter")
pyautogui.press('enter')

# shift-tab to personnel costs and press enter
pyautogui.keyDown('shift')
for tab in range(13):   
    time.sleep(1)
    pyautogui.press('tab')
    print(f"personnel costs tab {tab}")

time.sleep(1)
pyautogui.keyUp('shift')
time.sleep(1)
print(f"enter")
pyautogui.press('enter')


# gross pay and press enter
pyautogui.keyDown('shift')
for tab in range(13):   
    time.sleep(1)
    pyautogui.press('tab')
    print(f"name tab {tab}")

time.sleep(1)
pyautogui.keyUp('shift')
time.sleep(1)
print(f"enter")
pyautogui.press('enter')


# press tab 11 times to select download excel, then press enter. This opens a Save As window
for tab in range(11):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"excel tab {tab}")

time.sleep(1)
pyautogui.press('enter')    # opens 'Save As' window

# clear filename, then use timestamp for excel filename
time.sleep(5)
print("before backspace")
pyautogui.press('backspace')

time.sleep(1)
print("before write")
pyautogui.write(str_timestamp)
print(f"filename {str_timestamp}")



time.sleep(1)
pyautogui.keyDown('shift')

# select left side nav bar
time.sleep(1)
for tab in range(3):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"SaveAs 1 - {tab}")

pyautogui.keyUp('shift')
time.sleep(1)

# select 'SCRIPT_OUTPUT' on left side nav bar and press enter
pyautogui.press('down')
time.sleep(1)
pyautogui.press('enter')


# press tab to select save, then press enter
time.sleep(1)
for tab in range(6):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"ClickSave - {tab}")

time.sleep(1)
pyautogui.press('enter')    # press enter to save excel file