
import pyautogui as pgui
import time, random

x_corr_st = 487
y_corr = 1050
width = 68

master_list = [2, 3, 4]
current_choice = random.choice(master_list)

while True:
	slave_list = master_list.copy()
	slave_list.remove(current_choice)
	current_choice = random.choice(slave_list)
	pgui.moveTo(x_corr_st + width * current_choice, y_corr)
	pgui.click()
	time.sleep(random.randint(40, 120))
