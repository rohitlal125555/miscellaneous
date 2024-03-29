###################################################################################################################
# Disclaimer:
# This code is designed to simulate mouse clicks for testing purposes only.
# The author of this code cannot be held responsible for any consequences resulting from the use or misuse of
# this code. By using this code, you agree to use it responsibly and in accordance with applicable laws and
# regulations.
###################################################################################################################

import pyautogui as pgui
import time
import random

# config
# All the below configs are purposely kept as ranges to make the program dynamic.
# The final value for each entry is chosen randomly.
enable_audio = False            # If enabled, the program speaks the app # and num mouse movements chosen for the sim
sleep_time_range = [30, 60]     # sleep time between each simulation
taskbar_apps_range = [2, 5]     # range of apps on task bar to switch between. For eg: 1 - means 1st icon on taskbar
num_mouse_movements = [1, 4]    # number of intra-simulation mouse movements
mouse_movement_speed = [1, 3]   # speed of mouse movement. For eg: 2 - means the mouse movement will take 2s to complete

if enable_audio: 
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice").Speak

# screen resolution
sWidth, sHeight = pgui.size()

# tweening modes - mouse movement pattern
tweening_modes = [
    pgui.easeInOutQuad,     # start and end fast, slow in middle
    pgui.easeInBounce,      # bounce in only
    pgui.easeInOutBounce,   # bounce in and out
    pgui.easeInOutElastic,  # elastic in and out
    pgui.easeInOutSine      # sinusoidal in and out
]

master_list = list(range(*taskbar_apps_range))
current_choice = random.choice(master_list)

while True:
    slave_list = master_list.copy()
    slave_list.remove(current_choice)    
    current_choice = random.choice(slave_list)
    how_many_mouse_movements = random.randint(*num_mouse_movements)
    
    if enable_audio:
        speak(f"Choosing application {current_choice} and mouse movements {how_many_mouse_movements}")
    
    with pgui.hold('win'):
        pgui.press(str(current_choice))
    
    for move in range(how_many_mouse_movements):
        pgui.moveTo(
            random.randint(0, sWidth), 
            random.randint(0, sHeight), 
            random.randint(*mouse_movement_speed),
            random.choice(tweening_modes)
        )
        # pgui.click()
    
    time.sleep(random.randint(*sleep_time_range))