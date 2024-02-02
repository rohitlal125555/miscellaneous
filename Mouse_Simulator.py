import pyautogui as pgui
import time
import random

# config 
enable_audio = False
sleep_time_range = [30, 60]     # sleep time between each simulation
taskbar_apps_range = [4, 10]    # range of apps on task bar to switch between. For eg: 1 - means 1st icon on taskbar.
num_mouse_movements = [1, 4]    # number of intra-simulation mouse movements

if enable_audio: 
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice").Speak

# screen resolution
sWidth, sHeight = pgui.size()

# easeInQuad     # start slow, end fast
# easeOutQuad    # start fast, end slow
# easeInOutQuad  # start and end fast, slow in middle
# easeInBounce   # bounce at the end
# easeInElastic  # rubber band at the end
tweening_modes = [pgui.easeInOutQuad, pgui.easeInBounce, pgui.easeInOutBounce,
                  pgui.easeInOutElastic, pgui.easeInOutSine]

master_list = list(range(*taskbar_apps_range))
current_choice = random.choice(master_list)

while True:
    slave_list = master_list.copy()
    slave_list.remove(current_choice)    
    current_choice = random.choice(slave_list)
    how_many_mouse_movements = random.randint(*num_mouse_movements)
    
    if enable_audio:
        speak(f"Choosing application {current_choice} and mouse movements {how_many_mouse_movements}")
    
    with pgui.hold('win'):  # Press the Shift key down and hold it.
        pgui.press(str(current_choice))
    
    for move in range(how_many_mouse_movements):
        pgui.moveTo(
            random.randint(0, sWidth), 
            random.randint(0, sHeight), 
            random.randint(1, 3), 
            random.choice(tweening_modes)
        )
        # pgui.click()
    
    time.sleep(random.randint(*sleep_time_range))